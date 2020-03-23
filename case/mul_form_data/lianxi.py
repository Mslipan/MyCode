import os

#将host变成环境变量,之后传入host

#设置成环境变量
os.environ['host'] = "http://192.168.0.215/construct"
#从环境变量中取出host
host = os.environ['host']
print(host)
