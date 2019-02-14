

# ! -*- coding:utf-8 -*-

# 2019.1.23  增加index手数的部分
import time
import re
from math import floor

import pymysql
import requests
from lxml import etree
from selenium import webdriver
# 还是要用PhantomJS
import datetime
import string

total_Cash = 30000 # 初始资金3万美元
index_Cash = 0.3*total_Cash
stock_Cash = 0.6*total_Cash
index_Future_N = floor(index_Cash/6380) #都是美元，
index_cost = 2650
stock_cost = 16.3

# 2019.1.22 阿根廷电信——————标普500指数模型测试(重新关注，有了接口)



def get_index_PL():
    try :

        driver = webdriver.Chrome()
        url = 'http://quote.hexun.com/wpfutures/index_wfutures.aspx?code=692'
        # driver = webdriver.PhantomJS(service_args=SERVICE_ARGS)
        driver.set_window_size(38, 12)  # 设置窗口大小
        driver.get(url)
        html = driver.page_source
        selector = etree.HTML(html)
        items = selector.xpath('//*[@id="wpFutureListPage"]/table/tbody/tr[7]/td[2]/text()')
        items_list =[]
        for item in items:
            items_list.append(float(item))
            indexF_PL = (index_cost-items_list[0])* 50 *index_Future_N # index点差，乘上每点50美元，再乘上手数，就是美元盈亏
            indexF_PL_2 = round(indexF_PL,2)
            big_list.append(str(indexF_PL_2))
            driver.quit()
    except ValueError as e:
        pass



# 2016.1.23 阿根廷电信
def get_stocks_PL():
    url = 'https://www.laohu8.com/hq/s/TEO'
    headers = {'Useragent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0'}
    response = requests.get(url, headers=headers)
    content = response.text
    patt = re.compile('<td class="price">(.*?)</td>', re.S)
    items = re.findall(patt, content)
    stock_PL = ((float(items[0])-stock_cost) /stock_cost) * stock_Cash  # 股价股价涨跌幅，乘以stock部位的资金
    stock_PL_2 = round(stock_PL,2)
    big_list.append(stock_PL_2)




def profilo_PL():
    try:
        A = big_list[0]
        B = big_list[1]
        profilo_PL =  float(B) + float(A)
        profilo_PL_2 = round(profilo_PL,2)
        big_list.append(profilo_PL_2)
        total_profit_R = profilo_PL_2/total_Cash
        total_profit_R_2 = round(total_profit_R,3) * 100  # 这个最简单

        big_list.append(total_profit_R_2)

    except IndexError as e:
        print(e)







def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='web_monitor',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # 这里是判断big_list的长度，不是content字符的长度
    if len(big_list) == 4:
        cursor.executemany('insert into OneStock_ES500_PL (index_PL,stock_PL,profilo_PL,profilo_PL_R) values (%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    else:
        print('出列啦')

#
#
if __name__ == '__main__':
    i = 0
    while True:

        i += 1
        print(i)
        big_list = []
        get_index_PL()
        get_stocks_PL()
        profilo_PL()
        l_tuple = tuple(big_list)
        content = []
        content.append(l_tuple)
        insertDB(content)
        time.sleep(6)






# create table OneStock_ES500_PL(
# id int not null primary key auto_increment,
# index_PL varchar(10),
# stock_PL varchar(10),
# profilo_PL varchar(10),
# profilo_PL_R varchar(10)
# ) engine=InnoDB  charset=utf8;

# drop table OneStock_ES500_PL;
