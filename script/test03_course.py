import pytest
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
    @pytest.mark.parametrize("name,subject,price,applicablePerson,info,status,message,code",test_data)
    def test_course_add(self,name,subject,price,applicablePerson,info,status,message,code):
        course_data={
            "name": name,
            "subject": subject,
            "price":price,
            "applicablePerson": applicablePerson,
            "info":info,
        }
        if message=='认证失败':
            response = self.course_api.add_course(course_data, 'dvsv000')
        else:
            response=self.course_api.add_course(course_data,self.token)
        assert str(response.status_code) == status
        assert message in response.text
        assert str(response.json().get('code'))==code
#测试课程查询的方法
    def test_course_find(self):
        #查询存在的课程和查询失败
        response=self.course_api.find_course(self.token,"?name='测试开发提升课01'")
        print(response.json())


