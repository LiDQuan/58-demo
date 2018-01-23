import urllib
import random
import proxy_list
from urllib import request


class city_five(object):
    def __init__(self):
        #初始化Page页面
        self.Page = 1

    def downPage(self):
        """
            下载页面源代码
        """
        #设定url
        url = "http://nn.58.com/tech/pn" + str(self.Page) + "/"

        #设定User-Agent列表，之后用随即读取
        headers_list = [
            {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1"},
            {"User-Agent":"Mozilla/5.0 (Macintosh;Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
            {"User_Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"},
            {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko"},
            {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"}
        ]

        #使用随机数，随即选取headers
        headers = random.choice(headers_list)

        #测试随机headers
        print(headers)


if __name__ == "__main__":
    new_city = city_five()
    new_city.downPage()
    #测试代理库类
    #new_proxy = proxy_list.Get_proxy()

