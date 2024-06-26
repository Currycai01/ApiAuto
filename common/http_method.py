import requests

class HttpMethod():
    def post_main(self,url,**kwargs):
        # 忽略不安全的请求警告信息
        requests.packages.urllib3.disable_warnings()
        # 遇到requests的ssl验证，若想直接跳过不验证，设置verify=False即可
        response = requests.post(url=url, verify=False,**kwargs)
        return response

    def get_main(self,url,**kwargs):
        # 忽略不安全的请求警告信息
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=url,verify=False,**kwargs)
        return response

    def run_main(self,url,method,**kwargs):
        # 忽略不安全的请求警告信息
        requests.packages.urllib3.disable_warnings()
        response = ''
        if(method == 'post'):
            response = self.post_main(url=url,**kwargs)
        elif(method == 'get'):
            response = self.get_main(url=url,**kwargs)
            # 将响应的的数据以字典数据结构和json数据格式返回
        return response
'''
class RunMethod(object):

    def post_main(self, url, headers, data):
        # 忽略不安全的请求警告信息
        requests.packages.urllib3.disable_warnings()
        # 遇到requests的ssl验证，若想直接跳过不验证，设置verify=False即可
        response = requests.post(url=url, headers=headers, data=data, verify=False)
        return response

    def get_main(self, url, headers, data=None):
        # 忽略不安全的请求警告信息
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=url, headers=headers, data=data, verify=False)
        return response

    def run_main(self, method, url, headers, data=None):
        # 忽略不安全的请求警告信息
        requests.packages.urllib3.disable_warnings()
        requests.adapters.DEFAULT_RETRIES = 5

        if method == "Post":
            res = self.post_main(url, headers, data)
        elif method == "Get":
            res = self.get_main(url, headers, data)
        # 将响应的的数据以字典数据结构和json数据格式返回
        return res.json()
'''