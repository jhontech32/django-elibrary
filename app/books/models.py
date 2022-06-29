from django.db import models

# Create your models here.
class TblBook(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_book'

