from django.db import models

class MonthFee(models.Model):
    month = models.CharField(max_length = 10,unique = True)
    sumfee = models.IntegerField()
    ES = models.IntegerField()
    OCR = models.IntegerField()
    GWIP = models.IntegerField()
    VOD = models.IntegerField()
    COS = models.IntegerField()
    DCDB = models.IntegerField()
    CLB = models.IntegerField()
    DKB = models.IntegerField()
    CRC = models.IntegerField()
    CDN = models.IntegerField()
    VDO = models.IntegerField()
    CI = models.IntegerField()
    TY = models.IntegerField()
    TXSB = models.IntegerField()
    CFS = models.IntegerField()
    CKafka = models.IntegerField()
    YDJFJDCY = models.IntegerField()
    CVM = models.IntegerField()
    MariaDB = models.IntegerField()
    MySQL = models.IntegerField()
    PostgreSQL = models.IntegerField()
    Redis = models.IntegerField()
    IM = models.IntegerField()
    CBS = models.IntegerField()
    Snapshot = models.IntegerField()
    ZB = models.IntegerField()
    ZXJR = models.IntegerField()
    YMZC = models.IntegerField()
    SSL = models.IntegerField()
    SMS = models.IntegerField()
    CDM = models.IntegerField()
    VPN = models.IntegerField()
    YJX = models.IntegerField()
    MapReduce = models.IntegerField()
    TBDSSOFT = models.IntegerField()
    TBDSSVC = models.IntegerField()
    TCEYJ = models.IntegerField()
    TCERJ = models.IntegerField()
    TCEFW = models.IntegerField()
    SMRZ = models.IntegerField()
    WEB = models.IntegerField()


# Create your models here.
