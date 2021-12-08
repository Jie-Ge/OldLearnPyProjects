

def getReqNumAndDay(element):
    '''
    获取申请号、申请日
    :return:
    '''
    try:
        expression = "//i[contains(text(),'申请号')]//text()"
        value = element.xpath(expression)
        # print("申请号：", value)
        value = ';'.join(value)  # 将列表用分号连接成字符串
        request_num_string, request_day_dict = value.split(' ')
        request_num_head, request_num = request_num_string.split('：')
        request_day_head, request_day = request_day_dict.split('：')

        return request_num, request_day
    except Exception as e:
        print('error, 可能不是我们想要的页面: ', e)
        print(element)
        exit()


def get_patent_name(element):
    '''
    获取专利名称
    :return:
    '''
    text = element.xpath('//h1/text()')[0]
    # print(text)
    patent_name = text.replace('\n', '').replace(' ', '').replace('\t', '').replace('\r', '')
    # print(soup.h1.string)  # 为啥不行
    # print(patent_name)

    return patent_name


def get_other_info(element):
    name_list = ['法律状态', '公开号', '公开日', '优先权', '国际申请', '国际公布', '进入国家日期', '专利代理机构', '代理人',
                 '地址', '摘要', '申请人', '发明(设计)人', '主分类号', '分类号', '同族专利', '引用文献', '被引用文献']
    info_dict = {}
    for name in name_list:

        value = ''

        if name == '法律状态':
            expression = "//span[contains(text(), '{0}')]/../../following-sibling::table//tr[last()-1]//text()".format(name)
            info_list = element.xpath(expression)
            try:
                value = info_list[-2]
                value = value.strip()  # 去掉首尾的空格和换行符
            except:
                print('无法律状态')

        elif name == '专利代理机构':

            # td[contains(text(),"string"): 定位文本内容包含"string"的td标签
            # following-sibling::td[1]：兄弟节点中的第 1 个 td标签
            # 注意引号,{0}还需要加上引号
            expression = "//td[contains(text(),'{0}')]/following-sibling::td[1]//a//text()".format(name)
            info_list = element.xpath(expression)
            value = ';'.join(info_list)  # 将列表用分号连接成字符串
            value = value.strip()  # 去掉首尾的空格和换行符

        # 这一项会出现多个同级同样a标签，使用position()>0来全部获取
        elif name == '代理人':
            expression = "//td[contains(text(),'{0}')]/following-sibling::td[1]//a[position()>0]//text()".format(name)
            info_list = element.xpath(expression)
            value = ';'.join(info_list)
            value = value.strip()

        # 表达式不一样
        elif name == '申请人' or name == '发明(设计)人' or name == '主分类号' or name == '分类号':
            expression = "//b[contains(text(), '{0}')]//following-sibling::a/text()".format(name)
            info_list = element.xpath(expression)
            value = ';'.join(info_list)
            value = value.strip()

        elif name == '优先权':
            expression = "//td[contains(text(),'{0}')]/following-sibling::td[1]/text()".format(name)
            info_list = element.xpath(expression)
            try:
                value = info_list[0]
                value = value.strip()
            except:
                print('无优先权')

        # 表达式不一样
        elif name == '同族专利' or name == '引用文献' or name == '被引用文献':
            expression = "//td[contains(text(),'{0}')]/following-sibling::td[1]//td//a/text()".format(name)
            info_list = element.xpath(expression)
            value = ';'.join(info_list)
            value = value.strip()

        elif name == '地址' or name == '摘要':
            expression = "//b[contains(text(), '{0}')]//following-sibling::text()".format(name)
            info_list = element.xpath(expression)
            value = ';'.join(info_list)
            value = value.strip()

        else:
            expression = "//td[contains(text(),'{0}')]/following-sibling::td[1]/text()".format(name)
            info_list = element.xpath(expression)
            value = ';'.join(info_list)
            value = value.strip()

        info_dict[name] = value

    return info_dict
