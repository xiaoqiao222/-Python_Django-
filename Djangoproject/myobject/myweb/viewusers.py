from django.shortcuts import render,redirect
from myweb.models import Goods,Type,Users,Orders,Detail
from django.http import HttpResponse
from django.core.urlresolvers import reverse
import time,os
def loadContext(request):
    context={}
    context['typelist'] = Type.objects.filter(pid=0)
    return context

#d登陆页
def login(request):
	return render(request,'myweb/login.html')
#验证码
def logincodes(request):
	import random
	from PIL import Image, ImageDraw, ImageFont
	bgcolor=(242,164,247)
	width=100
	height=40
	#创建画面对象
	im = Image.new('RGB', (width, height), bgcolor)
	draw=ImageDraw.Draw(im)
	for i  in range(0,100):
		xy=(random.randrange(0,width),random.randrange(0, height))
		fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
		draw.point(xy, fill=fill)
	str1 = '0123456789'
	rand_str = ''
	for i in range(0, 4):
		rand_str += str1[random.randrange(0, len(str1))]
	font = ImageFont.truetype('segoescb.ttf', 21)
	fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
	draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
	draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
	draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
	draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
	del draw
	request.session['verifycode'] = rand_str
	import io
	buf = io.BytesIO()
	#将图片保存在内存中，文件类型为png
	im.save(buf, 'png')
	#将内存中的图片数据返回给客户端，MIME类型为图片png
	return HttpResponse(buf.getvalue(), 'image/png')	
def dologin(request):
	logincode=request.session['verifycode']
	code=request.POST['code']
	if logincode!=code:
		context= {'info':'验证码错误!'}
		return render(request,'myweb/login.html',context)
	try:
		user=Users.objects.get(username=request.POST['username'])
		#判断当前用户是否是后台管理员用户
		if user.state!=2:
			#验证密码
			import hashlib
			m=hashlib.md5()
			m.update(bytes(request.POST['pwd'],encoding='utf-8'))
			if user.pwd==m.hexdigest():
				#此处判断登陆成功 将当前登录信息放入到session中 并条转页面
				request.session['webuser']=user.userlist()
				request.session['we']=True
				return redirect(reverse('index'))
			else:
				context = {'info':'登录密码错误！'}
		else:
			context = {'info':'此用户被禁用'}
	except :
		context = {'info':'账号错误'} 
	return render(request,'myweb/login.html',context)

def logindel(request):
	del request.session['webuser']
	# 跳转登录页面（url地址改变）
	return redirect(reverse('login'))
#注册页
def register(request):
	return render(request,'myweb/register.html')	
def registerinsert(request):
	
	if  request.POST['pwd']!=request.POST['pwds']:
		context={'info':'密码不一致'}
		return render(request,"myweb/register.html",context)
	try:
		ob=Users()
		ob.username=request.POST['username']
		ob.name=request.POST['name']
		import hashlib
		m = hashlib.md5() 
		m.update(bytes(request.POST['pwd'],encoding="utf8"))
		ob.pwd = m.hexdigest()
		ob.sex=request.POST['sex']
		ob.address=request.POST['address']
		ob.code=request.POST['code']
		ob.phone=request.POST['phone']
		ob.email=request.POST['email']
		ob.addtime=time.time()
		ob.save()
		context={'info':'添加成功请登录'}
		return render(request,'myweb/login.html',context)
	except:
		context={'info':'添加失败'}
		return render(request,"myweb/register.html",context)
#-------------------------------------#个人中心--------------
#个人中心
def personalCore(request):
    ob=Users.objects.get(id=request.session['webuser']['id'])
    context={'stu':ob}
    return render(request,"myweb/personalCore.html",context)
#个人中心
def personalCores(request):
    uid=Users.objects.get(name=request.session['webuser']['name']).id
    print(uid)
    corelist=Orders.objects.filter(uid=uid)
    print(corelist)
    for core in corelist:
        pers=[]
        pers=Detail.objects.filter(orderid=core.id)
        core.list=pers
        print(pers)
    context={'corelist':corelist}
    return render(request,"myweb/personalCores.html",context)	
#--修改个人信息
def personaledit(request):
    ob=Users.objects.get(id=request.session['webuser']['id'])
    context={'stu':ob}
    return render(request,'myweb/personalupdate.html',context)
def personalupdate(request,uid):
    try:
        ob=Users.objects.get(id=uid)
        ob.name=request.POST['name']
        ob.sex=request.POST['sex']
        ob.address=request.POST['address']
        ob.code=request.POST['code']
        ob.phone=request.POST['phone']
        ob.email=request.POST['email']
        ob.save()
        context={'info':'修改成功'}

    except:
        context={'info':'修该失败'}
    ob=Users.objects.get(id=request.session['webuser']['id'])
    context={'stu':ob}    
    return render(request,"myweb/personalCore.html",context)
 #订单确认收货修改
def personaledita(request,cid):
    orders=Orders.objects.get(id=cid)
    orders.status = 2
    orders.save()
    return redirect(reverse('personalCores'))
def personaledits(request,cid):
    orders=Orders.objects.get(id=cid)
    orders.status = 3
    orders.save()
    return redirect(reverse('personalCores'))	