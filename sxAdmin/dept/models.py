from django.db import models

from utils.base_model import BaseModel


class DeptModel(BaseModel):


    deptId = models.IntegerField(primary_key=True,auto_created=True,db_column='dept_id')
    parentId = models.IntegerField(db_column='parent_id')
    ancestors = models.CharField(max_length=100)
    deptName = models.CharField(max_length=100,db_column='dept_name')
    orderNum = models.IntegerField(db_column='order_num')
    leader = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    status = models.CharField(max_length=1)
    delFlag = models.CharField(max_length=1,db_column='del_flag')

    class Meta:
        db_table = 'sys_dept'

