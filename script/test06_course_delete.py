from request_project.api.course import CourseApi
from request_project.api.login import LoginApi

class TestCourseDelete:
    token=None
    login_data = {
        "username": "admin",
        "password": "HM_2023_test",
        "code": "2",
        "uuid":""
    }
    def setup_method(self):
        self.login_api = LoginApi()
        self.course_api = CourseApi()
        self.token=self.login_api.login(self.login_data).json().get('token')
    def test01_delete_success(self):
        response=self.course_api.delete_course(self.token,1)
        assert response.status_code==200
        assert response.json().get('code')==200
        assert '成功' in response.text
    def test02_delete_fail_id(self):
        response=self.course_api.delete_course(self.token,66)
        assert response.status_code==200
        assert response.json().get('code')==500
        assert '失败' in response.text
    def test03_delete_fail_token(self):
        response=self.course_api.delete_course('wdadw419684',6)
        assert response.status_code==200
        assert response.json().get('code')==401
        assert '失败' in response.text

