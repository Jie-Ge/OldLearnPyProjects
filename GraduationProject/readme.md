# 文件说明
- main.py：爬取数据的主文件
- get_url.py：获取需要爬取网页的url
- get_info.py：提取专利信息
- get_proxies_ip.py: 爬取免费的代理ip
- Chaojiying.py: 第三方验证码识别平台提供的API
- verification_code.py: 识别验证码

- data_handle: 将数据处理成能够可视化的数据格式
- visualization：数据可视化（可视化文件在production文件下）

# 文件运行顺序
- 若要使用代理ip，可先执行get_proxies_ip.py爬取免费的代理ip，并修改main.py中的代码
- 若不使用代理ip，直接执行main.py