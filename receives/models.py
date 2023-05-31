from django.db import models
from vcst.models import CoorVCST
# Create your models here.

RECEIVE_STATUS = (
    ("0", "Adjust"),
    ("1", "Waiting"),
    ("2", "Success"),
    ("3", "Failed"),
)


class ReceiveEnties(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    receive_date = models.DateTimeField(verbose_name="วันที่รับ")
    book_id = models.CharField(
        max_length=8, null=False, blank=False, verbose_name="เล่มที่เอกสาร")
    whs_id = models.CharField(max_length=8, null=False,
                              blank=False, verbose_name="คลังสินค้า")
    invoice_no = models.CharField(
        max_length=20, null=False, blank=False, verbose_name="เลขที่ Invoice")
    coor_id = models.ForeignKey(
        CoorVCST, null=False, blank=False, verbose_name="ผู้ขาย", on_delete=models.CASCADE)
    sect_id = models.CharField(
        max_length=8, null=False, blank=False, verbose_name="แผนก", editable=False)
    po_no = models.CharField(max_length=20, verbose_name="เลขที่ PO")
    remark = models.TextField(verbose_name="หมายเหตุ")
    status = models.CharField(
        max_length=1, choices=RECEIVE_STATUS, null=False, blank=False, verbose_name="สถานะ")
    sync = models.BooleanField(verbose_name="สถานะซิงค์ข้อมูล", editable=False)
    created_at = models.DateTimeField(
        verbose_name="สร้างเมื่อ", editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name="แก้ไขเมื่อ", editable=False, auto_now=True)

    def __str__(self):
        return self.book_id

    class Meta:
        verbose_name = "ข้อมูลการรับสินค้า(Enties)"
        verbose_name_plural = "ข้อมูลการรับสินค้า(Enties)"
        db_table = "tbt_receive_enties"
