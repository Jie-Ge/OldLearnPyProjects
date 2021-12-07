import random
import time
import csv
from GraduationProject import get_url, get_info, verification_code
# import urllib.request
import urllib.parse
from lxml import etree
from urllib import request
from fake_useragent import UserAgent
import requests
from selenium import webdriver

def read_ip_file():
    '''
    读取保存的代理ip文件
    :return: ip列表
    '''
    with open('ip_proxies_valid.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')  # 去掉换行符
            ip_list.append(line)
    return None


def getHtml(url):
    '''
    获取整个网页
    :param url:
    :return:
    '''
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
    }
    global ip
    ip = ''

    try:
        # print('可用ip：', ip_list)
        # print('不可用ip: ', banned_ip)
        if not ip_list:
            print('无可用的代理ip，程序终止')
            exit()
        ip = random.choice(ip_list)

        proxies = {'http': 'http://{0}'.format(ip)}

        global req
        req = requests.get(url, headers=headers, timeout=(4, 7))
        # req = requests.get(url, headers=headers, proxies=proxies, timeout=(4, 7))
        ele = etree.HTML(req.text)

        # print(req.text)

        # 检验是否是验证码页面
        string_list = ele.xpath('//div/table//td/div/a/text()')

        if string_list and string_list[0] == '跳过验证码':
            print('正在处理验证码....')
            # selenium使用代理
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--proxy-server=%s' % ip)
            # chrome_options.add_argument('--headless')
            # chrome_options.add_argument('--disable-gpu')
            vc = verification_code.VerificationCode(url, chrome_options)
            vc.main()

            req = requests.get(url, headers=headers, timeout=(4, 7))
            # req = requests.get(url, headers=headers, proxies=proxies, timeout=(4, 7))
    except Exception as e:
        print(e, '\n连接超时，当前ip不可用，启用新的ip ...')
        ip_list.remove(ip)
        banned_ip.append(ip)
        getHtml(url)
        return req.text
    else:
        print('数据获取成功')
        return req.text


def save_data(data_dict, field_name):
    print('\n保存数据 ************ \n')
    try:
        with open('patent_data2.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=field_name)
            # writer.writeheader()  # 第一次需要先写入表头
            writer.writerow(data_dict)
    except Exception as e:
        print('error, 保存数据时出错：', e)
    return None

def main():
    '''
    主程序
    :return:
    '''
    print('start main ...\n')

    # 获取URL
    dateURL_list = get_url.getDateURL()

    # 页码
    page_num = 0

    date_count = 1
    for url in dateURL_list:
        print('正在获取  {0}  的专利数据'.format(url))

        while page_num <= 990:
            print('第 {0} 页的数据'.format(page_num // 10 + 1))

            # 下一页url
            next_page_url = get_url.getNextPageURL(url, page_num)
            page_num += 10

            data = getHtml(next_page_url)
            # print(data_of_visual)
            time.sleep(random.uniform(3, 5))

            # 专利类型列表 (整页里的全部类型)
            patentClass_list = get_url.getPatentClass(data)
            cla_index = 0

            # 跳转url
            jumpURL_list = get_url.getJumpURL(data)

            if not jumpURL_list:
                print('无法获取jumpURL，当前ip被封, 启用新的ip')
                ip_list.remove(ip)
                banned_ip.append(ip)
                main()

            count = 1
            for jumpURL in jumpURL_list:
                print('正在获取...第 {1}/50 个dateURL, 第 {2}/100 页，第 {0}/10 条数据'.format(count, date_count, page_num // 10))
                count += 1
                # 保存键值，作为保存数据时的head
                key_list = []

                data = getHtml(jumpURL)
                time.sleep(random.uniform(3, 5))
                # print(data_of_visual)

                element = etree.HTML(data)

                # 获取申请号、申请日
                request_num, request_day = get_info.getReqNumAndDay(element)
                req_num_dict = {'申请号': request_num}
                req_day_dict = {'申请日': request_day}
                key_list.extend(list(req_num_dict.keys()))
                key_list.extend(list(req_day_dict.keys()))

                # 获取专利名称
                patent_name = get_info.get_patent_name(element)
                pat_name_dict = {'专利名称': patent_name}
                key_list.extend(list(pat_name_dict.keys()))

                # 专利类型 (依次取出)
                pat_cla_dict = {'专利类型': patentClass_list[cla_index]}
                cla_index += 1
                key_list.extend(list(pat_cla_dict.keys()))

                # 获取网页中的其他数据
                other_dict = get_info.get_other_info(element)
                key_list.extend(list(other_dict.keys()))

                # 将所有数据合并到一起，方便保存
                all_data_dict = {}
                all_data_dict.update(pat_cla_dict)
                all_data_dict.update(req_num_dict)
                all_data_dict.update(req_day_dict)
                all_data_dict.update(pat_name_dict)
                all_data_dict.update(other_dict)

                save_data(all_data_dict, key_list)


if __name__ == '__main__':

    # 我这里爬取的数据并不多，就没加多线程

    start_time = time.clock()

    ip_list = []
    banned_ip = []
    # 115.223.7.110:80
    read_ip_file()
    main()

    end_time = time.clock()

    print('运行结束，程序运行时间：', end_time-start_time)

    # 专利网站（含可视化）https://www.patenthub.cn/statistics/applicant.html?ds=cn&dm=mix&s=score!&q2=&m=none&fc=&q=fa
    # （含专利引用关系）https://www.baiten.cn/results/s/%25E5%258F%2591%25E5%258A%25A8%25E6%259C%25BA/.html?type=s