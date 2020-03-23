import allure


@allure.step("这是第一个步骤@")
def step_01():
    print("步骤1:先加入购物车")

@allure.step("这是第二个步骤@")
def step_02():
    print("步骤2:跳转到付款页面")

@allure.feature("这是一个测试allure页面")
class TestAllureDemo():
    '''测试allure使用'''

    @allure.story("放测试用例标题01")
    def test_allure_demo_01(setup_login):
        '''测试用例的描述01--比如  先登录再测试'''
        print("test_allure_demo_01")

    @allure.story("放测试用例标题02")
    def test_allure_demo_02(setup_login):
        '''测试用例的描述02--比如  先登录再测试'''
        print("test_allure_demo_02")