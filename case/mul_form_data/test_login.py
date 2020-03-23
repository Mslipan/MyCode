import allure

@allure.feature("登录的接口")
class TestLogin():

    @allure.story("传入正确的用户名和密码")
    def test_login_01(self,get_mul_form_data_class_obj):
        '''用户名为admin,密码为yoyo12345'''
        obj = get_mul_form_data_class_obj
        res = obj.login()
        assert "主页面 | 后台页面" in res.text

    @allure.story("传入错误的用户名,正确的密码")
    def test_login_02(self,get_mul_form_data_class_obj):
        '''错误的用户名为root'''
        obj = get_mul_form_data_class_obj
        res = obj.login("root")
        assert "请输入正确的用户名和密码" in res.text

    @allure.story("传入正确的用户名,错误的密码")
    @allure.issue("http://192.168.0.215:8088/zentao/bug-create-1-0-moduleID=0.html")#该用例发现的bug,提出的bug对应的地址
    @allure.testcase("http://192.168.0.215:8088/zentao/testcase-view-8-1.html")#该用例对应的地址
    def test_login_03(self,get_mul_form_data_class_obj):
        '''错误的密码为yoyy123456'''
        obj = get_mul_form_data_class_obj
        res = obj.login("admin","yoyy123456")
        assert "请输入正确的用户名和密码" in res.text
