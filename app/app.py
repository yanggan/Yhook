# coding:utf-8
from flask import Flask,request
app = Flask(__name__)

import commands,os

# 全局变量
PROJECT_PATH = '/Users/yg/Documents/code/Project/leanroom'



# 接受到消息
@app.route('/',methods=['POST','GET'])
def webhook():

    if request.method == "GET":
        return "pelase use POST"

    x = request.form
    pull_code()
    print x
    x = str(x)
    return 'Receive successful %s ' % x

# 拉取gitpull
def pull_code():

    # 执行
    # cd /home/yg/www/leanroom/
    # git reset --hard
    # git pull

    (status, output) = commands.getstatusoutput('cd %s ' % PROJECT_PATH)
    print status, output
    (status, output) = commands.getstatusoutput('git add . ')
    print status, output
    (status, output) = commands.getstatusoutput('git commit -m "added:js"') 
    print status, output



# 重启服务器
def restart_server():

    pass


if __name__ == '__main__':
   
    app.run()

