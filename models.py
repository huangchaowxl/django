from django.db import models

# Create your models here.
class gggg(models.Model):
    title = models.CharField(u'bt', max_length=256)
    content = models.TextField(u'nr')
#    email=models.EmailField(blank=True)
    pub_date = models.DateTimeField(u'fbsl', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'gxsj',auto_now=True, null=True)
    def  __str__(self):
        return self.title

class sensor(models.Model):
     title = models.CharField(u'user', max_length=13)
     content1 = models.CharField(u'device', max_length=13)
     content2 = models.CharField(u'pm1', max_length=13)
     content3 = models.CharField(u'pm2.5', max_length=13)
     content4 = models.CharField(u'co2', max_length=13)
     def  __str__(self):
        return self.title