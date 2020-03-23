import yaml
import os

def readYaml(yamlPath):
    '''读取yaml里面的数据
    :arg  yamlPath 文件的绝对路径
    '''

    #判断路径是否存在
    if not os.path.isfile(yamlPath):
        raise FileNotFoundError("文件路径不存在，请检查路径是否正确 %s" %yamlPath)

    #打开文件
    f = open(yamlPath,"r",encoding='utf-8')

    #读取文件
    cfg = f.read()

    #将内容转换成dict
    yaml_data = yaml.load(cfg)

    return yaml_data

if __name__ == '__main__':
    # data = readYaml("G:\Python code\\2020\yoyo_request_0314\\requests_parametrize\\test_data.yml")
    # print(data['update_userinfo'][0])
    data = readYaml("G:\Python code\\2020\yoyo_request_0314\\requests_parametrize\\test_data.yml")["update_userinfo"]
    print(data)

    #获取当前文件所在的路径
    p = os.path.realpath(__file__)

    #获取当前文件所在的文件夹
    pa = os.path.dirname(p)

    #路径拼接
    pat = os.path.join(pa,"test_data.yml")
    print(pat)

