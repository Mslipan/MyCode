from case.login_userinfo.all_function import YoYoKeChengAPI
import pytest
import requests
import os


#命令行 -- 输入地址
def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost",
        action="store",
        default="http://49.235.92.12:9000",
        help="run project host"
    )

#命令行获取到host,将其变成环境变量,自动生效
@pytest.fixture(scope="session",autouse=True)
def get_host(request):
    os.environ['host']=request.config.getoption("--cmdhost")

@pytest.fixture()
def setup_get_session(get_host):
    #获取会话
    s = requests.session()
    return s

@pytest.fixture()
def setup_get_yoyo_shili(setup_get_session):
    #获取会话
    s = setup_get_session
    #创建实例
    yoyo = YoYoKeChengAPI(s)
    return yoyo




