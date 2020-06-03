from django.db import models

from utils.base_model import BaseModel


class RoleModel(BaseModel):

    roleId = models.IntegerField(primary_key=True,auto_created=True,db_column='role_id')
    roleName = models.CharField(max_length=20,db_column='role_name')
    roleKey = models.CharField(max_length=100,db_column='role_key')
    roleSort = models.IntegerField(db_column='role_sort')
    dataScope = models.CharField(max_length=10,db_column='data_scope')
    status = models.CharField(max_length=10)
    delFlag = models.CharField(max_length=1,db_column='del_flag')

    class Meta:


        db_table = 'sys_role'



class RoleMenuModel(models.Model):

    role = models.ForeignKey('RoleModel',on_delete=models.CASCADE) #这里不设置主键

    menu = models.ForeignKey('menu.MenuModel',on_delete=models.CASCADE) #这里不设置主键


    class Meta:

        db_table = 'sys_role_menu'
