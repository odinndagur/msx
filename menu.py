import json
import requests
import json
import time
from operator import itemgetter

item = {
    'sid': '4785',
    'pid': '1dk8gh',
}

def requestsVodDataRetrieveWithRetries(sid = None, pid = None):
    graphdata = '?operationName=getProgramType&variables={"id":'+sid +',"episodeId":["'+pid+'"]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"9d18a07f82fcd469ad52c0656f47fb8e711dc2436983b53754e0c09bad61ca29"}}'
    retries_left = 3

    while True:
        retries_left = retries_left - 1
        r = requests.get(
        url='https://www.ruv.is/gql/'+graphdata, 
        headers={'content-type': 'application/json', 'Referer' : 'https://www.ruv.is/sjonvarp', 'Origin': 'https://www.ruv.is' })
        data = json.loads(r.content.decode())

        if 'data' in data:
            return data

        if retries_left <= 0:
            return None

        if not 'errors' in data:
            print("Unexpected data in VOD download reply, "+str(data))
            return None

        # OK we will try again, but first we sleep a little bit to throttle the requests
        time.sleep(3)

with open('/Users/odinndagur/Code/sarpur/tvschedule.json', 'r') as f:
    schedule = json.loads(f.read())

download_list = []
    
for key, schedule_item in schedule.items():
    if key == 'date' or not 'pid' in schedule_item:
        continue
    candidate_to_add = schedule_item
    download_list.append(candidate_to_add)

download_list = sorted(download_list, key=itemgetter('pid', 'title'))
download_list = sorted(download_list, key=itemgetter('showtime'), reverse=True)
# print('\n'.join([f"{f['title']}\t{f['desc']}" for f in download_list]))

def alt_get_vod(item):
    # print(item)
    data = requestsVodDataRetrieveWithRetries(sid=item['sid'],pid=item['pid'])
    # data = requestsVodDataRetrieveWithRetries(ep_graphdata)     
    print(data)
    if data is None or len(data) < 1:
        print("Error: Could not retrieve episode download url, unable to download VOD details, skipping "+item['title'])
        # continue
    
    if not data or not 'data' in data or not 'Program' in data['data'] or not 'episodes' in data['data']['Program'] or len(data['data']['Program']['episodes']) < 1:
        print("Error: Could not retrieve episode download url, VOD did not return any data, skipping "+item['title'])
        # continue
    breakpoint()

    ep_data = data['data']['Program']['episodes'][0] # First and only item
    vod_url_full = ep_data['file']
    return vod_url_full


def get_vod(item):
    outp = requestsVodDataRetrieveWithRetries(sid=item['sid'],pid=item['pid'])
    if not outp['data']:
        return
    # import code
    # code.interact(local=locals())
    if not outp['data']['Program']['episodes']:
        return
    import code
    code.interact(local=locals())
    return outp['data']['Program']['episodes'][0]['file']
    

data = [f for f in download_list if 'Veistu' in f['title']]
items = '\n'.join([f"""
{{
    "title": "{item['title']}",
    "action": "video:{alt_get_vod(item)}",
    "image": "{item['episode_image']}"
}},""" for item in data if 'title' in item])

output_json = f'''
{{
    "icon": "movie",
    "image": "{data[0]["series_image"]}",
    "label": "{data[0]["series_title"]}",
    "data": {{
        "type": "pages",               
        "template": {{            
            "type": "separate",
            "layout": "0,0,2,4",
            "icon": "msx-white-soft:movie",
            "color": "msx-glass"                    
        }},
        "items": [
            { items }
        ]
    }}
}},
'''

print(output_json)