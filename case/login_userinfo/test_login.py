import pytest

def test_login_01(setup_get_yoyo_shili):
    '''传入正确的用户名和密码'''
    yoyo_shili = setup_get_yoyo_shili  #获取实例
    res = yoyo_shili.login("test","123456") #传入正确的用户名和参数
    assert res['code'] == 0
    assert res['msg'] == 'login success!'

@pytest.mark.parametrize("username_input",["","test23","te st"])
def test_login_02(setup_get_yoyo_shili,username_input):
    '''传入不正确的用户名'''
    yoyo_shili = setup_get_yoyo_shili  #获取实例
    res = yoyo_shili.login(username_input,"123456") #不正确的用户名
    assert res['code'] == 3003
    assert res['msg'] == '账号或密码不正确'

@pytest.mark.parametrize("password_input",["","1234567890","123 456"," 123456","123456 "])
def test_login_03(setup_get_yoyo_shili,password_input):
    '''传入不正确的密码'''
    yoyo_shili = setup_get_yoyo_shili  #获取实例
    res = yoyo_shili.login("test",password_input) #传入不正确的密码
    assert res['code'] == 3003
    assert res['msg'] == '账号或密码不正确'
