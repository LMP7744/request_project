import json
from request_project.config import Base_Dir

data_list=[]
def get_data(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        data=json.load(f)
        for i in data:
            data_list.append(tuple(i.values()))
    # print(data_list)
    return data_list

if __name__=='__main__':
    data_list=get_data(Base_Dir+'/data/course.json')
    print(data_list)