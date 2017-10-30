from django.shortcuts import render,redirect
from myweb.models import Goods,Type,Users
from django.http import HttpResponse
from django.core.urlresolvers import reverse
import time,os


def loadContext(request):
	context={}
	context['typelist'] = Type.objects.filter(pid=0)
	return context
#首页
def index(request):
	if 'we' not in request.session:
		request.session['we']=False
	context=loadContext(request)
	context['mxlist']=Goods.objects.order_by('clicknum')[0:8]
	context['rqlist']=Goods.objects.order_by('num')[0:4]
	context['zxlist']=Goods.objects.order_by('addtime')[0:4]
	return render(request,'myweb/index.html',context)
#列表页
def listing(request,uid=0):
	context=loadContext(request)
	if uid==0:
		context['goodslist'] = Goods.objects.all()
	else:
		#获取当前类别下的所有子类别信息
		context['type']=Type.objects.filter(pid=uid)
		# 判断参数ttid是否有值
		if request.GET.get('tid',None):
			context['goodslist'] = Goods.objects.filter(typeid=request.GET['tid'])
		else:
			 # 获取指定商品类别下的所有商品信息
			context['goodslist'] = Goods.objects.filter(typeid__in=Type.objects.only('id').filter(path__contains=','+str(uid)+','))
	return render(request,'myweb/listing.html',context)
#详情页
def details(request,uid):
	context=loadContext(request)
	ob=Goods.objects.get(id=uid)
	ob.clicknum+=1
	ob.save()
	context={'details':ob}
	return render(request,'myweb/details.html',context)

