import pytest
from case.login_userinfo.all_function import YoYoKeChengAPI

def test_user_info_01(setup_get_yoyo_shili):
    '''获取正确的token传入,再获取用户的信息'''
    yoyo_shili = setup_get_yoyo_shili
    login_res = yoyo_shili.login("test","123456")  #实例调登录方法
    res = yoyo_shili.get_user_info()  #实例调获取用户信息的方法
    assert res['msg'] == "sucess!"
    assert res['code'] == 0

@pytest.mark.parametrize("token",["dbe695eb516bff2f0c31f68d9b0a873aeb8b0fcf@2","ff2f0c31f68d9b0a873aeb8b0fcf"])
def test_user_info_02(setup_get_session,token):
    '''传入错误的token ---'''
    s = setup_get_session  #获取会话session
    h = {
        "Authorization": "Token %s" %token
    }
    s.headers.update(h)
    #创建用例,将s传入
    yoyo_shili = YoYoKeChengAPI(s) #创建实例
    res = yoyo_shili.get_user_info()  #实例调获取用户信息的方法
    assert res['detail'] == "Invalid token."

