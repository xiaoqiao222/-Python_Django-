from django.conf.urls import url
from . import views,viewusers,viewsorders

urlpatterns = [
    # 首页
    url(r'^$',views.index,name='index'),
    #列表页
    url(r'^listing$',views.listing,name='listing'),
    url(r'^listing(?P<uid>[0-9]+)/$',views.listing,name='listing'),
    #详情页
    url(r'^details(?P<uid>[0-9]+)/$',views.details,name='details'),
    #列登页
    url(r'^login$',viewusers.login,name='login'),
    url(r'^dologin$',viewusers.dologin,name='dologin'),
    url(r'^logindel$',viewusers.logindel,name='logindel'),
    #验证码
    url(r'^logincodes$',viewusers.logincodes,name='logincodes'),
         #注册页
    url(r'^register$',viewusers.register,name='register'),
    url(r'^registerinsert$',viewusers.registerinsert,name='registerinsert'),
    #--------个人中心-------------------
    url(r'^personalCore$', viewusers.personalCore,name='personalCore'), #个人中心信息
    url(r'^personalCores$', viewusers.personalCores,name='personalCores'), #个人订单信息
    url(r'^personaledit$', viewusers.personaledit,name='personaledit'), #个人订单信息
    url(r'^personalupdate(?P<uid>[0-9]+)/$', viewusers.personalupdate,name='personalupdate'), #个人执行信息
    url(r'^personaledita/(?P<cid>[0-9]+)$', viewusers.personaledita,name='personaledita'), #执行确认订单
    url(r'^personaledits/(?P<cid>[0-9]+)$', viewusers.personaledits,name='personaledits'), #取消订单
    #购物车页
    url(r'^cartindex$',viewsorders.cartindex,name='cartindex'),#浏览
    url(r'^cartadd/(?P<cid>[0-9]+)$', viewsorders.cartadd,name='cartadd'), #添加购物车
    url(r'^cartdel/(?P<cid>[0-9]+)$', viewsorders.cartdel,name='cartdel'), #从购物车中删除一个商品
    url(r'^cartclear$', viewsorders.cartclear,name='cartclear'), #清空购物车
    url(r'^cartchange$', viewsorders.cartchange,name='cartchange'), #更改购物车中商品数量

# #订单路由-----------------------------------------------------------

    url(r'^ordersform$', viewsorders.ordersform,name='ordersform'), #订单表单
    url(r'^ordersconfirm$', viewsorders.ordersconfirm,name='ordersconfirm'), #订单确认
    url(r'^ordersinsert$', viewsorders.ordersinsert,name='ordersinsert'), #执行订单添加
 
    url(r'^ordersinfo$', viewsorders.ordersinfo,name='ordersinfo'), #订单信息

]
