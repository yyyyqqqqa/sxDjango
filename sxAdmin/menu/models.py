from django.db import models


class MenuModel(models.Model):
    menu_id = models.IntegerField(primary_key=True,auto_created=True)
    menu_name = models.CharField(max_length=50,db_column='menu_name')
    parent_id = models.IntegerField()
    order_num = models.IntegerField()
    path = models.CharField(max_length=200)
    component = models.CharField(max_length=255)
    is_frame = models.IntegerField()
    menu_type = models.CharField(max_length=20)
    visible = models.CharField(max_length=20)
    status = models.CharField(max_length=1)
    perms = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    create_by = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now_add=True)
    remark = models.CharField(max_length=500)

    class Meta:
        db_table = 'sys_menu'