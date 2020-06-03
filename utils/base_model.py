from django.db import models




class BaseModel(models.Model):

    createBy = models.CharField(max_length=64,db_column='create_by')
    createTime = models.DateTimeField(auto_now_add=True,db_column='create_time')
    updateBy = models.CharField(max_length=64,db_column='update_by')
    updateTime = models.DateTimeField(db_column='update_time',auto_now=True)
    remark = models.CharField(max_length=500)

    class Meta:
        abstract = True