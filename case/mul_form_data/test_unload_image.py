import allure

@allure.feature("上传图片和文件的接口")
class TestUploadImage():

    @allure.story("只上传图片")
    def test_unload_image(self,setup_login):
        '''先登录,再正常上传图片'''
        obj = setup_login
        res = obj.upload_image("image127","1.jpg")
        #判断上传后的结果
        image_name = obj.get_first_data(res.text,"//form[@id='changelist-form']/div/table/tbody/tr/td[2]/a")
        assert image_name == "image127"


