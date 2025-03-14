from datetime import datetime
import logging

from database.winx_database import WinxDatabaseQuery
from config.configuration import target_user

winx_db = WinxDatabaseQuery()

def get_new_posts(x_last_posts: dict, last_date: str) -> list:
    x_posts_check: list = [
        [
            posts['id'], 
            posts['text'], 
            posts['created_at'],
            0 if datetime.fromisoformat(posts['created_at'].replace('Z', '+00:00')) > datetime.fromisoformat(last_date.replace('Z', '+00:00')) else 1
        ] 
        for posts in x_last_posts
    ]
    x_new_posts: list = [posts for posts in x_posts_check if posts[3] == 0]
    return x_new_posts

def insert_new_posts(x_new_posts: list) -> None:
    if x_new_posts:
        winx_db.insert(x_new_posts)
    else:
        print(f'No new post to insert in WinxDb')

def post_for_publish() -> list:
    publish_list: list = winx_db.post_for_publish()
    if not publish_list:
        logging.info(f'No post for publish - {publish_list}')
    publish_links: list = [(post[0], f"https://x.com/{target_user["username"]}/status/{post[0]}") for post in publish_list]

    return publish_links