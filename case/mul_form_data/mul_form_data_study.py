import requests
import re
from requests_toolbelt import MultipartEncoder
from lxml import etree

def login(s):
    #进入登录页面
    url = " http://49.235.92.12:8020/xadmin/"
    res = s.get(url=url)
    #正则
    token = re.findall("name='csrfmiddlewaretoken' value='(.+?)'",res.text)
    #传入参数
    body = {
        "csrfmiddlewaretoken":token,
        "username":"admin",
        "password":"yoyo123456",
        "next":"/xadmin/",
        "this_is_the_login_form":1
    }
    resu = s.post(url=url,data=body)
    return resu

def add_teacher(s):
    url2 = "http://49.235.92.12:8020/xadmin/hello/teacherman/add/"
    res = s.get(url=url2)
    #正则
    csrfmiddlewaretoken = re.findall("name='csrfmiddlewaretoken' value='(.+?)'",res.text)
    #构建请求参数
    body = MultipartEncoder(
        fields= [
            ("csrfmiddlewaretoken",csrfmiddlewaretoken[0]),
            ("csrfmiddlewaretoken",csrfmiddlewaretoken[0]),
            ( "mail","32412421@qq.com"),
            ("sex","M"),
            ("teacher_name","teach456"),
            ("tel","3214124"),
            ("_save","")
        ]
    )
    res = s.post(url=url2,data=body,headers={"Content-Type":body.content_type})
    return res

def get_first_data(result):
    #对增加teacher后的页面进行解析
    html = etree.HTML(result)
    #获取最上面的节点
    nodes = html.xpath("//*[@id='changelist-form']/div/table/tbody/tr/td[2]/a")
    return nodes[0].text

def upload_image(s):
    url = "http://49.235.92.12:8020/xadmin/hello/fileimage/add/"
    result = s.get(url=url)
    #正则,获取csrfmiddlewaretoken
    csrfmiddlewaretoken = re.findall("name='csrfmiddlewaretoken' value='(.+?)'",result.text)
    body = MultipartEncoder(
        fields=[
            ("csrfmiddlewaretoken",csrfmiddlewaretoken[0]),
            ("csrfmiddlewaretoken",csrfmiddlewaretoken[0]),
            ("title","image123"),
            #("image",("1.jpg",open("1.jpg","rb"),"image/jpeg")),
            ("fiels",("1.jpg",open("1.jpg","rb"),"image/jpeg")),
            ("_save","")
        ]
    )
    resu = s.post(url,data=body,headers={"Content-Type":body.content_type})
    return resu

if __name__ == "__main__":
    s = requests.session()
    res = login(s)
    resu = add_teacher(s)
    text = get_first_data(resu.text)
    print(text)
    result = upload_image(s)
    text = get_first_data(result.text)
    print(text)




