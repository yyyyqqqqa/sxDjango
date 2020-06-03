from django.test import TestCase

# Create your tests here.

import pandas as pd

from pydash import at

# d = [{'dictId': 3, 'createBy': 'admin', 'createTime': '2018-03-16 11:33:00', 'updateBy': 'ry', 'updateTime': '2018-03-16 11:33:00', 'remark': '系统开关列表', 'dictName': '系统开关', 'dictType': 'sys_normal_disable', 'status': '0'}, {'dictId': 4, 'createBy': 'admin', 'createTime': '2018-03-16 11:33:00', 'updateBy': 'ry', 'updateTime': '2018-03-16 11:33:00', 'remark': '任务状态列表', 'dictName': '任务状态', 'dictType': 'sys_job_status', 'status': '0'}, {'dictId': 8, 'createBy': 'admin', 'createTime': '2018-03-16 11:33:00', 'updateBy': 'ry', 'updateTime': '2018-03-16 11:33:00', 'remark': '通知状态列表', 'dictName': '通知状态', 'dictType': 'sys_notice_status', 'status': '0'}, {'dictId': 10, 'createBy': 'admin', 'createTime': '2018-03-16 11:33:00', 'updateBy': 'ry', 'updateTime': '2018-03-16 11:33:00', 'remark': '登录状态列表', 'dictName': '系统状态', 'dictType': 'sys_common_status', 'status': '0'}, {'dictId': 105, 'createBy': 'admin1', 'createTime': '2020-06-03 10:29:57', 'updateBy': 'admin1', 'updateTime': '2020-06-03 10:30:12', 'remark': 'a', 'dictName': 'a', 'dictType': 'a', 'status': '0'}]
#
#
# df = pd.DataFrame(d)
#
# print(df)

