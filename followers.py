import requests

url_path = input('Write the link of account:\n>> ')

name = url_path.split('/')[-1].lower()

res = requests.get(f'https://api.twitter.com/graphql/'
                   f'-xfUfZsnR_zqjFd-IfrN5A/UserByScreenName?'
                   f'variables={{"screen_name":"{name}",'
                   f'"withHighlightedLabel":true}}',
                   headers={'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'})
res.raise_for_status()

print('Followers count: ' + str(res.json()['data']['user']['legacy']['followers_count']))
