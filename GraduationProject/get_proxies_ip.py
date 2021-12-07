import requests
from fake_useragent import UserAgent
from lxml import etree
import time
from multiprocessing import Pool
import multiprocessing
import sys
import random


def get_single(url):  # 爬出单页上的所有代理ip
    print('请求中。。。。')
    r = requests.get(url, headers=head)
    print('请求完成')
    time.sleep(random.uniform(3, 5))  # 产生3到5之间的随机浮点数
    if r.status_code == 503:
        print('由于爬取次数过多,你的Ip已经被封')
        sys.exit(0)
    content = etree.HTML(r.text)
    ip = content.xpath('//table[@id="ip_list"]/tr/td[2]/text()')
    port = content.xpath('//table[@id="ip_list"]/tr/td[3]/text()')
    for i in range(0, len(ip)):
        ip_list.append(ip[i] + ":" + port[i])
    return 'finish'


def input_urls():  # 防止ip被封每三秒访问一页
    for i in range(1, 21):
        get_single(url + str(i))
        print('爬取第' + str(i) + '页\r', end="")
        time.sleep(3)


def verify_ips(ip, ip_valid_list):  # 验证代理ip
    global count
    print('验证第 {0}/{1} 个ip, 目前可用ip {2} 个'.format(count, len(ip_list), len(ip_valid_list)))
    count += 1
    poxie = "http://" + ip
    proxies = {
        'http': poxie,
        'https': poxie
    }
    try:
        url1 = 'http://www.soopat.com/Patent/201680086232'
        url2 = 'https://www.baidu.com'
        requests.get(url1, headers=head, proxies=proxies, timeout=3)
        ip_valid_list.append(ip)
        time.sleep(1)

    except Exception:
        print('此ip不可用......')


count = 1
ip_list = []
url = "https://www.xicidaili.com/nn/"
ua = UserAgent()
head = {
    'User-Agent': ua.random}

if __name__ == "__main__":
    """
    程序结束后会在当前文件夹生成一个ip_proxies_valid.txt文件，
    防止ip被封,控制爬取频率
    """
    mlist = multiprocessing.Manager()
    ip_valid_list = mlist.list()
    input_urls()
    print("总共爬取到" + str(len(ip_list)) + "个ip,接下来准备验证ip有效性")
    print("开始验证!")
    p = Pool(15)
    for ip in ip_list:
        p.apply_async(verify_ips, (ip, ip_valid_list))  # 多进程验证
    p.close()
    p.join()
    f = open('ip_proxies_valid.txt', 'a')
    for ip in ip_valid_list:  # 写入txt文件
        f.write(ip)
        if ip != ip_valid_list[-1]:
            f.write('\n')
    f.close()
    print(ip_valid_list)
    print("完成")
