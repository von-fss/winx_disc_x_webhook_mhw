import atexit
import sqlite3
from sqlite3 import Cursor, Connection
from typing import Optional
import logging
from contextlib import contextmanager

import inspect

def func_name() -> str:
    return inspect.currentframe().f_back.f_code.co_name

class WinxDatabase:
    def __init__(self):
        self.connection: Optional[Connection] = None
        self.winx_table: str = 'last_posts'
        self.winx_db: str = 'winx_webhook'

    def get_connection(self) -> None:
        if self.connection is None:
            self.connection = sqlite3.connect(f'database/{self.winx_db}.db')
            atexit.register(self.close_connection)
            logging.info(f'{self.winx_db} connected')

    def close_connection(self) -> None:
        if self.connection:
            self.connection.close()
            logging.info(f'{self.winx_db} connection closed')

class WinxDatabaseQuery(WinxDatabase):
    def __init__(self):
        super().__init__()
        super().get_connection()

    @contextmanager
    def get_cursor(self, cursor_type: str) -> Cursor:
        cur: Cursor = self.connection.cursor()
        try:
            logging.info(f'Cursor oppened - {cursor_type}')
            yield cur
        finally:
            cur.close()
            logging.info(f'Cursor closed - {cursor_type}')

    def get_last_date(self) -> str:
        with self.get_cursor(func_name()) as cur:
            cur.execute(f'select max(created_at) from {self.winx_table}')
            last_date = cur.fetchone()
            logging.info(f'get last date sucess -> {last_date}')
        return last_date[0]
    
    def insert(self, posts: list) -> None:
        with self.get_cursor(func_name()) as cur:
            columns: str = 'x_id, post_content, created_at, published'
            try:
                cur.executemany(f'insert into {self.winx_table} ({columns}) values (?, ? ,? ,?)', posts)
                cur.connection.commit()
                logging.info(f'Post of X id {posts[0]}, inserted')
            except Exception as e:
                logging.error(f'Error when inserting values to {self.winx_table} -> ', e)

    def post_for_publish(self) -> list:
        with self.get_cursor(func_name()) as cur:
            cur.execute(f'select * from {self.winx_table} where published = 0')
            posts: list = cur.fetchall()
            return posts

    def update_published(self, update_id: int) -> None:
        with self.get_cursor(func_name()) as cur:
            try:
                cur.execute(f'update {self.winx_table} set published = 1 where x_id = {update_id}')
                cur.connection.commit()
                logging.info(f'winx_id = {update_id} updated to 1 in {self.winx_table}')
            except Exception as e:
                logging.error(f'Cannot update table {self.winx_table}', e)