from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseNotFound,HttpResponseRedirect
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

from myadmin.models import Users
import time
# Create your views here.
def index(request):


	return render(request,'myadmin/index.html')
#=================后台管理员操作======
#管理员登陆
def login(request):
	return render(request,"myadmin/login.html")
#验证码
def logincode(request):
	import random
	from PIL import Image, ImageDraw, ImageFont
	bgcolor=(242,164,247)
	width=100
	height=25
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
#管理员执行登陆
def dologin(request):
	logincode=request.session['verifycode']
	code=request.POST['code']
	if logincode!=code:
		context = {'info':'验证码错误！'}
		return render(request,'myadmin/login.html',context)
	try:
		user = Users.objects.get(username=request.POST['username'])
	#判断当前用户是否是后台管理员用户
		if user.state == 0:
			# 验证密码
			import hashlib
			m = hashlib.md5() 
			m.update(bytes(request.POST['pwd'],encoding="utf8"))
			if user.pwd == m.hexdigest():
			#if user.pwd == request.POST['pwd']:
				# 此处登录成功，将当前登录信息放入到session中，并跳转页面
				request.session['adminuser'] = user.name
				#print(json.dumps(user))
				return redirect(reverse('myadmin_index'))
			else:
				context = {'info':'登录密码错误！'}
		else:
			context = {'info':'此用户非后台管理用户！'}
	except:
		context = {'info':'登录账号错误！'}
	return render(request,"myadmin/login.html",context)
#管理员退出
def logout(request):
	 # 清除登录的session信息
	del request.session['adminuser']
    # 跳转登录页面（url地址改变）
	return redirect(reverse('myadmin_login'))
    # 加载登录页面(url地址不变)
    #return render(request,"myadmin/login.html")



#------------后台会员操作-------------
#浏览会员
def usersindex(request,pIndex):
	list=Users.objects.filter()
	#实例化对象
	p=Paginator(list,5)
	#处理当前页号信息
	if pIndex=="":
		pIndex='1',
	pIndex=int(pIndex)
	#获取当前页数据
	list2=p.page(pIndex)
	plist=p.page_range
	return render(request,'myadmin/users/index.html',{'stulist':list2,'pIndex':pIndex,'plist':plist})
#添加操作
def usersadd(request):
	return render(request,'myadmin/users/add.html')
#添加执行操作
def usersinsert(request):
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
		ob.state=request.POST['state']
		ob.addtime=time.time()
		ob.save()
		context={'info':'添加成功'}
	except:
		context={'info':'添加失败'}
		return render(request,"myadmin/users/info.html",context)
#删除操作
def usersdel(request,uid):
	ob=Users.objects.get(id=uid)
	ob.delete()
	return HttpResponseRedirect(reverse('myadmin_usersindex',args=(1,)))
#修改操作
def usersedit(request,uid):
	ob=Users.objects.get(id=uid)
	context={"stu":ob}
	return render(request,'myadmin/users/edit.html',context)
#修改执行操作
def usersupdate(request,uid):
	try:
		ob=Users.objects.get(id=uid)
		ob.username=request.POST['username']
		ob.name=request.POST['name']
		ob.sex=request.POST['sex']
		ob.address=request.POST['address']
		ob.code=request.POST['code']
		ob.phone=request.POST['phone']
		ob.email=request.POST['email']
		ob.state=request.POST['state']
		ob.addtime=request.POST['addtime']
		ob.save()
		context={'info':'修改成功'}
	except:
		context={'info':'修该失败'}
	return render(request,"myadmin/users/info.html",context)


