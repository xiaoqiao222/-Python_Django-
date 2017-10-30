from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseNotFound,HttpResponseRedirect
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from myadmin.models import Goods,Type
import time,os
from PIL import Image




# #------------------------商品类型-------------------------
def typeindex(request):
	    # 执行数据查询，并放置到模板中
	list = Type.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
    # 遍历查询结果，为每个结果对象追加一个pname属性，目的用于缩进标题
	for ob in list:
		ob.pname ='. . . '*(ob.path.count(',')-1)
        # print(list[0].__dict__)
	context = {"typelist":list}
	return render(request,'myadmin/type/index.html',context)
def typeaddss(request,uid):	
    # 获取父类别信息，若没有则默认为根类别信息
	if uid == '0':
		context = {'pid':0,'path':'0,','name':'根类别'}
	else:
		ob = Type.objects.get(id=uid)
		context = {'pid':ob.id,'path':ob.path+str(ob.id)+',','name':ob.name}
	return render(request,'myadmin/type/add.html',context)

#执行商品类别信息添加    
def typeinserts(request):
	try:
		ob = Type()
		ob.name = request.POST['name']
		ob.pid = request.POST['pid']
		ob.path = request.POST['path']
		ob.save()
		context = {'info':'添加成功！'}
	except:
		context = {'info':'添加失败！'}
	return render(request,"myadmin/type/info.html",context)

#删除操作
def typedel(request,uid):
	try:
        # 获取被删除商品的子类别信息量，若有数据，就禁止删除当前类别
		row = Type.objects.filter(pid=uid).count()
		if row != 0 :
			context = {'info':'删除失败：此类别下还有子类别！'}
			return render(request,"myadmin/type/info.html",context)
		ws=Goods.objects.filter(typeid=uid).count()
		if ws > 0 :
			context = {'info':'删除失败：此类别下还有商品！'}
			return render(request,"myadmin/type/info.html",context)	
		ob = Type.objects.get(id=uid)
		ob.delete()
		context = {'info':'删除成功！'}
	except:
		context = {'info':'删除失败！'}
	return HttpResponseRedirect(reverse('myadmin_typeindex'))
#修改操作
def typeedit(request,uid):
	try:
		ob = Type.objects.get(id=uid)
		context = {'type':ob}
		return render(request,"myadmin/type/edit.html",context)
	except:
		context = {'info':'没有找到要修改的信息！'}	
	return render(request,"myadmin/type/info.html",context)
	# ob=Type.objects.get(id=uid)
	# context={"type":ob}
	# return render(request,'myadmin/type/edit.html',context)
#修改操作
# def typeedits(request):
# 	dlist=Type.objects.filter()
# 	list=[]
# 	for ob in dlist:
# 		list.append({'id':ob.id,'name':ob.name})
# 	return JsonResponse({'data':list})
#修改执行操作
def typeupdate(request,uid):
	# try:
	# 	ob=Type.objects.get(id=uid)
	# 	ob.name=request.POST['name']
	# 	uid=int(request.POST['id'])
	# 	ob.pid=str(id)
	# 	path=Type.objects.get(id=uid)
	# 	print(path)
	# 	if path.path=='0':
	# 		ob.path='0'
	# 		context={'info':'修改成功'}
	# 		ob.save()
	# 		return render(request,"myadmin/type/info.html",context)
	# 	ob.path=path.path+','+str(pid)
	# 	ob.save()
	# 	context={'info':'修改成功'}
	# except:
	# 	context={'info':'修改失败'}
	# return render(request,"myadmin/type/info.html",context)
	try:
		ob = Type.objects.get(id=uid)
		ob.name = request.POST['name']
		ob.save()
		context = {'info':'修改成功！'}
	except:
		context = {'info':'修改失败！'}
	return render(request,"myadmin/type/info.html",context)
# #-----------------商品详情----------
#浏览操作
def goodsindex(request,pIndex):
	list=Goods.objects.filter()
	for ob in list:
		ty = Type.objects.get(id=ob.typeid)
		ob.typename = ty.name
	context = {"goodslist":list}
	#实例化对象
	p=Paginator(list,5)
	#处理当前页号信息
	if pIndex=="":
		pIndex='1',
	pIndex=int(pIndex)
	#获取当前页数据
	list2=p.page(pIndex)
	plist=p.page_range
	return render(request,'myadmin/goods/index.html',{'goodslist':list2,'pIndex':pIndex,'plist':plist},context)#添加操作
def goodsadd(request):
	return render(request,'myadmin/goods/add.html')
#添加执行操作
def goodsadds(request,uid):
	dlist=Type.objects.filter(pid = uid)
	list=[]
	for ob in dlist:
		list.append({'id':ob.id,'name':ob.name})
		print(ob.id)
	return JsonResponse({'data':list})
