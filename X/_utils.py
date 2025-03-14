from dataclasses import dataclass
import requests
from requests import Response
import logging
import sys

from config.configuration import keys, target_user

XRequestConfig: dict = {
    'url' : f'https://api.twitter.com/2/users/{target_user["id"]}/tweets',
    'headers' : {'Authorization': f'Bearer {keys["x_api_bearer_token"]}'},
    'params' : {'max_results': 5, 'tweet.fields':'created_at'}
}
   
def x_get_posts(config: dict) -> dict:
    try:
        response: Response = requests.get(config["url"], headers=config["headers"], params=config["params"])

        if response.status_code == 429:
            logging.error('Rate limit exceeded (429)')
            response.raise_for_status()
            raise requests.exceptions.HTTPError('Rate limite exceeded (429)')
        response_dict = response.json()

        if 'data' not in response_dict:
            logging.warning(f'No data found in API response for user {id}. Response: {response_dict}')
            raise ValueError('No data found in API response')
        return response_dict['data']
    
    except requests.exceptions.RequestException as e:
        logging.error(f'HTTP Request failed: {e}')
        sys.exit(1)

    except ValueError:
        logging.error(f'Failed to decode JSON response: {response.text}')
        sys.exit(1)