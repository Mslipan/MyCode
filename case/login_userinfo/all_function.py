import requests
import os

class YoYoKeChengAPI():

    def __init__(self,s):
        self.s = s

    def login(self,username="test",password="123456"):
        '''登录
        :arg  s 会话
        '''
        url = os.environ["host"] + "/api/v1/login"
        body = {
            "username": username,
            "password": password
        }
        res = self.s.post(url=url, json=body)
        re =  res.json()
        # 获取token值
        token =re['token']
        # 将token更新到headers
        h = {
            "Authorization": "Token %s" % token
        }
        # 更新到头部
        self.s.headers.update(h)
        return re

    def get_user_info(self):
        '''查询个人信息
        :arg  s 会话
        '''
        url = os.environ["host"] + "/api/v1/userinfo"
        res = self.s.get(url)  # 登录
        return res.json()

    def updata_user_info(self,name="test",sex="M",age=18,mail="2361094@qq.com"):
        '''修改个人信息
        :arg  s 会话
        '''
        url = os.environ["host"] + "/api/v1/userinfo"
        body = {
            "name": name,
            "sex": sex,
            "age": age,
            "mail": mail
        }
        res = self.s.post(url=url,json=body)
        re = res.json()
        return re

if __name__=="__main__":
    s = requests.session()
    yoyo = YoYoKeChengAPI(s) #创建对象，将会话s初始化

    re = yoyo.login(username="test")
    print(re)
    res = yoyo.updata_user_info(name="test")
    print(res)

    re = yoyo.get_user_info()
    print(re)

