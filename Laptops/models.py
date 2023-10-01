from django.db import models
# from django.contrib.auth.models import User
#Create your models here.





class asset_data(models.Model):
    asset_id = models.AutoField(primary_key=True,auto_created=100)
    login_user=models.CharField(max_length=50)
    asset_type=models.CharField(max_length=20)
    Company_name=models.CharField(max_length=20)
    asset_model=models.CharField(max_length=20)
    serial_no=models.CharField(max_length=20)
    host_name=models.CharField(max_length=20)
    processor=models.CharField(max_length=20)
    ram=models.CharField(max_length=10)
    storage_type=models.CharField(max_length=20)
    storage=models.CharField(max_length=10)
    screen_size=models.CharField(max_length=20)
    purchasing_date=models.CharField(max_length=20)
    asset_age=models.CharField(max_length=20)
    sap_code=models.CharField(max_length=20)
    tba=models.CharField(max_length=20)
    lt_dt_cond=models.CharField(max_length=30)
    other_details=models.TextField(max_length=200)
    asset_location=models.CharField(max_length=30)
    asset_state=models.CharField(max_length=20)
    asset_scrap=models.CharField(max_length=20)
    assign_status=models.BooleanField(default=False)



class emp_data(models.Model):
    emp_id=models.CharField(primary_key=True, max_length=10)
    login_user=models.CharField(max_length=50)
    alias_id=models.CharField(max_length=10,unique=True)
    email_address=models.EmailField(unique=True)
    grade=models.CharField(max_length=10)
    designation=models.CharField(max_length=30)
    department=models.CharField(max_length=30)
    job_profile=models.CharField(max_length=30)
    user_location=models.CharField(max_length=50)
    user_state=models.CharField(max_length=50)
    region=models.CharField(max_length=30)
    business_unit=models.CharField(max_length=30)
    status=models.BooleanField(default=False)




class assign_assets_data_m(models.Model):
    assign_id=models.AutoField(primary_key=True,auto_created=1001)
    login_user=models.CharField(max_length=50)

    asset_id1=models.OneToOneField("asset_data",on_delete=models.CASCADE)
    asset_model=models.CharField(max_length=20)
    serial_no=models.CharField(max_length=20)
    host_name=models.CharField(max_length=20)
    asset_location=models.CharField(max_length=30)
    purchasing_date=models.CharField(max_length=20)
    tba=models.CharField(max_length=20)
    
    emp_id1=models.OneToOneField("emp_data",on_delete=models.PROTECT)
    alias_id=models.CharField(max_length=10,unique=True)
    email_address=models.EmailField(unique=True)
    grade=models.CharField(max_length=10)
    designation=models.CharField(max_length=30)
    department=models.CharField(max_length=30)






    

