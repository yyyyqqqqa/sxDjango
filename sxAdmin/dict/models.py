from django.db import models

from utils.base_model import BaseModel


class DictTypeModel(BaseModel):
    dictId = models.IntegerField(primary_key=True,auto_created=True,db_column='dict_id')
    dictName = models.CharField(max_length=100,db_column='dict_name')
    dictType = models.CharField(max_length=100,db_column='dict_type')
    status = models.CharField(max_length=10)

    class Meta:
        db_table = 'sys_dict_type'




class DictDataModel(BaseModel):

    dictCode = models.IntegerField(primary_key=True,auto_created=True,db_column='dict_code')
    dictSort = models.IntegerField(db_column='dict_sort')
    dictLabel = models.CharField(max_length=100,db_column='dict_label')
    dictValue = models.CharField(max_length=100,db_column='dict_value')
    dictType = models.CharField(max_length=20,db_column='dict_type')
    cssClass = models.CharField(max_length=100,db_column='css_class')
    listClass = models.CharField(max_length=100,db_column='list_class')
    isDefault = models.CharField(max_length=10,db_column='is_default')
    status = models.CharField(max_length=10)


    class Meta:

        db_table = 'sys_dict_data'
