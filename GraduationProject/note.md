# 数据的获取
- 按申请日期搜索专利
- 每日的专利申请量都可达到1000条，且专利网站的普通用户仅显示前1000项，
- 计划得到5w条数据，则需要50个日期
- 为了数据的随机性，为了时间的跨度长，采用随机法，随机选取近5年(?)的50天

# xpath
- BeautifulSoup很容易让网站出现验证信息，xpath好些
- 使用
    - 可以在浏览器控制台输入：$x('xpath表达式')
        - 可以实时看见返回值
    - 表达式：
        - '//div[@属性名="string"]/标签[1]//标签/text()'
            - [1] ：匹配第一个
            - // 与 / 的区别
                - // 只要是后代标签，都匹配到
                - / 只匹配子标签(儿子)
        
        - //tr[contains(text(), "摘要")]//following-sibling::text()
            - 文本内容包含"摘要"的tr标签之后的 同级(兄弟)的文本内容
        - //tr[contains(text(), "摘要")]//following-sibling::td[1]/text()
            - 文本内容包含"摘要"的tr标签之后的 同级的第一个td标签(兄弟标签)下 的文本内容
        - preceding：之前的
        - . : 当前节点
        - .. : 当前节点的父节点
        - tr[last()] : 定位到的最后一个tr标签
        - tr[position()<3] : 选取前面两个tr标签
        - * ：所有
        - | ：或
        
# 代理ip
- 此网站 http://icanhazip.com/ 返回ip地址，可用于检验代理ip是否设置成功
- 此网站 http://httpbin.org/get 返回请求头部信息

# 线程
- t1 = threading.Thread(target=func_name1, args=('param',))
- t2 = threading.Thread(target=func_name2, args=('param',))
- t1.start()
- t2.start()
- t1.join()
- t2.join()
    - 函数名后不能加括号，传参要用args参数；否则线程无效，会挨个执行，不会并发
    - join()要最后添加，若在t2启动前加t1.join(), 会等到t1执行完后才执行t2
    