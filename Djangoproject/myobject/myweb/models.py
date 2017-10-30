
from django.db import models

# Create your models here.
# 商品分类
class Users(models.Model):
	username = models.CharField(max_length=32)
	name = models.CharField(max_length=16)
	pwd = models.CharField(max_length=32)
	sex = models.IntegerField(max_length=1)
	address = models.CharField(max_length=255)
	code = models.CharField(max_length=6)
	phone = models.CharField(max_length=16)
	email = models.CharField(max_length=50)
	state = models.IntegerField(max_length=1,default=1)
	addtime = models.IntegerField()
	def userlist(self):
		return {'id':self.id,'username':self.username,'name':self.name,'address':self.address,'phone':self.phone,'code':self.code}
class Type(models.Model):
	name = models.CharField(max_length=32)
	pid = models.IntegerField(default=0)
	path = models.CharField(max_length=255)

# 商品信息表
class Goods(models.Model):
	typeid = models.IntegerField()
	goods = models.CharField(max_length=32)
	company = models.CharField(max_length=50)
	descr = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=2)
	picname = models.CharField(max_length=255)
	state = models.IntegerField(max_length=1,default=1)
	store = models.IntegerField(default=0)
	num = models.IntegerField(default=0)
	clicknum = models.IntegerField(default=0)
	addtime = models.IntegerField()
	def toDict(self):
		return {'id':self.id,'goods':self.goods,'picname':self.picname,'price':self.price,'store':self.store,'m':1}
class Orders(models.Model):
    uid = models.IntegerField()
    linkman = models.CharField(max_length=32)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    addtime = models.IntegerField()
    total = models.FloatField()
    status = models.IntegerField()

class Detail(models.Model):
    orderid = models.IntegerField()
    goodsid = models.IntegerField()
    name = models.CharField(max_length=32)
    price = models.FloatField()
    num = models.IntegerField()