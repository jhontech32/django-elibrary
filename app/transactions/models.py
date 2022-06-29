from django.db import models

# Create your models here.
class TblTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    book = models.CharField(max_length=100)
    startDate = models.DateField()
    endDate = models.DateField()

    class Meta:
        managed = False
        db_table = 'tbl_transaction'
