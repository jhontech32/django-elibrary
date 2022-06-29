from django.db import models

# Create your models here.
class TblUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_user'

