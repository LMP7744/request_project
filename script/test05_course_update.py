from api.course import CourseApi
from api.login import LoginApi
from config import Base_Dir
from data.course import get_data

class TestCourseUpdate:
    token=None
    file_path=Base_Dir+'/data/course.json'
    test_data = get_data(file_path)
    login_data = {
        "username": "admin",
        "password": "HM_2023_test",
        "code": "2",
        "uuid":""
    }
    update_data = {
        "name": "测试你的姆",
        "subject": "6",
        "price": 899999,
    }
    def setup(self):
        self.login_api=LoginApi()
        self.course_api = CourseApi()
        self.login_api.login(self.login_data)
        self.token=self.login_api.login(self.login_data).json().get('token')
    def teardown(self):
        pass
#修改成功
    def test01_update_success(self):
        response = self.course_api.update_course(test_data=self.update_data, token=self.token)
        print(response.json())
        assert response.status_code == 200
        assert '成功' in response.text
        assert response.json().get('code') == 200
    def test02_update_fail(self):
        #修改失败（未登录）
        response=self.course_api.update_course(test_data=self.update_data,token='wafaftq')
        print(response.json())
        assert  response.status_code==200
        assert '失败' in response.text
        assert response.json().get('code')==401


