from django.shortcuts import render
from django.http import HttpResponse
from . import monthbill
import time
from . import models


def refresh(request):
    result = models.MonthFee.objects.order_by('-id')
    if result.exists():
        yearStart = int(result[0].month.split('-')[0])
        monStart = int(result[0].month.split('-')[1])
        if monStart == 12:
            yearStart = yearStart + 1
            monStart = 1
        else:
            monStart = monStart + 1
    else:
        yearStart = 2018
        monStart = 8
    print(yearStart,monStart)
    yearNow = int(time.strftime("%Y",time.localtime()))
    monNow = int(time.strftime("%m",time.localtime()))
    while not (yearStart == yearNow and monStart == monNow):
        mon = str(yearStart) + "-" + str(monStart).zfill(2)
        bill = monthbill.Bill(mon)
        sum,productfee = bill.cost()
        b = models.MonthFee(month = mon,\
                            sumfee = sum,\
                            ES = productfee["Elasticsearch Service"],\
                            OCR = productfee["OCR文字识别"],\
                            GWIP = productfee["弹性公网IP"],\
                            VOD = productfee["点播VOD"],\
                            COS = productfee["COS 对象存储"],\
                            DCDB = productfee["分布式数据库DCDB"],\
                            CLB = productfee["负载均衡CLB"],\
                            DKB = productfee["共享带宽包"],\
                            CRC = productfee["跨地域互联CRC"],\
                            CDN = productfee["内容分发网络CDN"],\
                            VDO = productfee["实时音视频"],\
                            CI = productfee["数据万象CI"],\
                            TY = productfee["天御"],\
                            TXSB = productfee["图像识别"],\
                            CFS = productfee["文件存储CFS"],\
                            CKafka = productfee["消息服务CKafka"],\
                            YDJFJDCY = productfee["月度计费精度差异"],\
                            CVM = productfee["云服务器CVM"],\
                            MariaDB = productfee["云数据库MariaDB（TDSQL）"],\
                            MySQL = productfee["云数据库MySQL"],\
                            PostgreSQL = productfee["云数据库PostgreSQL"],\
                            Redis = productfee["云数据库Redis"],\
                            IM = productfee["云通信IM"],\
                            CBS = productfee["云硬盘CBS"],\
                            Snapshot = productfee["云硬盘快照Snapshot"],\
                            ZB = productfee["直播"],\
                            ZXJR = productfee["专线接入"],\
                            YMZC = productfee["域名注册"],\
                            SSL = productfee["SSL证书"],\
                            SMS = productfee["短信SMS"],\
                            CDM = productfee["云数据迁移CDM"],\
                            VPN = productfee["VPN网关"],\
                            YJX = productfee["云解析"],\
                            MapReduce = productfee["弹性MapReduce"],\
                            TBDSSOFT = productfee["TBDS大数据平台软件"],\
                            TBDSSVC = productfee["TBDS大数据支持服务"],\
                            TCEYJ = productfee["TCE硬件"],\
                            TCERJ = productfee["TCE软件"],\
                            TCEFW = productfee["TCE服务"],\
                            SMRZ = productfee["实名认证"],\
                            WEB = productfee["web漏洞扫描"])
        b.save()
        if monStart == 12:
            yearStart = yearStart + 1
            monStart = 1
        else:
            monStart = monStart + 1
 
    return HttpResponse("Refresh Success!")

# Create your views here.
