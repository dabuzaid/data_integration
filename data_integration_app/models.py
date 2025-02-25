from django.db import models

class Customer(models.Model):
    cus_no = models.FloatField(null=True, blank=True)
    cus_name = models.CharField(max_length=120, null=True, blank=True)
    cus_contact = models.CharField(max_length=50, null=True, blank=True)
    cus_tel = models.CharField(max_length=20, null=True, blank=True)
    cus_fax = models.CharField(max_length=20, null=True, blank=True)
    cus_address = models.CharField(max_length=120, null=True, blank=True)
    cus_branch = models.SmallIntegerField(null=True, blank=True)
    cus_account = models.FloatField(null=True, blank=True)
    cus_opening = models.FloatField(null=True, blank=True)
    cus_remark = models.CharField(max_length=120, null=True, blank=True)
    cus_user = models.SmallIntegerField(null=True, blank=True)
    cus_balance = models.FloatField(null=True, blank=True)
    cus_opening1 = models.FloatField(null=True, blank=True)
    cus_balance1 = models.FloatField(null=True, blank=True)
    cus_name_eng = models.CharField(max_length=120, null=True, blank=True)
    cus_period = models.FloatField(null=True, blank=True)
    cus_card_no = models.CharField(max_length=20, null=True, blank=True)
    cus_credit_limit = models.FloatField(null=True, blank=True)
    cus_trading_no = models.CharField(max_length=15, null=True, blank=True)
    cus_email = models.CharField(max_length=50, null=True, blank=True)
    cus_bal30 = models.FloatField(null=True, blank=True)
    cus_bal60 = models.FloatField(null=True, blank=True)
    cus_bal90 = models.FloatField(null=True, blank=True)
    cus_bal120 = models.FloatField(null=True, blank=True)
    cus_salesman = models.SmallIntegerField(null=True, blank=True)
    cus_start_date = models.DateTimeField(null=True, blank=True)
    cus_sale_account = models.FloatField(null=True, blank=True)
    cus_sale_cost = models.CharField(max_length=10, null=True, blank=True)
    cus_bal_grt120 = models.FloatField(null=True, blank=True)
    cus_mainid = models.FloatField(null=True, blank=True)
    cus_name_en = models.CharField(max_length=120, null=True, blank=True)
    cus_type = models.IntegerField(null=True, blank=True)
    cus_country = models.IntegerField(null=True, blank=True)
    cus_sub_type = models.IntegerField(null=True, blank=True)
    cus_l = models.SmallIntegerField(null=True, blank=True)
    cus_h = models.SmallIntegerField(null=True, blank=True)
    cus_key_account = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.cus_name or "Unknown Customer"


class Salesman(models.Model):
    smn_no = models.SmallIntegerField(null=True, blank=True)
    smn_name = models.CharField(max_length=50, null=True, blank=True)
    smn_tel = models.CharField(max_length=20, null=True, blank=True)
    smn_pager = models.CharField(max_length=20, null=True, blank=True)
    smn_address = models.CharField(max_length=50, null=True, blank=True)
    smn_remark = models.CharField(max_length=150, null=True, blank=True)
    smn_user = models.SmallIntegerField(null=True, blank=True)
    smn_max_dis = models.SmallIntegerField(null=True, blank=True)
    smn_area = models.IntegerField(null=True, blank=True)
    smn_target = models.FloatField(null=True, blank=True)
    smn_type = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.smn_name or "Unknown Salesman"


class SalesM(models.Model):
    salm_no = models.FloatField()  # NOT NULL, part of PK
    salm_branch = models.SmallIntegerField()  # NOT NULL, part of PK
    salm_type = models.SmallIntegerField()  # NOT NULL, part of PK

    salm_date = models.DateTimeField(null=True, blank=True)
    salm_customer = models.FloatField(null=True, blank=True)
    salm_cash_type = models.SmallIntegerField(null=True, blank=True)
    salm_sman = models.SmallIntegerField(null=True, blank=True)
    salm_qno = models.FloatField(null=True, blank=True)
    salm_remark = models.CharField(max_length=120, null=True, blank=True)
    salm_downpay = models.FloatField(null=True, blank=True)
    salm_discra = models.SmallIntegerField(null=True, blank=True)
    salm_disca = models.FloatField(null=True, blank=True)
    salm_total = models.FloatField(null=True, blank=True)
    salm_net = models.FloatField(null=True, blank=True)
    salm_user = models.SmallIntegerField(null=True, blank=True)
    salm_flag = models.CharField(max_length=1, null=True, blank=True)
    salm_remaind = models.FloatField(null=True, blank=True)
    salm_discr = models.FloatField(null=True, blank=True)
    salm_aflag = models.CharField(max_length=1, null=True, blank=True)
    salm_custname = models.CharField(max_length=50, null=True, blank=True)
    salm_asset = models.CharField(max_length=10, null=True, blank=True)
    salm_asset_type = models.SmallIntegerField(null=True, blank=True)
    salm_housetel = models.CharField(max_length=15, null=True, blank=True)
    salm_worktel = models.CharField(max_length=15, null=True, blank=True)
    salm_addded_value = models.FloatField(null=True, blank=True)
    salm_addded_desc = models.CharField(max_length=50, null=True, blank=True)
    salm_ret_invno = models.FloatField(null=True, blank=True)
    salm_location = models.CharField(max_length=5, null=True, blank=True)
    salm_locatdesc = models.CharField(max_length=50, null=True, blank=True)
    salm_numtotext = models.CharField(max_length=100, null=True, blank=True)
    salm_duedate = models.CharField(max_length=10, null=True, blank=True)
    salm_instcust = models.FloatField(null=True, blank=True)
    salm_sponsor = models.FloatField(null=True, blank=True)
    salm_collector = models.SmallIntegerField(null=True, blank=True)
    salm_instcount = models.SmallIntegerField(null=True, blank=True)
    salm_instamount = models.FloatField(null=True, blank=True)
    salm_instrem = models.FloatField(null=True, blank=True)
    salm_iflag = models.CharField(max_length=1, null=True, blank=True)
    salm_key = models.FloatField(null=True, blank=True)
    salm_newinv = models.FloatField(null=True, blank=True)
    salm_mode = models.CharField(max_length=1, null=True, blank=True)
    salm_date1 = models.DateTimeField(null=True, blank=True)
    salm_date2 = models.DateTimeField(null=True, blank=True)
    salm_paid = models.FloatField(null=True, blank=True)
    salm_mastercard_amnt = models.FloatField(null=True, blank=True)
    salm_mastercard_disc = models.FloatField(null=True, blank=True)
    salm_visa_amnt = models.FloatField(null=True, blank=True)
    salm_visa_disc = models.FloatField(null=True, blank=True)
    salm_delivery_branch = models.SmallIntegerField(null=True, blank=True)
    salm_voucher = models.FloatField(null=True, blank=True)
    salm_vtype = models.IntegerField(null=True, blank=True)
    transaction_id = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'SalesM'  # Ensure table name matches
        unique_together = ('salm_no', 'salm_branch', 'salm_type')  # Composite PK

    def __str__(self):
        return f"SalesM {self.salm_no} - Branch {self.salm_branch}"


