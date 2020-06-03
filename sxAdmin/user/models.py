from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.base_model import BaseModel


class UserModel(AbstractUser,BaseModel):

    userId = models.IntegerField(primary_key=True,auto_created=True,db_column='user_id')
    dept = models.ForeignKey('dept.DeptModel',on_delete=models.CASCADE,null=True)
    nickName = models.CharField(max_length=30,db_column='nick_name')
    userType = models.CharField(max_length=2,db_column='user_type')
    phoneNumber = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)
    avatar = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    delFlag = models.CharField(max_length=10,db_column='del_flag')
    loginIp = models.CharField(max_length=50,db_column='login_ip')
    loginDate = models.CharField(max_length=50,db_column='login_date')


    class Meta:
        db_table = 'sys_user'


class UserRoleModel(models.Model):

    users = models.ForeignKey('UserModel',on_delete=models.CASCADE,null=True,db_column='user_id')

    roles = models.ForeignKey('role.RoleModel',on_delete=models.CASCADE,null=True,db_column='role_id')

    class Meta:

        db_table = 'sys_user_role'