def goodsinsert(request):
	try:
		# 判断并执行图片上传，缩放等处理
		myfile = request.FILES.get("picname", None)
		print(myfile)
		if not myfile:
			return HttpResponse("没有上传文件信息！")
			# 以时间戳命名一个新图片名称
		filename= str(time.time())+"."+myfile.name.split('.').pop()
		destination = open(os.path.join("./static/goodsimg/",filename),'wb+')
		for chunk in myfile.chunks():      # 分块写入文件  
			destination.write(chunk)  
		destination.close()
		# 执行图片缩放
		# 执行图片缩放
		im = Image.open("./static/goodsimg/"+filename)
		# 缩放到375*375:
		im.thumbnail((375, 375))
		# 把缩放后的图像用jpeg格式保存:
		im.save("./static/goodsimg/"+filename, 'jpeg')
		# 缩放到220*220:
		im.thumbnail((220, 220))
		# 把缩放后的图像用jpeg格式保存:
		im.save("./static/goodsimg/m_"+filename, 'jpeg')
		# 缩放到220*220:
		im.thumbnail((100, 100))
		# 把缩放后的图像用jpeg格式保存:
		im.save("./static/goodsimg/s_"+filename, 'jpeg')
		print(request.POST['typeid'])
		ob=Goods()

		ob.typeid=request.POST['typeid'] 
		ob.goods=request.POST['goods']
		ob.company=request.POST['company']
		ob.descr=request.POST['descr']
		ob.price=request.POST['price']
		ob.picname=filename
		ob.state=request.POST['state']
		ob.store=request.POST['store']
		ob.num=request.POST['num']
		ob.clicknum=request.POST['clicknum']
		ob.addtime=time.time()
		ob.save()
		context={'info':'添加成功'}
	except:
		context={'info':'添加失败'}
	return render(request,"myadmin/goods/info.html",context)
#删除操作
def goodsdel(request,uid):
	ob=Goods.objects.get(id=uid)
	# os.remove("./static/goods/"+ob.picname)   
	# os.remove("./static/goods/m_"+ob.picname)   
	# os.remove("./static/goods/s_"+ob.picname)
	ob.delete()
	return HttpResponseRedirect(reverse('myadmin_goodsindex',args=(1,)))
#修改操作
def goodsedit(request,uid):
	ob=Goods.objects.get(id=uid)
	context={"goods":ob}
	return render(request,'myadmin/goods/edit.html',context)
#修改执行操作
def goodsupdate(request):
	try:
		b=False
		oldpicname=request.POST['oldpicname']
		if None !=request.FILES.get('picname'):
			myfile = request.FILES.get("picname", None)
			print(myfile)
			if not myfile:
				return HttpResponse("没有上传文件信息！")
				# 以时间戳命名一个新图片名称
			filename= str(time.time())+"."+myfile.name.split('.').pop()
			destination = open(os.path.join("./static/goodsimg/",filename),'wb+')
			for chunk in myfile.chunks():      # 分块写入文件  
				destination.write(chunk)  
			destination.close()
			im = Image.open("./static/goodsimg/"+filename)
			# 缩放到375*375:
			im.thumbnail((375, 375))
			# 把缩放后的图像用jpeg格式保存:
			im.save("./static/goodsimg/"+filename, 'jpeg')
			# 缩放到220*220:
			im.thumbnail((220, 220))
			# 把缩放后的图像用jpeg格式保存:
			im.save("./static/goodsimg/m_"+filename, 'jpeg')
			# 缩放到220*220:
			im.thumbnail((100, 100))
			# 把缩放后的图像用jpeg格式保存:
			im.save("./static/goodsimg/s_"+filename, 'jpeg')
			picname=filename
			b = True
		else:
			picname=oldpicname
		ob=Goods.objects.get(id=request.POST['id'])
		ob.typeid=request.POST['typeid']
		ob.goods=request.POST['goods']
		ob.company=request.POST['company']
		ob.descr=request.POST['descr']
		ob.price=request.POST['price']
		ob.picname=picname
		ob.state=request.POST['state']
		ob.store=request.POST['store']
		ob.num=request.POST['num']
		ob.clicknum=request.POST['clicknum']
		ob.addtime=request.POST['addtime']
		ob.save()
		context={'info':'修改成功'}
		if b:
			os.remove('./static/goodsimg/'+oldpicname )
			os.remove('./static/goodsimg/m_'+oldpicname )
			os.remove('./static/goodsimg/s_'+oldpicname )
	except:
		context={'info':'修该失败'}
		if b:
			os.remove('./static/goodsimg/'+picname)
			os.remove('./static/goodsimg/m_'+picname)
			os.remove('./static/goodsimg/s_'+picname)
	return render(request,"myadmin/goods/info.html",context)
