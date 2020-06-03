from django.db import models



class StatusModel(models.Model):

    id = models.IntegerField(primary_key=True,auto_created=True)

    status = models.CharField(max_length=20)

    class Meta:
        db_table = 'status'


class StuModel(models.Model):

    phone = models.CharField(primary_key=True,max_length=100)
    status = models.ForeignKey('StatusModel',on_delete=models.CASCADE,db_column='status_id',blank=True, null=True)
    gw = models.ForeignKey('user.UserModel',on_delete=models.CASCADE,db_column='gw_id',blank=True, null=True)
    name = models.CharField(max_length=20)
    tracking_details = models.CharField(max_length=100)
    import_date = models.CharField(max_length=40)
    import_times = models.IntegerField()
    job_objective = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    years = models.CharField(max_length=10)
    edu = models.CharField(max_length=20)
    school = models.CharField(max_length=100)
    professional = models.CharField(max_length=100)
    email = models.CharField(max_length=20)
    re_com = models.CharField(max_length=100)
    re_job = models.CharField(max_length=100)
    hope_money = models.CharField(max_length=100)
    source = models.CharField(max_length=20)
    jianli = models.CharField(max_length=20)
    mtimes = models.CharField(max_length=40)

    class Meta:
        db_table = 'sx_customer_infos'


class StuDetailModel(models.Model):

    # phone = models.CharField(max_length=100,db_column='phone')
    id = models.IntegerField(primary_key=True,auto_created=True)
    co1 = models.CharField(max_length=100)
    co2 = models.CharField(max_length=1000)
    index = models.IntegerField()
    phone = models.CharField(max_length=20)


    class Meta:
        db_table = 'stu_detail'