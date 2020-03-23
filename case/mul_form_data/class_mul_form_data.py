import re
from requests_toolbelt import MultipartEncoder
import lxml.etree
import os
import allure

class MulFormData():

    def __init__(self,s):
        self.s = s

    @allure.step("登录xadmin")
    def login(self,username="admin",password="yoyo123456"):
        '''登录'''
        url = os.environ['host'] + "/xadmin/"
        res = self.s.get(url=url)
        # 正则
        token = re.findall("name='csrfmiddlewaretoken' value='(.+?)'",res.text)
        # 传入参数
        body = {
            "csrfmiddlewaretoken": token,
            "username": username,
            "password": password,
            "next": "/xadmin/",
            "this_is_the_login_form": 1
        }
        resu = self.s.post(url=url, data=body)
        return resu

    @allure.step("增加老师")
    def add_teacher(self,teacher_name="teach123456",sex="M",mail="32412421@qq.com",tel="3214124"):
        '''增加老师'''
        url = os.environ['host'] + "/xadmin/hello/teacherman/add/"
        res = self.s.get(url=url)
        # 正则
        csrfmiddlewaretoken = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", res.text)
        # 构建请求参数
        body = MultipartEncoder(
            fields=[
                ("csrfmiddlewaretoken", csrfmiddlewaretoken[0]),
                ("csrfmiddlewaretoken", csrfmiddlewaretoken[0]),
                ("mail", mail),
                ("sex", sex),
                ("teacher_name", teacher_name),
                ("tel", tel),
                ("_save", "")
            ]
        )
        resu = self.s.post(url=url, data=body, headers={"Content-Type": body.content_type})
        return resu

    @allure.step("上传图片或文件")
    def upload_image(self,title="image123",image="1.jpg"):
        '''上传图片或文件'''
        url = os.environ['host'] + "/xadmin/hello/fileimage/add/"
        result = self.s.get(url=url)
        # 正则,获取csrfmiddlewaretoken
        csrfmiddlewaretoken = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", result.text)
        body = MultipartEncoder(
                    fields=[
                        ("csrfmiddlewaretoken", csrfmiddlewaretoken[0]),
                        ("csrfmiddlewaretoken", csrfmiddlewaretoken[0]),
                        ("title", title),
                        ("image",(image , open(image,"rb"),"image/jpeg")),
                        #("fiels", ("1.jpg", open("1.jpg", "rb"), "image/jpeg")),
                        ("_save", "")
            ]
        )
        resu = self.s.post(url, data=body, headers={"Content-Type": body.content_type})
        return resu

    @allure.step("解析html页面,根据路径获取页面上的值")
    def get_first_data(self,result,xpath="//*[@id='changelist-form']/div/table/tbody/tr/td[2]/a"):
        '''获取添加的数据'''
        # 对访问后的页面进行解析
        html = lxml.etree.HTML(result)
        # 获取最上面的节点
        nodes = html.xpath(xpath)
        #返回最前面的数据文本
        return nodes[0].text

