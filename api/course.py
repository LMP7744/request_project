#接口封装，实现接口信息封装，关注接口如何被调用
# 接口信息：1.URL
# 2.请求方法
# 3.请求头 Content-Type Authorization
# 4.请求体 json等
import requests
from config import Base_Url


class CourseApi:
    header_data = {
        "Authorization": "",
        "Content-Type": "application/json"
    }
    def __init__(self):
        self.course_url=Base_Url+'/api/clues/course'
        self.find_url=Base_Url+'/api/clues/course/list'
        self.update_url=Base_Url+'/api/clues/course'
    def add_course(self,course_body,token):
        self.header_data["Authorization"]=token
        return requests.post(url=self.course_url,headers=self.header_data,json=course_body)
    def find_course(self,token,query):
        header = {"Authorization":token}
        return  requests.get(url=self.find_url + f"/{query}",headers=header)
    def update_course(self,test_data,token):
        self.header_data["Authorization"] = token
        return requests.put(self.update_url,json=test_data,headers=self.header_data)
    def delete_course(self,token,cou_id):
        return requests.delete(self.update_url+f"/{cou_id}",headers={"Authorization":token})