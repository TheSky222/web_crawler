import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url,headers=headers).content

    # 实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
    soup = BeautifulSoup(page_text, 'lxml')

    # 解析章节标题和详情页的url
    li_list = soup.select('.book-mulu > ul > li')

    fp = open('./sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.text
        # print(li.a)
        # print(title)
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        # 对详情页发起请求，解析出章节内容
        detail_page_text = requests.get(url=detail_url,headers=headers).content
        # 解析出详情页中相关内容
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div', class_ = 'chapter_content')
        # print(div_tag)
        # 解析到的章节内容
        content = div_tag.text
        fp.write(title+':'+content+'\n')
        print(title,'successfully')
