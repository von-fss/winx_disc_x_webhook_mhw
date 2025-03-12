import _utils as ut


from datetime import datetime
import requests
import json

from discord_webhook import DiscordWebhook

######## Steps for sucess !!! ##########
#### Get the last posts X

id: int = ut.x_user['username_id']
config: dict = ut.get_config()

print(config)

# x_last_posts: dict = ut.x_get_posts(id, config)

##### mocked version ######
# mocked_string = '''{"data":[{"created_at":"2025-03-12T17:01:06.000Z","edit_history_tweet_ids":["1899868262973780255"],"id":"1899868262973780255","text":"Since Ajarakan fights with powerful punches, the shape of a fist is included in the Sword &amp; Shield, almost like a gauntlet. Fighting with this set looks as if the hunter is punching with a flame-clad left fist, and guarding with their right arm. #MHWilds https://t.co/NmM9Ybbt9X"},{"created_at":"2025-03-12T10:59:46.000Z","edit_history_tweet_ids":["1899777331025072328"],"id":"1899777331025072328","text":"Hunters! Did you know we have some dedicated regional accounts for Monster Hunter? \\n\\nFR: @MH_Officiel_FR\\nDE: @DEMonsterHunter\\nES: @ESMonsterHunter\\nAR: @MonsterHunterAR\\nPL: @MonsterHunterPL\\n\\nIf any catch your interest, drop them a follow for localised content and more! https://t.co/YwRdoIu7Qk"},{"created_at":"2025-03-12T00:56:03.000Z","edit_history_tweet_ids":["1899625399191060987"],"id":"1899625399191060987","text":"\\uD83D\\uDCDC EVENT QUEST \\uD83D\\uDCDC\\n\\nA Tempered Chatacabra stands between you and a pile of Hard and Advanced Armor Spheres in \\"Tongue-Tied\\"!\\n\\nThis quest joins last week\'s \\"Kut-Ku Gone Cuckoo\\" that has special headgear material rewards!\\n\\nBoth available until Mar. 18, 4:59pm PT / 23:59pm GMT. https://t.co/GTvRPIPuhQ"},{"created_at":"2025-03-11T20:17:26.000Z","edit_history_tweet_ids":["1899555283636036040"],"id":"1899555283636036040","text":"What are your current primary and secondary weapons in #MHWilds? https://t.co/Ik4U969r42"},{"created_at":"2025-03-10T17:14:23.000Z","edit_history_tweet_ids":["1899146829461168452"],"id":"1899146829461168452","text":"The Ajarakan hunter armor\'s silhoutte resembles flames, while the design draws on elements of Japanese legends. The Palico armor is heavily inspired by guardian dog statues (Koma-inu) found in Japan, to express the Palico\'s duty to protect hunters. #MHWilds https://t.co/C9bxaozZHd"}],"meta":{"result_count":5,"newest_id":"1899868262973780255","oldest_id":"1899146829461168452","next_token":"7140dibdnow9c7btw4b3o57y8s02a2rrmuc3dhbzl6ipe"}}'''

# class MockResponse:
#     def __init__(self, json_data):
#         self._json = json_data

#     def json(self):
#         return self._json

# x_last_posts = MockResponse(json.loads(mocked_string))

#########################################

#### Get the last posted date on the local database

last_date: str = ut.winxdb_get_last_date()

#### Check if there any new post on X

# x_posts_check: list = [
#     [
#         posts['id'], 
#         posts['text'], 
#         posts['created_at'],
#         0 if datetime.fromisoformat(posts['created_at'].replace('Z', '+00:00')) > datetime.fromisoformat(last_date.replace('Z', '+00:00')) else 1
#     ] 
#     for posts in x_last_posts
# ]

# x_new_posts = [posts for posts in x_posts_check if posts[3] == 0]

#### Insert the new post in the database

# if x_new_posts:
#     ut.winxdb_insert(x_new_posts)
# else:
#     print("No new post to insert in WinxDb")

# mocked_return = [['1899868262973780255',
#  'Since Ajarakan fights with powerful punches, the shape of a fist is included in the Sword &amp; Shield, almost like a gauntlet. Fighting with this set looks as if the hunter is punching with a flame-clad left fist, and guarding with their right arm. #MHWilds https://t.co/NmM9Ybbt9X',
#  '2025-03-12T17:01:06.000Z',
#  0]] 

#### get the post not published in discord

publish_list: list = ut.winxdb_post_for_publish()
print(publish_list)

# publish_links: list = [(post[0], f"https://x.com/{ut.x_user['username']}/status/{post[0]}") for post in publish_list]

#### Update database column published to 1

# for link in publish_links:
#     webhook = DiscordWebhook(url=config['winx_url'], content=link[1])
#     response = webhook.execute()
#     print(f"Message sent to discord with link = {link[1]}")

#     try:
#         ut.winxdb_update_published(link[0])
#     except Exception as e:
#         print(f"Database not updated with link {link[1]}")