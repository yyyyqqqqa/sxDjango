from django.db import models

from utils.base_model import BaseModel


class MenuModel(BaseModel):
    menuId = models.IntegerField(primary_key=True,auto_created=True,db_column='menu_id')
    menuName = models.CharField(max_length=50,db_column='menu_name',)
    parentId = models.IntegerField(db_column='parent_id')
    orderNum = models.IntegerField(db_column='order_num')
    path = models.CharField(max_length=200)
    component = models.CharField(max_length=255)
    isFrame = models.IntegerField(db_column='is_frame')
    menuType = models.CharField(max_length=20,db_column='menu_type')
    visible = models.CharField(max_length=20)
    status = models.CharField(max_length=1)
    perms = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)


    class Meta:
        db_table = 'sys_menu'