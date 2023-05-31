from django.db import models

# Create your models here.


class WhouseFormulaVCST(models.Model):
    FCSKID = models.CharField(
        primary_key=True,
        max_length=8, verbose_name="ID", db_column='FCSKID', editable=False)
    FCCODE = models.CharField(
        max_length=20, verbose_name="รหัส", db_column='FCCODE')
    FCNAME = models.CharField(
        max_length=20, verbose_name="ชื่อ", db_column='FCNAME')
    FCNAME2 = models.CharField(
        max_length=20, verbose_name="ข้อมูลเพิ่มเติม", db_column='FCNAME2')
    FTDATETIME = models.DateTimeField(
        verbose_name="สร้างเมื่อ", db_column='FTDATETIME', auto_now_add=True)
    FTLASTEDIT = models.DateTimeField(
        verbose_name="แก้ไขเมื่อ", db_column='FTLASTEDIT', auto_now=True)
    FTLASTUPD = models.DateTimeField(
        verbose_name="อัพเดทเมื่อ", db_column='FTLASTUPD', auto_now=True)

    def __str__(self) -> str:
        return self.FCNAME

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "WHOUSE"
        app_label = "vcst"
        verbose_name = "ข้อมูลคลังสินค้า"
        verbose_name_plural = "คลังสินค้า"


class CorpFormulaVCST(models.Model):
    FCSKID = models.CharField(
        primary_key=True,
        max_length=8, verbose_name="ID", db_column='FCSKID', editable=False)
    FCCODE = models.CharField(
        max_length=20, verbose_name="รหัส", db_column='FCCODE')
    FCNAME = models.CharField(
        max_length=50, verbose_name="ชื่อ", db_column='FCNAME')
    FCNAME2 = models.CharField(
        max_length=255, verbose_name="ข้อมูลเพิ่มเติม", db_column='FCNAME2', null=False, blank=True)
    FCADDR1 = models.CharField(
        max_length=50, db_column='FCADDR1', verbose_name="FCADDR1", null=False, blank=True)
    FCADDR12 = models.CharField(
        max_length=50, db_column='FCADDR12', verbose_name="FCADDR12", null=False, blank=True)
    FCADDR2 = models.CharField(
        max_length=50, db_column='FCADDR2', verbose_name="FCADDR2", null=False, blank=True)
    FCADDR2 = models.CharField(
        max_length=50, db_column='FCADDR22', verbose_name="FCADDR22", null=False, blank=True)
    FCTEL = models.CharField(
        max_length=50, db_column='FCTEL', verbose_name="FCTEL", null=False, blank=True)
    FCFAX = models.CharField(
        max_length=50, db_column='FCFAX', verbose_name="FCFAX", null=False, blank=True)
    FTDATETIME = models.DateTimeField(
        verbose_name="สร้างเมื่อ", db_column='FTDATETIME', auto_now_add=True)
    FTLASTEDIT = models.DateTimeField(
        verbose_name="แก้ไขเมื่อ", db_column='FTLASTEDIT', auto_now=True)
    FTLASTUPD = models.DateTimeField(
        verbose_name="อัพเดทเมื่อ", db_column='FTLASTUPD', auto_now=True)
    FCTAXID = models.CharField(
        max_length=50, db_column='FCTAXID', verbose_name="FCTAXID", null=False, blank=True)

    def __str__(self) -> str:
        return self.FCNAME

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "CORP"
        app_label = "vcst"
        verbose_name = "รายชื่อบริษัท"
        verbose_name_plural = "รายชื่อบริษัท"


class ProductTypeFormulaVCST(models.Model):
    FCSKID = models.CharField(
        max_length=8, verbose_name="ID", db_column='FCSKID', editable=False)
    FCCODE = models.CharField(
        primary_key=True,
        max_length=20, verbose_name="รหัส", db_column='FCCODE')
    FCNAME = models.CharField(
        max_length=20, verbose_name="ชื่อ", db_column='FCNAME')
    FCNAME2 = models.CharField(
        max_length=20, verbose_name="ข้อมูลเพิ่มเติม", db_column='FCNAME2')
    FTDATETIME = models.DateTimeField(
        verbose_name="สร้างเมื่อ", db_column='FTDATETIME', auto_now_add=True)
    FTLASTEDIT = models.DateTimeField(
        verbose_name="แก้ไขเมื่อ", db_column='FTLASTEDIT', auto_now=True)
    FTLASTUPD = models.DateTimeField(
        verbose_name="อัพเดทเมื่อ", db_column='FTLASTUPD', auto_now=True)

    def __str__(self) -> str:
        return self.FCNAME

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "PRODTYPE"
        app_label = "vcst"
        verbose_name = "ประเภทสินค้า"
        verbose_name_plural = "ประเภทสินค้า"


