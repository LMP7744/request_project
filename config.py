import os #动态获取项目路径，我在测试轮询
Base_Url="http://kdtx-test.itheima.net"
Base_Dir=os.path.dirname(__file__)
if __name__=='__name__':
    print(Base_Dir,Base_Url)
