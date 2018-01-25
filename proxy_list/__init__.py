"""
爬取代理库
"""
import urllib
import sqlite3
import re
import sqlite3
from urllib import request


class Get_proxy(object):
    #初始化页数
    def __init__(self):
        self.Page = 1
        self.flag = True

    def proxy_down(self):
        """
        获取高匿名代理网页信息，并下载源码

        """
        url = "https://www.kuaidaili.com/free/inha/" + str(self.Page) + "/"

        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko"
        }

        #开始构建访问
        rq = request.Request(url, headers = headers)
        op_rq = request.urlopen(rq)
        #测试连接
        html = op_rq.read().decode("utf-8")
        #调用函数用正则将IP从网页中提取出来
        self.proxy_get_re_ip(html)
        #print(requests)

    def proxy_get_re_ip(self, html):
        """
        提取网页中的代理ip
        :param html:
        :return:
        """
        pattern_ip = re.compile('<td\sdata-title="IP">(.*?)</td>',re.S)
        pattern_port = re.compile('<td\sdata-title="PORT">(.*?)</td>',re.S)
        content_ip_list = pattern_ip.findall(html)
        content_port_list = pattern_port.findall(html)



        #原以列表形式写入文件
        #self.proxy_sql_set(content_ip_list,"ip")
        #self.proxy_sql_set(content_port_list,"port")

    def proxy_sql_set(self, list_o, name):
        """
        将获取的ip列表以列表形式，存入数据库中，以待读取
        :param list:
        :return:
        """
        #如果没有则在此目录创建一个数据库，如果已有该数据库，则打开该数据库
        connt = sqlite3.connect("data.db")
        #创建数据库游标
        cursor = connt.cursor()
        #建立表，proxy_list 代理ip爬取表，data_list数据表
        cursor.execute("CREATE TABLE 'proxy_list'([id] integer(4) PRIMARY KEY,  [IP] varchar(20), [PROT] varchar(20))")

        #print("正在将ip写入本地....")
        #with open(name + ".txt","a") as f:
        #    f.write(str(list_o))



if __name__ == "__main__":
    test_rq = Get_proxy()
    #test_rq.proxy_down()
    test_rq.starwork()