class UmFormulaVCST(models.Model):
    FCSKID = models.CharField(
        primary_key=True,
        max_length=8, verbose_name="ID", db_column='FCSKID', editable=False)
    FCCODE = models.CharField(
        max_length=20, verbose_name="รหัส", db_column='FCCODE')
    FCNAME = models.CharField(
        max_length=20, verbose_name="ชื่อ", db_column='FCNAME')
    FCNAME2 = models.CharField(
        max_length=20, verbose_name="ข้อมูลเพิ่มเติม", db_column='FCNAME2')
    FTDATETIME = models.DateTimeField(
        verbose_name="สร้างเมื่อ", db_column='FTDATETIME', auto_now_add=True)
    FTLASTEDIT = models.DateTimeField(
        verbose_name="แก้ไขเมื่อ", db_column='FTLASTEDIT', auto_now=True)
    FTLASTUPD = models.DateTimeField(
        verbose_name="อัพเดทเมื่อ", db_column='FTLASTUPD', auto_now=True)

    def __str__(self) -> str:
        return self.FCNAME

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "UM"
        app_label = "vcst"
        verbose_name = "ข้อมูลหน่วยสินค้า"
        verbose_name_plural = "หน่วยสินค้า"


class PdGrdFormulaVCST(models.Model):
    FCSKID = models.CharField(
        primary_key=True,
        max_length=8, verbose_name="ID", db_column='FCSKID', editable=False)
    FCCODE = models.CharField(
        max_length=20, verbose_name="รหัส", db_column='FCCODE')
    FCNAME = models.CharField(
        max_length=20, verbose_name="ชื่อ", db_column='FCNAME')
    FCNAME2 = models.CharField(
        max_length=20, verbose_name="ข้อมูลเพิ่มเติม", db_column='FCNAME2')
    FTDATETIME = models.DateTimeField(
        verbose_name="สร้างเมื่อ", db_column='FTDATETIME', auto_now_add=True)
    FTLASTEDIT = models.DateTimeField(
        verbose_name="แก้ไขเมื่อ", db_column='FTLASTEDIT', auto_now=True)
    FTLASTUPD = models.DateTimeField(
        verbose_name="อัพเดทเมื่อ", db_column='FTLASTUPD', auto_now=True)

    def __str__(self) -> str:
        return self.FCNAME

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "PDGRP"
        app_label = "vcst"
        verbose_name = "ข้อมูลกลุ่ม"
        verbose_name_plural = "กลุ่มสินค้า"


class ProductFormulaVCST(models.Model):
    FCSKID = models.CharField(
        primary_key=True, max_length=8, verbose_name="ID", db_column='FCSKID', editable=False)
    FCCODE = models.CharField(
        max_length=20, verbose_name="รหัส", db_column='FCCODE')
    FCNAME = models.CharField(
        max_length=20, verbose_name="ชื่อ", db_column='FCNAME')
    FCNAME2 = models.CharField(
        max_length=20, verbose_name="เพิ่มเติม1", db_column='FCNAME2')
    FCSNAME = models.CharField(
        max_length=20, verbose_name="เพิ่มเติม2", db_column='FCSNAME')
    FCSNAME2 = models.CharField(
        max_length=20, verbose_name="เพิ่มเติม3", db_column='FCSNAME2')
    FCDATASER = models.CharField(
        max_length=20, verbose_name="รหัสจำเพราะ", db_column='FCDATASER', editable=False)
    FCCORP = models.ForeignKey(
        CorpFormulaVCST, verbose_name="ชื่อบริษัท", db_column='FCCORP', on_delete=models.CASCADE)
    FCTYPE = models.ForeignKey(
        ProductTypeFormulaVCST, verbose_name="ประเภท", db_column='FCTYPE', on_delete=models.CASCADE)
    FCPDGRP = models.ForeignKey(
        PdGrdFormulaVCST, verbose_name="กลุ่ม", db_column='FCPDGRP', on_delete=models.CASCADE)
    FCUM = models.ForeignKey(
        UmFormulaVCST, verbose_name="หน่วย", db_column='FCUM', on_delete=models.CASCADE)
    FTDATETIME = models.DateTimeField(
        verbose_name="สร้างเมื่อ", db_column='FTDATETIME', auto_now_add=True)
    FTLASTEDIT = models.DateTimeField(
        verbose_name="แก้ไขเมื่อ", db_column='FTLASTEDIT', auto_now=True)
    FTLASTUPD = models.DateTimeField(
        verbose_name="อัพเดทเมื่อ", db_column='FTLASTUPD', auto_now=True)

    def __str__(self) -> str:
        return self.FCCODE

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "PROD"
        app_label = "vcst"
        verbose_name = "รายการข้อมูลสินค้า"
        verbose_name_plural = "รายการสินค้า"


