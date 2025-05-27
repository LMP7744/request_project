#接口封装，实现接口信息封装，关注接口如何被调用
import requests
from request_project.config import Base_Url

class LoginApi:
    uuid=None
    token=None
    header_data={
    "Content-Type":"application/json"}
    def __init__(self):
        self.code_url=Base_Url+"/api/captchaImage"
        self.login_url=Base_Url+"/api/login"
    def login(self,login_body):
        self.uuid = requests.get(url=self.code_url).json().get('uuid')
        login_body['uuid']=self.uuid
        return requests.post(url=self.login_url,json=login_body,headers=self.header_data)