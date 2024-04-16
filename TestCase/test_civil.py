import json
import requests
from jsonpath import jsonpath
from common.tool import read_excel, responseToJson

class TestBasic():

    def test_case(self):
        data = read_excel('./api.xlsx','test')
        headers = {'Authorization': 'appcode 8d54e478bbcc4364ab46a2a0a9f1b8de'}
        requests.packages.urllib3.disable_warnings()
        resultlist = []
        for i in data:
            url = i['url']
            body = json.loads(i['data'])
            verifypath = i['path']
            verifyvalue = i['expect']
            r = requests.get(url=url,verify=False,headers = headers,params= body)
            try:
                assert jsonpath(responseToJson(r),verifypath)[0] == verifyvalue
                resultlist.append("passed")
                print("成功啦！")
            except:
                resultlist.append("faile")
                print("失败啦！")
