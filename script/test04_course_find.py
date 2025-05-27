from request_project.api.course import CourseApi
from request_project.api.login import LoginApi
from request_project.config import Base_Dir
from request_project.data.course import get_data

class TestCourse:
    token=None
    file_path=Base_Dir+'/data/course.json'
    test_data = get_data(file_path)
    login_data = {
        "username": "admin",
        "password": "HM_2023_test",
        "code": "2",
        "uuid":""
    }
    def setup_method(self):
        self.login_api=LoginApi()
        self.course_api = CourseApi()
        self.login_api.login(self.login_data)
        self.token=self.login_api.login(self.login_data).json().get('token')
    def teardown(self):
        pass

#测试课程查询的方法查询存在的
    def test01_course_find(self):
        #查询存在的课程和查询失败
        response=self.course_api.find_course(self.token,"?name=\"测试开发提升课01\"")
        print(response.json())
        assert  response.status_code==200
        assert '成功' in response.text
        assert response.json().get('code')==200
        #查询失败（用户未登录）
    def test02_course_find(self):
        #查询存在的课程和查询失败
        response=self.course_api.find_course('fail_token',"?subject=\"6\"")
        print(response.json())
        assert  response.status_code==200
        assert '失败' in response.text
        assert response.json().get('code')==401


