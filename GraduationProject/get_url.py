import re
from bs4 import BeautifulSoup
import time
import random

# https://www.uyanip.com/
host = "http://www2.soopat.com"


def getDateURL():
    '''
    随机选取近5年的50天,根据日期得到需要搜索的url
    :return: URL列表
    '''

    start_tuple = (2015, 1, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（1976-01-01 00：00：00）
    end_tuple = (2019, 12, 31, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（1990-12-31 23：59：59）

    start_timestamp = time.mktime(start_tuple)  # 生成开始时间戳
    end_timestamp = time.mktime(end_tuple)  # 生成结束时间戳

    # 随机生成50个日期字符串
    date_list = []
    url_list = []
    while len(date_list) < 50:
        rad = random.randint(start_timestamp, end_timestamp)  # 在开始和结束时间戳中随机取出一个
        date_tuple = time.localtime(rad)  # 将时间戳生成时间元组
        date = time.strftime("%Y-%m-%d", date_tuple)  # 将时间元组转成格式化字符串
        if date not in date_list:
            date_list.append(date)
            url = host + '/Home/Result?SearchWord=' + date + '&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
            url_list.append(url)

    return url_list


# =============== 专利类型 ==============
def getPatentClass(data):
    '''

    :param data: 整个网页
    :return: 专利类型列表
    '''

    pat = re.compile(r'[[]([\u4e00-\u9fa5]+)[]]')  # 正则匹配

    patent_class = pat.findall(data)

    if '关闭' in patent_class:
        patent_class.remove('关闭')  # 若多了一个‘关闭’，删除

    return patent_class


# ==============得到跳转(具体信息)网址===================
def getJumpURL(data):
    '''

    :param data: 整个网页
    :return: 返回跳转到具体信息网页的URL
    '''
    soup = BeautifulSoup(data, 'html.parser')

    # 查找href中含有"/Patent/"的标签
    # print(soup.find_all(href=re.compile("/Patent/")))

    # 选择类名为PatentTypeBlock的标签下的a标签
    soupA = soup.select(".PatentTypeBlock > a")

    jump_url_list = []

    for item in soupA:
        # 拼接主机与a标签里的链接
        jump_url_list.append(host + item['href'])

    return jump_url_list


# ============= 得到下一页网址 =====================

def getNextPageURL(url, page_num):

    next_page_url = url + '&PatentIndex=' + str(page_num)

    return next_page_url