class EmployeeVCST(models.Model):
    FCSKID = models.CharField(
        primary_key=True, max_length=8, verbose_name="ID", db_column='FCSKID', editable=False)
    FCLOGIN = models.CharField(
        max_length=20, verbose_name="รหัส", db_column='FCLOGIN')
    FCPW = models.CharField(
        max_length=20, verbose_name="รหัสผ่าน", db_column='FCPW')
    FCRCODE = models.CharField(
        max_length=20, verbose_name="ชื่อ", db_column='FCRCODE')
    FTDATETIME = models.DateTimeField(
        verbose_name="สร้างเมื่อ", db_column='FTDATETIME', auto_now_add=True)
    FTLASTEDIT = models.DateTimeField(
        verbose_name="แก้ไขเมื่อ", db_column='FTLASTEDIT', auto_now=True)
    FTLASTUPD = models.DateTimeField(
        verbose_name="อัพเดทเมื่อ", db_column='FTLASTUPD', auto_now=True)

    def __str__(self) -> str:
        return self.FCRCODE

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "EMPLR"
        app_label = "vcst"
        verbose_name = "รายการผู้ใช้งาน"
        verbose_name_plural = "รายการผู้ใช้งาน"


class CoorVCST(models.Model):
    FCSKID = models.CharField(
        primary_key=True, max_length=8, verbose_name="ID", db_column='FCSKID', editable=False)
    FCCODE = models.CharField(
        max_length=20, verbose_name="รหัส", db_column='FCCODE')
    FCNAME = models.CharField(
        max_length=20, verbose_name="ชื่อ", db_column='FCNAME')
    FCSNAME = models.CharField(
        max_length=20, verbose_name="-", db_column='FCSNAME')
    FCNO = models.CharField(
        max_length=20, verbose_name="เลขที่", db_column='FCNO')
    FCFLOOR = models.CharField(
        max_length=50, verbose_name="ชั้น", db_column='FCFLOOR')
    FCROOMNO = models.CharField(
        max_length=50, verbose_name="ห้อง", db_column='FCROOMNO')
    FCBUILDING = models.CharField(
        max_length=50, verbose_name="-", db_column='FCBUILDING')
    FCMOO = models.CharField(
        max_length=50, verbose_name="หมู่", db_column='FCMOO')
    FCSOI = models.CharField(
        max_length=50, verbose_name="ซอย", db_column='FCSOI')
    FCROAD = models.CharField(
        max_length=50, verbose_name="ถนน", db_column='FCROAD')
    FCTAMBON = models.CharField(
        max_length=50, verbose_name="ตำบล", db_column='FCTAMBON')
    FCAMPHUR = models.CharField(
        max_length=50, verbose_name="อำเภอ", db_column='FCAMPHUR')
    FCPROVINCE = models.CharField(
        max_length=50, verbose_name="จังหวัด", db_column='FCPROVINCE')
    FCZIP = models.CharField(
        max_length=10, verbose_name="รหัสไปรษณี", db_column='FCZIP')
    FCBRANCHNM = models.CharField(
        max_length=10, verbose_name="ประเภท", db_column='FCBRANCHNM')
    FMMEMDATA = models.TextField(
        verbose_name="หมายเหตุ", db_column='FMMEMDATA')
    FCCORP = models.ForeignKey(
        CorpFormulaVCST, verbose_name="ชื่อบริษัท", db_column='FCCORP', on_delete=models.CASCADE)
    FTDATETIME = models.DateTimeField(
        verbose_name="สร้างเมื่อ", db_column='FTDATETIME', auto_now_add=True)
    FTLASTEDIT = models.DateTimeField(
        verbose_name="แก้ไขเมื่อ", db_column='FTLASTEDIT', auto_now=True)
    FTLASTUPD = models.DateTimeField(
        verbose_name="อัพเดทเมื่อ", db_column='FTLASTUPD', auto_now=True)

    def __str__(self) -> str:
        return self.FCNAME

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "COOR"
        app_label = "vcst"
        verbose_name = "รายการลูกค้า"
        verbose_name_plural = "รายการลูกค้า"


