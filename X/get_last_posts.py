import sys
import logging
import requests

from ._utils import x_get_posts, XRequestConfig

def get_last_posts() -> dict:
    try:
        x_last_posts: dict = x_get_posts(XRequestConfig)
        logging.info('posts retrieved')
        return x_last_posts
    except requests.exceptions.HTTPError as e:
        logging.error(f"Request failed: {e}")
        sys.exit(1)