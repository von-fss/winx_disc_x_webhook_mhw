import sqlite3
import atexit
import requests
import logging
import json
from sqlite3 import Cursor, Connection
from typing import Optional

x_user: dict = {
    "username":"monsterhunter",
    "username_id":306490355
}

def get_config() -> json:
    with open('configuration.json', 'r') as file:
        x_config = json.load(file)
    return x_config

def x_get_posts(id: int, x_config: dict) -> dict:
    url = f"https://api.twitter.com/2/users/{id}/tweets"
    headers = {"Authorization": f"Bearer {x_config['x_api_bearer_token']}"}
    params = {"max_results": 5, "tweet.fields":"created_at"}

    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 429:
            print("status_code 429")
            return None

        response.raise_for_status()
        response_dict = response.json()

        if 'data' not in response_dict:
            logging.warning(f"No data found in API response for user {id}. Response: {response_dict}")
            return None
        return response_dict['data']
    
    except requests.exceptions.RequestException as e:
        logging.error(f"HTTP Request failed: {e}")
    except ValueError:
        logging.error(f"Failed to decode JSON response: {response.text}")

    return None

connection: Optional[Connection] = None
winx_table: str = "last_posts"
winx_db: str = "winx_webhook"

def get_cursor() -> Cursor:
    global connection
    global winx_db

    if connection is None:
        connection = sqlite3.connect(f"{winx_db}.db")
        atexit.register(close_connection)
        print(f"{winx_db} connected")
    cur: Cursor = connection.cursor()
    return cur

def close_connection() -> None:
    global connection
    global winx_db

    if connection:
        connection.close()
        print(f"{winx_db} connection closed")

def winxdb_get_last_date() -> str:
    cur: Cursor = get_cursor()
    res: Cursor = cur.execute(f"select max(created_at) from {winx_table}")

    last_date = res.fetchone()
    cur.close()
    print(f'get last date sucess -> {last_date}')
    return last_date[0]

def winxdb_insert(posts: list) -> None:
    cur: Cursor = get_cursor()
    columns: str = "x_id, post_content, created_at, published"
    try:
        cur.executemany(f"insert into {winx_table} ({columns}) values (?, ? ,? ,?)", posts)
        cur.connection.commit()
    except Exception as e:
        print(f"Error when inserting values to {winx_table} -> ", e)
    finally:
        cur.close()
        print(f"Post of X id {posts[0]}, inserted")
    
def winxdb_post_for_publish() -> list:
    cur: Cursor = get_cursor()
    posts_publish: Cursor = cur.execute(f"select * from {winx_table} where published = 0")
    posts: list = posts_publish.fetchall()
    cur.close()
    return posts

def winxdb_update_published(update_id: int) -> None:
    cur: Cursor = get_cursor()
    try:
        cur.execute(f"update {winx_table} set published = 1 where x_id = {update_id}")
        cur.connection.commit()
        print(f"winx_id = {update_id} updated to 1 in {winx_table}")
    except Exception as e:
        print(f"Cannot update table {winx_table}", e)
    finally:
        cur.close()