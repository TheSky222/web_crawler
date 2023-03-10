# web_crawler
自学爬虫笔记

## 1.[bs4 text与content的区别](https://blog.csdn.net/qq_42804678/article/details/91345725)

requests对象的get和post方法都会返回一个Response对象，这个对象里面存的是服务器返回的所有信息，包括响应头，响应状态码等。其中返回的网页部分会存在.content和.text两个对象中。

两者区别在于，content中间存的是字节码，而text中存的是Beautifulsoup根据猜测的编码方式将content内容编码成字符串。

直接输出content，会发现前面存在b'这样的标志，这是字节字符串的标志，而text是，没有前面的b,对于纯ascii码，这两个可以说一模一样，对于其他的文字，需要正确编码才能正常显示。大部分情况建议使用.text，因为显示的是汉字，但有时会显示乱码，这时需要用.content.decode('utf-8')，中文常用utf-8和GBK，GB2312等。这样可以手工选择文字编码方式。

所以简而言之，.text是现成的字符串，.content还要编码，但是.text不是所有时候显示都正常，这是就需要用.content进行手动编码。

## 2. [bs4 string与text的区别](https://www.cnblogs.com/kaibindirver/p/11374669.html)

If the `html` is like this:

1. 

   1、<td>some text</td>

2. 

   2、<td></td>

3. 

   3 、<td><p>more text</p></td>

4. 

   4、<td>even <p>more text</p></td>

5. 

   

`.string` on the four `td` will return,

1. 

   1、some text

2. 

   2、None

3. 

   3、more text

4. 

   4、None

`.text` will give result like this

1. 

   1、some text

2. 

   

3. 

   2、more text

4. 

   3、even more text

通过以上的举例，可以很清楚的发现，.find和.string之间的差异：

第一行，在指定标签td，没有子标签，且有文本时，两者的返回结果一致，都是文本

第二行，在指定标签td，没有子标签，且没有文本时，.string返回None，.text返回为空

第三行，在指定标签td，只有一个子标签时，且文本只出现在子标签之间时，两者返回结果一致，都返回子标签内的文本

第四行，最关键的区别，在指定标签td，有子标签，并且父标签td和子标签p各自包含一段文本时，两者的返回结果，存在很大的差异

.string返回为空，因为文本数>=2，string不知道获取哪一个

.text返回的是，两段文本的拼接。

## 3.[session和requests的区别](https://blog.csdn.net/sl01224318/article/details/119712543)

区别：

requests是做一次请求的，当一次请求结束之后，requests请求的内容就会被释放，类似于“做一次性买卖”。

session是做一次请求后，请求不会被立即释放，可以请求跨越多个页面，类似于出去旅游的买的套票，不进可以去A景区，还可以去其他B景区、C景区等。

优缺点：

request占用资源比较少，但是缺乏持续性，比如每个网站需要先登陆再进行其他操作，这时候就不能用request。

session资源的消耗会大点，安全性相对来说也会稍微低点,但可以持续进行会话，session对象能够帮我们跨请求保持某些参数，也会在同一个session实例发出的所有请求之间保持cookies

>>>>>>> 9f97396... init
