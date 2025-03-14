import json
from dataclasses import dataclass

keys: dict = {
    'winx_url':'',
    'x_api_consumer_key':'',
    'x_api_consumer_key_secret':'',
    'x_api_name':'',
    'x_api_bearer_token':''
}

target_user: dict = {
    'username':'monsterhunter',
    'id':306490355
}

@dataclass
class XRequestConfig:
    url: str
    headers: dict
    params: dict

    @staticmethod
    def get_config(bearer_token: str, id: int) -> 'XRequestConfig':
        url = f'https://api.twitter.com/2/users/{id}/tweets'
        headers = {'Authorization': f'Bearer {bearer_token}'}
        params = {'max_results': 5, 'tweet.fields':'created_at'}
        return XRequestConfig(url=url, headers=headers, params=params)
    
x_config = XRequestConfig.get_config(keys["x_api_bearer_token"], target_user["id"])