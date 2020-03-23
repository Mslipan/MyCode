import pytest
import requests
from case.mul_form_data.class_mul_form_data import MulFormData
import os



###想用命令行中带host地址,之后执行 --- host变不影响执行
#将其加入到pytest命令行
def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost",
        action="store",
        default="http://49.235.92.12:8020",
        help="run project host"
    )

#从命令行获取到cmdhost,将其变成环境变量,利用autouse自动生效
@pytest.fixture(scope="session",autouse=True)
def host(request):
    os.environ['host'] = request.config.getoption("--cmdhost")

@pytest.fixture()
def get_session(host):
    s = requests.session()
    yield s  #yiled后为返回值,yiled前为前置,yiled后为后置
    s.close()

'''
yiled  前置出现问题,测试用例中的代码不执行,yiled后的代码也不执行  ---终结函数 addfinalizer
       若只是测试用例中的代码出现问题,yiled后的代码仍执行
'''

@pytest.fixture()
def get_mul_form_data_class_obj(get_session):
    s = get_session
    obj = MulFormData(s)
    yield obj

@pytest.fixture()
def setup_login(get_mul_form_data_class_obj):
    obj = get_mul_form_data_class_obj
    obj.login("admin","yoyo123456")
    yield obj





