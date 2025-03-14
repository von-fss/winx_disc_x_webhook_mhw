from discord_webhook import DiscordWebhook
from config.configuration import keys
from database.winx_database import WinxDatabaseQuery
import logging

def discord_publish(publish_links: list):
    winx_db: WinxDatabaseQuery = WinxDatabaseQuery()
    for link in publish_links:
        webhook = DiscordWebhook(url=keys['winx_url'], content=link[1])
        response = webhook.execute()
        logging.info(f"Message sent to discord with link = {link[1]}")
        try:
            winx_db.update_published(link[0])
        except Exception as e:
            logging.error(f"Database not updated with link {link[1]}")
            webhook.delete()