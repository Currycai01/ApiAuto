import allure
import pytest
from faker.contrib.pytest.plugin import faker
from ruamel.yaml import YAML
from api.context import context
from common.tool import read_excel, responseToJson, testdata
from common.http_method import HttpMethod
import json
from jsonpath import jsonpath
import yaml
from faker import Faker


def get_yaml_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
        return result

def get_name():
    return testdata()

class TestRequest():

    context1 = context()
    SendRequest = HttpMethod()

    @allure.title('获取城市')
    @allure.testcase('获取城市名称')
    #@pytest.mark.parametrize('data',get_yaml_data("./data/API.yaml"))
    def test_city(self):
        r = self.context1.get_city()
        city = jsonpath(json.loads(r.text),context.citypath)
        #保存响应数据到yaml，进行参数传递
        py_object = {'city': city}
        yaml_file = "./data/generate.yaml"
        yaml = YAML(typ='full', pure=True)
        with open(yaml_file, "w", encoding="utf-8") as f:
            yaml.dump(py_object, f)

        assert r.status_code == 200
        assert jsonpath(responseToJson(r),context.citypath)[0] == '北京'

    def test1(self):
        filepath = './data/generate.yaml'
        with open(filepath, 'r', encoding='utf-8') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
            print(type(result))
            print(result)

    '''
    @pytest.mark.parametrize('testcity', get_yaml_data()['city'])
    def test_getweather(self,testcity):
        r = self.context1.get_weather(testcity)
        print(r.text)
    '''


    @allure.title('获取天气')
    @allure.testcase('获取天气信息')
    @pytest.mark.parametrize('testcity',get_yaml_data('./data/generate.yaml')['city'])
    def test_weather(self,testcity):
        data = testcity
        print(testcity)
        r = self.context1.get_weather(data = data)
        print(r.text)

    '''
    @allure.title('获取图片')
    @allure.testcase('获取图片内容')
    def test_photo(self):
        url = "https://api.apiopen.top/api/getImages?page=0&size=5"
        #headers = {'Authorization': 'appcode 8d54e478bbcc4364ab46a2a0a9f1b8de'}
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=url, verify=False)
        print(response.text)
        assert response.status_code == 200
        #assert jsonpath(json.loads(r.text).

    def test_add(self):
        r = self.context1.add_context("hahahaha")
        print(r.text)
    '''

    @allure.testcase('测试造数')
    @pytest.mark.parametrize('name',testdata())
    def test_print(self,name):
        print(name)