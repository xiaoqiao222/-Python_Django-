from django.conf.urls import url
from django.contrib import admin
from . import views,viewsgoods,viewsorders

urlpatterns = [
    # 后台首页
    url(r'^$',views.index,name='myadmin_index'),
 	#登陆
    url(r'^login$',views.login,name='myadmin_login'),
    url(r'^dologin$',views.dologin,name='myadmin_dologin'),
    url(r'^logout$',views.logout,name='myadmin_logout'),
    #验证码
    url(r'^logincode$',views.logincode,name='logincode'),
    # 后台用户管理
    url(r'^users/(?P<pIndex>[0-9]*)/$',views.usersindex,name='myadmin_usersindex'),
    url(r'^usersadd$',views.usersadd,name='myadmin_usersadd'),
    url(r'^usersinsert$',views.usersinsert,name='myadmin_usersinsert'),
    url(r'^usersdel(?P<uid>[0-9]+)/del$',views.usersdel,name='myadmin_usersdel'),
    url(r'^usersedit(?P<uid>[0-9]+)/edit$',views.usersedit,name='myadmin_usersedit'),
    url(r'^usersupdate(?P<uid>[0-9]+)/$',views.usersupdate,name='myadmin_usersupdate'),
#-------------------------------------------------------------------
    #后台商品类型表
    url(r'^type$',viewsgoods.typeindex,name='myadmin_typeindex'),
    # url(r'^typeadd$',viewsgoods.typeadd,name='myadmin_typeadd'),
    # url(r'^typeadds$',viewsgoods.typeadds,name='myadmin_typeadds'),
    # url(r'^typeinsert$',viewsgoods.typeinsert,name='myadmin_typeinsert'),
    url(r'^typeaddss(?P<uid>[0-9]+)$',viewsgoods.typeaddss,name='myadmin_typeaddss'),
    url(r'^typeinserts$',viewsgoods.typeinserts,name='myadmin_typeinserts'),
    url(r'^typedel(?P<uid>[0-9]+)/del$',viewsgoods.typedel,name='myadmin_typedel'),
    url(r'^typeedit(?P<uid>[0-9]+)/edit$',viewsgoods.typeedit,name='myadmin_typeedit'),
   # url(r'^typeedits$',viewsgoods.typeedits,name='myadmin_typeedits'),
    url(r'^typeupdate(?P<uid>[0-9]+)/$',viewsgoods.typeupdate,name='myadmin_typeupdate'),

    #后台商品详情信息表管理
    url(r'^goods/(?P<pIndex>[0-9]*)/$',viewsgoods.goodsindex,name='myadmin_goodsindex'),
    url(r'^goodsadd$',viewsgoods.goodsadd,name='myadmin_goodsadd'),
    url(r'^goodsadds/(?P<uid>[0-9]+)$',viewsgoods.goodsadds,name='myadmin_goodsadds'),
    url(r'^goodsinsert$',viewsgoods.goodsinsert,name='myadmin_goodsinsert'),
    url(r'^goodsdel(?P<uid>[0-9]+)/del$',viewsgoods.goodsdel,name='myadmin_goodsdel'),
    url(r'^goodsedit(?P<uid>[0-9]+)/edit$',viewsgoods.goodsedit,name='myadmin_goodsedit'),
    url(r'^goodsupdate$',viewsgoods.goodsupdate,name='myadmin_goodsupdate'),
#----------------------------订单表----------
 #后台商品订单管理
    url(r'^orders/(?P<pIndex>[0-9]*)/$',viewsorders.ordersindex,name='myadmin_ordersindex'),
    # url(r'^ordersadd$',viewsorders.ordersadd,name='myadmin_ordersadd'),
    # url(r'^ordersinsert$',viewsorders.ordersinsert,name='myadmin_ordersinsert'),
    # url(r'^ordersdel(?P<uid>[0-9]+)/del$',viewsorders.ordersdel,name='myadmin_ordersdel'),
    url(r'^ordersedit(?P<uid>[0-9]+)/edit$',viewsorders.ordersedit,name='myadmin_ordersedit'),
    url(r'^ordersupdate/(?P<uid>[0-9]+)$',viewsorders.ordersupdate,name='myadmin_ordersupdate'),
 #后台商品订单详情信息管理
    url(r'^detail/(?P<pid>[0-9]*)$',viewsorders.detailindex,name='myadmin_detailindex'),
    # url(r'^detailadd$',viewsorders.detailadd,name='myadmin_detailadd'),
    # url(r'^detailinsert$',viewsorders.detailinsert,name='myadmin_detailinsert'),
    # url(r'^detaildel(?P<uid>[0-9]+)/del$',viewsorders.detaildel,name='myadmin_detaildel'),
    url(r'^detailedit(?P<uid>[0-9]+)/edit$',viewsorders.detailedit,name='myadmin_detailedit'),
    url(r'^detailupdate(?P<uid>[0-9]+)/$',viewsorders.detailupdate,name='myadmin_detailupdate'),
]
