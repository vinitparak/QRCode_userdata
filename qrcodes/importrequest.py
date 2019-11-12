import urllib.request
import json
url='https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=activity&q=facebook&site=stackoverflow'
json_obj=urllib.request.urlopen('http://www.reddit.com/r/all/top/.json').read()
data=json.load(json_obj)