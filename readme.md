# 环境准备

- python 3.7.2

- 安装 requests.txt里的模块
>pip install -r requests.txt


# 项目描述

1.项目使用框架为pytest+allure
2.使用yml文件来管理测试数据
3.用类来管理测试步骤和测试用例


# 用例设计

-接口用例与功能用例设计思路一致
-等价法 边界值法....


# 报告生成

-报告使用allure
-report目录下的report_raw转换为allure报告

# 执行代码

>pytest --allure = ./report/report_raw
>allure serve  ./report/report_raw