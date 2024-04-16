import json
import os

import pytest
import requests
import schedule
import time

from TestCase.test_civil import TestBasic
from common import tool

if __name__ == '__main__':
  #tool.testdata()

  pytest.main(['-vs','./TestCase/test_request.py::TestRequest::test_print'])

  '''
  def job():
  print("定时任务执行中...")

 # 每天定时执行任务
 schedule.every().day.at('14:51').do(job)

 while True:
  schedule.run_pending()
  time.sleep(1)
 '''

 #pytest运行，指定数据生成路径
 #pytest.main(['-vs', "./TestCase/test_request.py::TestRequest::test_print",'--clean-alluredir',"--alluredir","./report/result"])
 # 生成allure报告，指定报告生成路径
 #os.system('allure generate ./report/result/ -o report/html --clean')
 #渲染
 #os.system('allure open ./report/html')

 #os.system('allure serve ./report/result')


'''
 file_name = r'./report/html/widgets/summary.json'
 with open(file_name, 'r', encoding='utf-8') as f:
     data = json.load(f)
 case_json = data['statistic']
 case_all = case_json['total']  # 测试用例总数
 case_fail = case_json['failed']  # 失败用例数量
 case_pass = case_json['passed']  # 成功用例数量
 if case_all >= 0:
  # 计算出来当前失败率
  case_rate = round((case_pass / case_all) * 100, 2)
 else:
  print('未获取到执行结果')
 # 发送报告内容
 text = f"咖喱接口测试"\
        f"\n用例通过率：{case_rate}%" \
        f"\n执行用例数：{case_all}个" \
        f"\n成功用例数：{case_pass}个" \
        f"\n失败用例数：{case_fail}个"
'''