class SalesD(models.Model):
    sald_no = models.FloatField()
    sald_branch = models.SmallIntegerField()
    sald_type = models.SmallIntegerField()
    sald_serial = models.SmallIntegerField()
    sald_item = models.CharField(max_length=20, null=True, blank=True)
    sald_qty = models.FloatField(null=True, blank=True)
    sald_price = models.FloatField(null=True, blank=True)
    sald_total = models.FloatField(null=True, blank=True)
    sald_delv_branch = models.SmallIntegerField(null=True, blank=True)
    sald_user = models.SmallIntegerField(null=True, blank=True)
    sald_itname = models.CharField(max_length=100, null=True, blank=True)
    sald_woodcolor = models.CharField(max_length=10, null=True, blank=True)
    sald_textilecolor = models.CharField(max_length=10, null=True, blank=True)
    sald_brand = models.CharField(max_length=10, null=True, blank=True)
    sald_category = models.CharField(max_length=10, null=True, blank=True)
    sald_branddes = models.CharField(max_length=30, null=True, blank=True)
    sald_ticket = models.FloatField(null=True, blank=True)
    sald_qtyfree = models.FloatField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['sald_no', 'sald_branch', 'sald_type', 'sald_serial'], name='pk_salesd')
        ]
        db_table = 'SalesD'

    def __str__(self):
        return f"SalesD({self.sald_no}, {self.sald_branch}, {self.sald_type}, {self.sald_serial})"


class ItemCard(models.Model):
    itc_serialno = models.FloatField(null=True, blank=True)
    itc_code = models.CharField(max_length=20, null=True, blank=True)
    itc_date = models.DateTimeField(null=True, blank=True)
    itc_branch = models.SmallIntegerField(null=True, blank=True)
    itc_in = models.FloatField(null=True, blank=True)
    itc_out = models.FloatField(null=True, blank=True)
    itc_document = models.FloatField(null=True, blank=True)
    itc_cost = models.FloatField(null=True, blank=True)
    itc_type = models.CharField(max_length=2, null=True, blank=True)
    itc_price = models.FloatField(null=True, blank=True)
    itc_otherbranch = models.SmallIntegerField(null=True, blank=True)
    str_handheld_no = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        db_table = 'ItemCard'

    def __str__(self):
        return f"ItemCard({self.itc_code}, {self.itc_branch}, {self.itc_date})"


class CustCard(models.Model):
    ccd_serial = models.AutoField(primary_key=True)  # Auto-incrementing field (IDENTITY in SQL)
    ccd_code = models.FloatField(null=True, blank=True)
    ccd_date = models.DateTimeField(null=True, blank=True)
    ccd_debit = models.FloatField(null=True, blank=True)
    ccd_credit = models.FloatField(null=True, blank=True)
    ccd_branch = models.SmallIntegerField(null=True, blank=True)
    ccd_document = models.FloatField(null=True, blank=True)
    ccd_type = models.CharField(max_length=2, null=True, blank=True)
    ccd_type2 = models.CharField(max_length=1, null=True, blank=True)  # `char(1)` mapped to CharField
    ccd_invtype = models.SmallIntegerField(null=True, blank=True)
    ccd_description = models.CharField(max_length=200, null=True, blank=True)
    ccd_voucher = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'CustCard'
        constraints = [
            models.UniqueConstraint(fields=['ccd_serial'], name='IX_CustCard')
        ]

    def __str__(self):
        return f"CustCard({self.ccd_serial}, {self.ccd_code}, {self.ccd_date})"