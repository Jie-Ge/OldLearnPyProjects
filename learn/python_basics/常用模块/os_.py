'''
- 跟操作系统有关，主要是文件系统
- 与操作系统有关的操作，主要包含在三个模块里
    - os: 操作系统目录有关
        os.getcwd(): 获取当前的工作目录
        os.chdir(路径): 更改当前的工作目录
        os.listdir([路径]): 获取一个目录中所有子目录和文件列表 【无参数就获取当前目录】
        os.makedirs([路径]): 创建文件夹
        os.getenv('环境变量名'): 获取指定的环境变量名

        os.curdir: 当前目录
        os.pardir: 父亲目录
        os.sep: 当前系统的路径分隔符
            - windows: '\'
            - linux: '/'
        os.linesep: 当前系统的换行符号
            - windows: '\r\n'
            - linux: '\n'
        os.name: 当前系统的名称

    - os.path: 系统路径相关操作
        . : 当前目录
        .. : 父目录
        abspath('路径'): 绝对路径
        basename('路径'): 获取路径中的最后文件
        join(路径1,路径2,...)： 将多个路径拼成一个路径
        split(路径): 将路径切割为文件夹部分和最后文件部分，返回元组
        isdir(路径): 判断是否是目录
        exists(路劲)： 检测文件或目录是否存在

    - shutil: 高级文件操作，目录树的操作，文件复制，删除，移动
        copy(来源路径， 目标路径): 复制文件， 目标路径可以是目录名
        copy2(来源路径， 目标路径): 区别是复制文件时尽量保留元数据(描述数据属性的信息)
        copyfile(src, dst): src, dst 都需是文件名, 如果dst存在或无权限，会抛出异常
        move(来源路径， 目标路径): 移动文件/文件夹， 但必须有操作权限

        归档和压缩：
            - 归档： 把多个文件或者文件夹合并到一个文件当中(感觉就是将某个文件中的内容压缩到另一个文件中)
                make_archive(归档后的文件, 后缀, 需要归档的文件)： 归档
                unpack_archive(需要解包的文件, 解包后的文件)： 解包
            - 压缩： 用算法把多个文件或者文件夹无损或者有损合并到一个文件当中
'''

# 以上方法的参数， 如果不是路径，而是一个单独的文件， 则都表示在当前文件目录下进行的操作


import os

print(os.getcwd())
print(os.listdir())

# 只能创建文件夹
# os.makedirs('try.py')

print('===== 环境变量名 =======\n', os.getenv('PATH'))

print('===== abspath() =======\n', os.path.abspath('.'))

print('===== basename() =======\n', os.path.basename('/home/yangjie'))

p1 = '/home/a'
p2 = 'jie/e'
# 注意： 第二个开始的路径，首字符不能是'/'
print('===== join() =======\n', os.path.join(p1, p2))

# 因为是返回拥有两个元素的元组， 所以可用两个变量接受
b1, b2 = os.path.split('home/jiege/file')
print('===== split() ======\n', os.path.split('/home/jiege/file'))

import shutil

shutil.copy('f.py', 'f1.py')
shutil.copyfile('f.py', 'f2.py')