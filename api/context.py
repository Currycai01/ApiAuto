from common.http_method import HttpMethod
class context():

    SendRequest = HttpMethod()

    def add_context(self,body):
        r = self.SendRequest.run_main(url="http://jsonplaceholder.typicode.com/posts", method='post',data = body)
        return r

    def get_context(self):
        r = self.SendRequest.run_main(url="http://jsonplaceholder.typicode.com/posts", method='get')
        return r

    def get_text(self,id):
        url = "http://jsonplaceholder.typicode.com/posts/"+id
        r = self.SendRequest.run_main(url=url, method='get')
        return r

    def get_city(self):
        headers = {'Authorization': 'appcode 8d54e478bbcc4364ab46a2a0a9f1b8de'}
        r = self.SendRequest.run_main(url="https://jisutqybmf.market.alicloudapi.com/weather/city", method='get',headers = headers)
        return r

    citypath = "$.result[0].city"

    def get_weather(self,data):
        headers = {'Authorization': 'appcode 8d54e478bbcc4364ab46a2a0a9f1b8de'}
        data = {"city": data}
        r = self.SendRequest.run_main(url="https://jisutqybmf.market.alicloudapi.com/weather/query", method='get',headers=headers,data = data)
        return r