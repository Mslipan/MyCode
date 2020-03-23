import allure

@allure.feature("增加老师的接口")
class TestAddTeacher():

    @allure.story("填写所有正常的参数")
    def test_add_teacher_01(self,setup_login):
        '''先登录,再正常增加老师'''
        obj = setup_login
        # resu = obj.login("admin","yoyo123456")
        res = obj.add_teacher("teach","M","23@qq.com","123456")
        #看最新的一条数据是不是在最上面
        text = obj.get_first_data(res.text,"//*[@id='changelist-form']/div/table/tbody/tr/td[2]/a")
        assert "teach" == text
