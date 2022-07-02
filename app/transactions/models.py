from django.db import models

# Create your models here.
class TblTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=True)
    book = models.CharField(max_length=100, default="JANUARY", blank=False, null=True)
    startDate = models.DateField(blank=False, null=True)
    endDate = models.DateField(blank=False, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_transaction'
