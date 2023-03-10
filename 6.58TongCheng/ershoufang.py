import requests
from lxml import etree

if __name__ == '__main__':
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    url = 'https://bj.58.com/ershoufang/'
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    li_List = tree.xpath('//section[@class = "list"]/div')
    fp = open('58.txt', 'w', encoding='utf-8')
    for li in li_List:
        title = li.xpath('./a/div[2]//div/h3/text()')[0]
        print(title)
        fp.write(title + '\n')
