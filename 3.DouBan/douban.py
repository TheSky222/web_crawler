import requests
import json

url = 'https://movie.douban.com/j/chart/top_list'

params = {
    'type':'24',
    'interval_id':'100:90',
    'action':'',
    'start':'1',#从库中第几部电影去取
    'limit':'20',#一次取出的个数
}

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
response = requests.get(url = url,params = params, headers = headers)
list_data = response.json()
fp = open('./douban.json','w',encoding='utf-8')
json.dump(list_data,fp = fp, ensure_ascii = False)