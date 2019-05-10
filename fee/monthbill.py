import binascii
import hashlib
import hmac
import sys
import urllib.parse
import urllib.request
import time
import random
class Bill(object):
    def __init__(self,month):
        self.month = month
        
    def cost(self):
        i = 0
        sum = 0.0
        product_fee = {"Elasticsearch Service":0.0,
            "OCR文字识别":0.0,
            "弹性公网IP":0.0,
            "点播VOD":0.0,
            "COS 对象存储":0.0,
            "分布式数据库DCDB":0.0,
            "负载均衡CLB":0.0,
            "共享带宽包":0.0,
            "跨地域互联CRC":0.0,
            "内容分发网络CDN":0.0,
            "实时音视频":0.0,
            "数据万象CI":0.0,
            "天御":0.0,
            "图像识别":0.0,
            "文件存储CFS":0.0,
            "消息服务CKafka":0.0,
            "月度计费精度差异":0.0,
            "云服务器CVM":0.0,
            "云数据库MariaDB（TDSQL）":0.0,
            "云数据库MySQL":0.0,
            "云数据库PostgreSQL":0.0,
            "云数据库Redis":0.0,
            "云通信IM":0.0,
            "云硬盘CBS":0.0,
            "云硬盘快照Snapshot":0.0,
            "直播":0.0,
            "专线接入":0.0,
            "域名注册":0.0,
            "SSL证书":0.0,
            "短信SMS":0.0,
            "云数据迁移CDM":0.0,
            "VPN网关":0.0,
            "云解析":0.0,
            "弹性MapReduce":0.0,
            "TBDS大数据平台软件":0.0,
            "TBDS大数据支持服务":0.0,
            "TCE硬件":0.0,
            "TCE软件":0.0,
            "TCE服务":0.0,
            "实名认证":0.0,
            "web漏洞扫描":0.0
            }
        while True:
            # 用户必须准备好的secretId和secretKey
            # 可以在 https://console.cloud.tencent.com/capi 获取
            secretId = "AKIDDBtLWXCbjbDa0LvlkXvDJGufASUScdrp"
            secretKey = "wd8NYTAdqsRowNYUBez5vWqGIQXZWer1"


            # 在此处定义一些必须的内容
            timeData = str(int(time.time())) # 时间戳
            nonceData = int(random.random()*10000) # Nonce，官网给的信息：随机正整数，与 Timestamp 联合起来， 用于防止重放攻击
            actionData = "DescribeBillResourceSummary" # Action一般是操作名称
            uriData = "billing.tencentcloudapi.com" # uri，请参考官网
            #signMethod="HmacSHA256" # 加密方法
            requestMethod = "GET" # 请求方法，在签名时会遇到，如果签名时使用的是GET，那么在请求时也请使用GET
            versionData = '2018-07-09' # 版本选择
            offset = 1000 * i
            limit = 1000   #一页多少条数据，默认20条，最大不超过1000
            periodType = "byPayTime"
            month = self.month

            # 签名时需要的字典
            paramDict = {
                "Action":actionData,
                "Version":versionData,
                "SecretId":secretId,
                "Nonce":nonceData,
                "Timestamp":timeData,
                "Offset":offset,
                "Limit":limit,
                "Offset":offset,
                "PeriodType":periodType,
                "Month":month
            }

            # 首先对所有请求参数按参数名做字典序升序排列，所谓字典序升序排列，
            # 直观上就如同在字典中排列单词一样排序，按照字母表或数字表里递增
            # 顺序的排列次序，即先考虑第一个“字母”，在相同的情况下考虑第二
            # 个“字母”，依此类推。

            tempList = []
            tempDict = {}
            for key,value in paramDict.items():
                tempLowerData = key.lower()
                tempList.append(tempLowerData)
                tempDict[tempLowerData] = key
            tempList.sort()

            resultList = []
            for data in tempList:
                tempStr = str(tempDict[data]) + "=" + str(paramDict[tempDict[data]])
                resultList.append(tempStr)

            sourceStr = "&".join(resultList)

            # 获得拼接的字符串，用于签名
            # 此步骤生成请求字符串。 将把上一步排序好的请求参数格式化成“参数名称”=“参数值”的形式，如对Action参数，
            # 其参数名称为"Action"，参数值为"DescribeRegions"，因此格式化后就为Action=DescribeRegions。
            # 注意：“参数值”为原始值而非url编码后的值。
            # 然后将格式化后的各个参数用"&"拼接在一起，最终生成请求字符串。
            # 此步骤生成签名原文字符串。 签名原文字符串由以下几个参数构成:
            # 1) 请求方法: 支持 POST 和 GET 方式，这里使用 GET 请求，注意方法为全大写。
            # 2) 请求主机:查看实例列表(DescribeRegions)的请求域名为：cvm.tencentcloudapi.com。实际的请求域名根据接口所属模块的不同而不同，详见各接口说明。
            # 3) 请求路径: 当前版本云API的请求路径固定为 / 。 
            #4) 请求字符串: 即上一步生成的请求字符串。
            # 签名原文串的拼接规则为:
            #   请求方法 + 请求主机 +请求路径 + ? + 请求字符串
            requestStr = "%s%s%s%s%s"%(requestMethod,uriData,"/","?",sourceStr)

            # 调用签名方法：
            # 1) 先进行sha1加密
            # 2) 在进行base64编码
            # 3) 进行url编码

            if sys.version_info[0] > 2:
                signStr = requestStr.encode("utf-8")
                secretKey = secretKey.encode("utf-8")

            hashed = hmac.new(secretKey,signStr,hashlib.sha1)
            base64Date = binascii.b2a_base64(hashed.digest())[:-1] 

            if sys.version_info[0] > 2:
                base64Date = base64Date.decode()

            base64Date = urllib.parse.quote(base64Date)



            # 根据uri构建请求的url
            url = "https://" + uriData + "/" + "?" + sourceStr + "&Signature=" + base64Date 

            # 获得response
            responseData = urllib.request.urlopen(url).read().decode("utf-8")

            #print(responseData)

            # 获得到的结果形式：
            #  {"Response":{"RequestId":"0fd2e5b4-0beb-4e01-906f-e63dd7dd33af","Source":"en","Target":"zh","TargetText":"\u4f60\u597d\u4e16\u754c"}}

            # 对Json字符串处理
            import json
            list = json.loads(responseData)["Response"]["ResourceSummarySet"]
            if len(list) == 0:
                break
            for Data in list: 
                sum = sum + float(Data["RealTotalCost"])
                if Data["BusinessCodeName"] in product_fee:
                    product_fee[Data["BusinessCodeName"]] = product_fee[Data["BusinessCodeName"]] + float(Data["RealTotalCost"]) 
        #        else:
        #            print(Data["BusinessCodeName"])
            i = i + 1
        return sum,product_fee
        
