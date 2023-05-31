from django.db import models

# Create your models here.


class ReceiveEnties(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    book_id = models.CharField(
        max_length=8, null=False, blank=False, verbose_name="เล่มที่เอกสาร")
    whs

    def __str__(self):
        return self.book_id

    class Meta:
        verbose_name = "ข้อมูลการรับสินค้า(Enties)"
        verbose_name_plural = "ข้อมูลการรับสินค้า(Enties)"
