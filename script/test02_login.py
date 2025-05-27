import pytest
from request_project.api.login import LoginApi
from request_project.config import Base_Dir
from request_project.data.login import get_data

class TestLogin:
    uuid=None
    file_path=Base_Dir+'/data/login.json'
    test_data = get_data(file_path)
    def setup_method(self):
        self.login_api = LoginApi()
    def teardown(self):
        pass
    @pytest.mark.parametrize("username,password,status,message,code",test_data)
    def test_login(self,username,password,status,message,code):
        login_data={
            "username": username,
            "password": password,
            "code": "2",
            "uuid":""
        }
        response=self.login_api.login(login_data)
        assert response.status_code == status
        assert message in response.text
        assert response.json().get('code')==code




