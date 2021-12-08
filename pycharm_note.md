# windows下进入conda环境
- pc左下角搜索‘Anaconda Prompt’
- conda env list: 有哪些环境
- conda activate env_name：进入某个环境

# pip时报错
- python -m pip install --upgrade pip 报 ReadTimeoutError
    - 解决方法：pip --default-timeout=1000 install --upgrade pip
- 安装镜像文件
    - 下载镜像文件（如：下载文件 xgboost-1.0.2-cp36-cp36m-win_amd64.whl 到D:\learnSoftware中）
    - 安装：pip install D:\learnSoftware\xgboost-1.0.2-cp36-cp36m-win_amd64.whl 
- 安装其他文件出错
    - 参考【https://blog.csdn.net/qq_32863549/article/details/105238497】
    - 参考【https://blog.csdn.net/qq_27283619/article/details/100110947】

    
# jupyter notebook
- 创建文件时可选择在哪个conda环境下创建，那么需要先将这个环境添加到可选环境中
    - 方法1：
        - 在相应conda环境下输入：
            - conda install ipykernel
            - python -m ipykernel install --user --name your_env --display-name "Python [conda env:your_env]"
        - 重启jupyter notebook
    - 方法2：
        - 在任意conda环境下输入：
            - conda install nb_conda_kernels
            - 参考网址：https://blog.csdn.net/sean2100/article/details/83744679

- 设置jupyter启动后的默认打开文件目录
    - 1、找到配置文件路径 
        - C:\Users\HUAWEI>jupyter notebook --generate-config  # 查看配置文件路径的命令
    - 2、打开这个文件
    - 3、找到py文件中的 # c.NotebookApp.notebook_dir='' 这一行
    - 4、解开注释，写入路径 c.NotebookApp.notebook_dir = 'D:/python3_anaconda_jupyter_notebook'
    - 5、重启 jupyter notebook
    
# git
- `Git` -> `Manage Remotes`
    - 'Name' : 远端仓库所起的（本地）名字，一般都是叫origin，其实你也可以要Ceres 或者Earth
    - 'URL' : 远端仓库的真实地址
    
- `Git` -> `Commit`   提交到本地仓库
- `Git` -> `Push`     推给远程仓库