from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseNotFound,HttpResponseRedirect
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from myadmin.models import Orders,Detail,Users,Goods
import time

# #------------------------商品订单-------------------------
def ordersindex(request,pIndex):
	list=Orders.objects.filter()
	#实例化对象
	p=Paginator(list,5)
	#处理当前页号信息
	if pIndex=="":
		pIndex='1',
	pIndex=int(pIndex)
	#获取当前页数据
	list2=p.page(pIndex)
	plist=p.page_range
	return render(request,'myadmin/orders/index.html',{'orderslist':list2,'pIndex':pIndex,'plist':plist})#添加操作

#修改操作
def ordersedit(request,uid):
	xg=Orders.objects.get(id=uid)
	context={"orders":xg}
	return render(request,'myadmin/orders/edit.html',context)
#修改执行操作
def ordersupdate(request,uid):
	xg=Orders.objects.get(id=uid)
	xg.linkman=request.POST['linkman']
	xg.status=request.POST['status']
	xg.save()
	context={'info':'修改成功'}
#except:
	#context={'info':'修该失败'}
	return render(request,"myadmin/orders/info.html",context)

# #-----------------商品详情订单----------
#浏览操作
def detailindex(request,pid):
	
	uids=Detail.objects.filter(orderid=pid)
	orders=Orders.objects.get(id=pid)
	for s in uids:
		# return HttpResponse(s.goodsid)
		s.picname=Goods.objects.get(id=s.goodsid).picname
	# uids=Detail.objects.filter(orderid=pid)
	times=time.strftime('%Y-%m-%d %H:%M:%S',(time.localtime(int(orders.addtime))))
	context={'detailslsit':uids,'orders':orders,'times':times}
	return render(request,'myadmin/detail/index.html',context)#添加操作

#修改操作
def detailedit(request,uid):
	ob=Detail.objects.get(id=uid)
	context={"detail":ob}
	return render(request,'myadmin/detail/edit.html',context)
#修改执行操作
def detailupdate(request,uid):
	try:
		ob=Detail.objects.get(id=uid)
		ob.orderid=request.POST['orderid']
		ob.goodsid=request.POST['goodsid']
		ob.name=request.POST['name']
		ob.price=request.POST['price']
		ob.num=request.POST['num']
		ob.save()
		context={'info':'修改成功'}
	except:
		context={'info':'修该失败'}
	return render(request,"myadmin/detail/info.html",context)
