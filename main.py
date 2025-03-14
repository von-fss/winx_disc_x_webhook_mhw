import config.logging_config
import logging

from _utils import winx_db, get_new_posts, insert_new_posts, post_for_publish

from X.get_last_posts import get_last_posts
from X.get_last_posts_mocked import get_mocked_response

from discord.webhook import discord_publish

x_last_posts: dict = get_last_posts()
# x_last_posts: dict = get_mocked_response()

last_date: str = winx_db.get_last_date()
x_new_posts = get_new_posts(x_last_posts, last_date)

insert_new_posts(x_new_posts)

#### get the post not published in discord

publish_links: list = post_for_publish()

## Publish in discord

discord_publish(publish_links)