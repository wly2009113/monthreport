from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class Load(models.Model):
    ip = models.GenericIPAddressField(blank= False,verbose_name='IP')
    business_id = models.IntegerField(blank= False, verbose_name='业务模块id')
    business_name = models.CharField(blank= True,max_length = 50,default='',verbose_name='业务模块')
    load = models.IntegerField(blank= False,verbose_name='机器负载')
    create_time = models.DateTimeField( auto_now_add =True,verbose_name='创建时间')

    #后台列表显示时，显示IP.
    def __unicode__(self):
        return self.ip