class GlrefVCST(models.Model):
    FCBOOK = models.CharField(
        max_length=8, verbose_name="เล่มเอกสาร", db_column='FCBOOK')
    FCBRANCH = models.CharField(
        max_length=8, verbose_name="พื้นที่จังหวัด", db_column='FCBRANCH')
    FCCODE = models.CharField(
        max_length=20, verbose_name="รหัส", db_column='FCCODE', editable=False)
    FCCOOR = models.ForeignKey(
        CoorVCST, verbose_name="ลูกค้า", db_column='FCCOOR', on_delete=models.CASCADE)
    FCCORP = models.ForeignKey(
        CorpFormulaVCST, verbose_name="ชื่อบริษัท", db_column='FCCORP', on_delete=models.CASCADE)
    FCCORRECTB = models.ForeignKey(
        EmployeeVCST, verbose_name="ชื่อบริษัท", db_column='FCCORRECTB', on_delete=models.CASCADE, editable=False)
    # FCCREATEBY = models.ForeignKey(
    #     EmployeeVCST, verbose_name="ชื่อบริษัท", db_column='FCCREATEBY', on_delete=models.CASCADE)
    # FCCREATETY = models.ForeignKey(
    #     EmployeeVCST, verbose_name="ชื่อบริษัท", db_column='FCCREATETY', on_delete=models.CASCADE)
    FCDATASER = models.CharField(
        max_length=8, verbose_name="APPID", db_column='FCDATASER', editable=False)
    # FCDELICOOR
    # FCDEPT
    # FCEAFTERR
    # FCGID
    # FCGLHEAD
    # FCJOB
    # FCPROJ
    FCREFNO = models.CharField(
        max_length=20, verbose_name="เลขที่เอกสารอ้างอิง", db_column='FCREFNO', editable=False)
    # FCREFTYPE
    # FCRFTYPE
    # FCSECT
    FCSKID = models.CharField(
        primary_key=True, max_length=8, verbose_name="ID", db_column='FCSKID', editable=False)
    FCSTEP = models.CharField(
        max_length=5, verbose_name="I/O", db_column='FCSTEP')
    # FCFRWHOUSE = models.ForeignKey(
    #     WhouseFormulaVCST, verbose_name="จากคลัง", db_column='FCFRWHOUSE', on_delete=models.CASCADE)
    # FCTOWHOUSE = models.ForeignKey(
    #     WhouseFormulaVCST, verbose_name="เข้าที่คลัง", db_column='FCTOWHOUSE', on_delete=models.CASCADE)
    # FCVATCOOR
    # FDDATE
    # FIMILLISEC
    # FNAFTDEP
    # FNAFTDEPKE
    FNAMT = models.DecimalField(
        decimal_places=2,
        max_digits=2, verbose_name="จำนวน", db_column="FNAMT")
    FTDATETIME = models.DateTimeField(
        verbose_name="สร้างเมื่อ", db_column='FTDATETIME', auto_now_add=True)
    FTLASTEDIT = models.DateTimeField(
        verbose_name="แก้ไขเมื่อ", db_column='FTLASTEDIT', auto_now=True)
    FTLASTUPD = models.DateTimeField(
        verbose_name="อัพเดทเมื่อ", db_column='FTLASTUPD', auto_now=True)
    FCLUPDAPP = models.CharField(
        max_length=8, verbose_name="FCLUPDAPP", db_column='FCLUPDAPP', editable=False)
    FMMEMDATA = models.TextField(
        verbose_name="หมายเหตุ", db_column='FMMEMDATA', editable=False)

    def __str__(self) -> str:
        return self.FCSKID

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "GLREF"
        app_label = "vcst"
        verbose_name = "รายการ GLREF"
        verbose_name_plural = "รายการ GLREF"
