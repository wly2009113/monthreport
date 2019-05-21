from django.db import models

class Loadinfo(models.Model):
    ip = models.GenericIPAddressField(blank= False,verbose_name='IP')
    business_id = models.CharField(blank=False,max_length = 50, verbose_name='业务模块id')
    business_name = models.CharField(blank= True,max_length = 50,default='',verbose_name='业务模块')
    load = models.CharField(blank= False,max_length = 50,verbose_name='机器负载')
    load_date = models.DateTimeField( auto_now_add =False,verbose_name='低负载日期')
    create_time = models.DateTimeField( auto_now_add =True,verbose_name='创建时间')

    #后台列表显示时，显示IP.
    def __unicode__(self):
        return self.ip



