#接口封装，实现接口信息封装，关注接口如何被调用
# 接口信息：1.URL
# 2.请求方法
# 3.请求头 Content-Type Authorization
# 4.请求体 json等multipart/formdata
import requests

from request_project.config import Base_Url


class Contract:
    up_filenames=''
    head_data={"Content-Type":"multipart/form-data","Authorization":""}
    add_header={
        "Content-Type": "application/json", "Authorization": ""
    }
    def __init__(self):
        self.con_load_url=Base_Url+'/api/common/upload'
        self.con_add_url=Base_Url+'/api/contract'
    def upload(self,contract_body,token):
        self.head_data['Authorization']=token
        return requests.post(url=self.con_add_url,headers=self.head_data,files=contract_body)
    def add(self,con_add_body,token):
        con_add_body['Authorization']=token
        return requests.post(url=self.con_add_url,json=con_add_body,headers=self.add_header)
