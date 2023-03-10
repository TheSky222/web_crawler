import requests
if __name__ == '__main__':
    # 图片地址
    url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fq_70%2Cc_zoom%2Cw_640%2Fimages%2F20190126%2F159d72185ac643e0bde72665182286c6.jpg&refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1632580840&t=d7be748430d26920b0cf5a7bed1b3a71'
    # content返回二进制形式的图片数据
    # text:字符串 content:二进制 json():对象
    image_data = requests.get(url=url).content
    with open('./image.jpg','wb') as fp:
        fp.write(image_data)
