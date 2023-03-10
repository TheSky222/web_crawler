import requests
import json

# UA伪装
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

post_url = 'https://fanyi.baidu.com/sug'

# post请求参数处理
word = input('enter a word')
data = {
    'kw':word
}

# 请求发送
response = requests.post(url = post_url, data = data, headers = headers)

# 返回对象obj（确认响应数据是json格式，才能使用json()）
dic_obj = response.json()
print(dic_obj)

# 持久化存储
fileName = word + '.json'
fp = open(fileName,'w',encoding = 'utf-8')
json.dump(dic_obj, fp = fp, ensure_ascii = False)
print('successfully')