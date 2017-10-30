from django.shortcuts import render,redirect
from myweb.models import Goods,Type,Users,Orders,Detail
from django.http import HttpResponse
from django.core.urlresolvers import reverse
import time,os
# 自定义公共信息加载函数
def loadContext(request):
    context={}
    context['typelist'] = Type.objects.filter(pid=0)
    return context

#购物车页
def cartindex(request):
	context=loadContext(request)
	if 'cartlist' not in request.session:
		request.session['cartlist']={}
	return render(request,'myweb/cart.html',context)
#添加商品
def cartadd(request,cid):
	#获取要放入购物车中的信息
	goods=Goods.objects.get(id=cid)
	cart=goods.toDict();
	cart['m']=int(request.POST['m'])
	#print(cart['m'])
	#从session获取购物车的信息
	if 'cartlist' in request.session:
		cartlist=request.session['cartlist']
	else:
		cartlist={}
	#判断此商品是否在购物车中
	if cid in cartlist:
		cartlist[cid]['m']+=cart['m']
	else:
		cartlist[cid]=cart
	#将购物车信息放回到session
	request.session['cartlist']=cartlist
	return redirect(reverse('cartindex'))
def cartdel(request,cid):
	cartlist=request.session['cartlist']
	del cartlist[cid]
	request.session['cartlist']=cartlist
	return redirect(reverse(cartindex))
def cartclear(request):
	context=loadContext(request)
	request.session['cartlist']={}
	return render(request,'myweb/cart.html',context)
def cartchange(request):
	 context=loadContext(request)
	 cartlist=request.session['cartlist']
	 #获取信息
	 cartid=request.GET['cid']
	 num=int(request.GET['m'])
	 if num<1:
	 	num=1
	 cartlist[cartid]['m']=num
	 request.session['cartlist']=cartlist
	 return render(request,'myweb/cart.html',context)


#================订单处理================================
#订单表单页
def ordersform(request):
    #获取要结账的商品id信息
    ids = request.GET['gids']
    if ids == '':
        return HttpResponse("请选择要结账的商品")
    gids = ids.split(',')
    # 获取购物车中的商品信息
    cartlist = request.session['cartlist']
    #封装要结账的商品信息，以及累计总金额
    orderlist = {}
    total = 0
    for sid in gids:
        orderlist[sid] = cartlist[sid]
        total += cartlist[sid]['price']*cartlist[sid]['m'] #累计总金额
    request.session['orderlist'] = orderlist
    request.session['total'] = total
    return render(request,"myweb/orders.html")

#订单确认页
def ordersconfirm(request):
    return render(request,"myweb/ordersconfirm.html")

#执行订单添加
def ordersinsert(request):
    # 封装订单信息，并执行添加
    orders = Orders()
    orders.uid = request.session['webuser']['id']
    orders.linkman = request.POST['linkman']
    orders.address = request.POST['address']
    orders.code = request.POST['code']
    orders.phone = request.POST['phone']
    orders.addtime = time.time()
    orders.total = request.session['total']
    orders.status = 0
    orders.save()
    #获取订单详情
    orderlist = request.session['orderlist']
    cartlist = request.session['cartlist']
    #遍历购物信息，并添加订单详情信息
    for cart in orderlist.values():
        print(cart)
        detail = Detail()
        detail.orderid = orders.id
        detail.goodsid = cart['id']
        detail.name = cart['goods']
        detail.price = cart['price']
        detail.num = cart['m']
        detail.save()
        cartlist.pop(str(cart['id']))
    request.session['cartlist']=cartlist
    return HttpResponse("订单成功：订单id号："+str(orders.id))


#提示信息
def ordersinfo(request):
    pass

