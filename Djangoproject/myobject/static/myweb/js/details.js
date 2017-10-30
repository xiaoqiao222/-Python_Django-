
	/*购物车移动事件
	移入事件*/
	$('#gw').mouseover(function(){
		$('.cart').css('display','block')
	});
	//移出事件
	$('#gw').mouseout(function(){
		$('.cart').css('display','none')
	});
	/*end 购物车事件*/
	
	// 图片变换
	//给li绑定单击事件
	$('#uing li').click(function(){
		//获取图片的src属性
		var s = $(this).find('img').attr('src');
		//修改图片的src属性
		$('.sing img').attr('src',s);
		return false;
	})
	// end 图片变换
	// 加减
	var i=1;
	$('.btjia').click(function(){
		var i=$("input[name=m]").val();
		i++;
		$("input[name=m]").val(i);
			
	});
	$('.btjian').click(function(){
		var i=$("input[name=m]").val();
		i--;
		if (i<=1) {i=1};
		$("input[name=m]").val(i)
	});
	//返回按钮和图片切换
	$('#card').click(function(){
		ss();
		$("#card img").slideDown();
		var sTop=$(document).scrollTop();
		if (sTop<100) {
			$("#card img").slideUp();
			
		}else{
			fei();
		}
		
	})
	$('#card').dblclick(function(){
		$("#card").slideUp();
	});
	function  ss(){
		$('body').animate({scrollTop:0+'px'},1000);
	}
	//切换图片事件方法
	var fei=function(){
		var i = 2;
	    setInterval(function(){
		i++;
		//检测是否越界
		if(i > 3){
			i = 2;
		}
		imgs.src = "{% static 'shop/img/fei/fei'+i+'.jpg'%}";
	},1000)
	}
		// 在线帮助
	$('.zai').popover('hide')
	$('.zai').click(function(){
		$('.zai').popover('show')
	});