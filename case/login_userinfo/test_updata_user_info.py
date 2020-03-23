import pytest

@pytest.fixture()
def setup_updata_user_info(setup_get_yoyo_shili):
    yoyo_shili = setup_get_yoyo_shili
    login_res = yoyo_shili.login("test", "123456")
    return yoyo_shili


@pytest.mark.parametrize("sex_input",["F","M"])
def test_updata_user_info(setup_updata_user_info,sex_input):
    '''修改当前用户的信息,且数据项填写正确,修改成功'''
    yoyo_shili = setup_updata_user_info

    user_info = {
        "name": "test",
        "sex": sex_input,
        "age": 20,
        "mail": "2361094@qq.com"
    }
    res = yoyo_shili.updata_user_info(**user_info)
    assert res['message'] == "update some data!"
    assert res['code'] == 0

@pytest.mark.parametrize("sex_input",["X"])
def test_updata_user_info_02(setup_updata_user_info,sex_input):
    '''修改当前用户的信息,sex数据项填写不正确'''
    yoyo_shili = setup_updata_user_info
    # user_info = {
    #     "name": "test",
    #     "sex":sex_input,
    #     "age": 20,
    #     "mail": "23610@qq.com"
    # }
    res = yoyo_shili.updata_user_info(sex=sex_input)
    assert res['message'] == "参数类型错误"
    assert res['code'] == 3333

@pytest.mark.parametrize("age_input",[1.8])
def test_updata_user_info_03(setup_updata_user_info,age_input):
    '''修改当前用户的信息,sex数据项填写不正确'''
    yoyo_shili = setup_updata_user_info
    res = yoyo_shili.updata_user_info(age=age_input)
    assert res['message'] == "参数类型错误"
    assert res['code'] == 3333


@pytest.mark.appApi
@pytest.mark.parametrize("mail_input", ["2361094", "@qq.com", "qq.@com"])
def test_updata_user_info_04(setup_updata_user_info,mail_input):
    '''修改当前用户的信息,sex数据项填写不正确'''
    yoyo_shili = setup_updata_user_info
    res = yoyo_shili.updata_user_info(mail=mail_input)
    assert res['message'] == "参数类型错误"
    assert res['code'] == 3333
