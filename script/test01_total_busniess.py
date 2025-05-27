from api.contract import Contract
from api.course import CourseApi
from api.login import LoginApi
from config import Base_Dir
import pytest

class TestTotalBussiness:
    token=None
    def setup_method(self):
        #创建类对象
        self.login_api=LoginApi()
        self.course_api=CourseApi()
        self.contract_api=Contract()
    def teardown_method(self):
        pass

    def test01_login_success(self):
    # 1.登陆成功
        # 从api/login中的LoginApi类的get_code方法获取
        login_body={
    "username": "admin",
    "password": "HM_2023_test",
    "code": "2",
    "uuid": ""}
        login =self.login_api.login(login_body)
        TestTotalBussiness.token=login.json().get('token')
        print(login.status_code)
        print(login.json())

    def test02_course_success(self):
        course_data={
"name": "测试开发提升课01",
"subject": "6",
"price": 899,
"applicablePerson": "2",
"info": "测试开发提升课01"
}

        course=self.course_api.add_course(course_data,TestTotalBussiness.token)
        print(course.json())

    def test03_contract_upload(self):
        with open(Base_Dir+'/data/contract.pdf','rb') as f:#请求体中files要接文件对象
            up_response=self.contract_api.upload(f,TestTotalBussiness.token)
        print(self.contract_api.head_data)#验证数据是否正常
        print(up_response.json())

    def test04_contract_add(self):
        con_add_body= {"name": "测试888", "phone": "13612341888", "contractNo": "HT10012004", "subject": "6",
                       "courseId": 99, "channel": "0", "activityId": 77, "fileName": Base_Dir + '/data/contract.pdf'}
        add_res=self.contract_api.add(con_add_body,self.token)#导入数据
        print(self.contract_api.add_header) #验证数据;
        print(add_res)
