/*头部事件浮动*/
	$(window).scroll(InitScro);
	InitScro();
	function InitScro(){
		var sTop=$(document).scrollTop();
		var t=$('.nhear').offset().top;
		
	if(sTop>=t){
		$('.user').show();
		$('#gws img').show();
		$('#gws span').show();
		$('.shou').css('color', '#fff');
		$('.quan').css('color', '#fff');
		$('.nhear nav').addClass('navbar-fixed-top').css({
			background: '#000',
			color:'#fff'
		});
		
	}else{
		$('.nhear nav').removeClass('navbar-fixed-top').css({
			background: '#D9D8D7',
			color:'#000'
		});;
		$('.user').hide();
		$('#gws img').hide();
		$('#gws span').hide();
		$('.shou').css('color', '#000');
		$('.quan').css('color', '#000');
	}
	}
	/*购物车移动事件
	移入事件*/
	$('#gw').mouseover(function(){
		$('.cart').css('display','block')
	});
	//移出事件
	$('#gw ').mouseout(function(){
		$('.cart').css('display','none')
	});
	/*end 购物车事件*/
	/*内容移入事件*/
	// 鼠标移入事件
	$('.re').mouseover(function(){
		$(this).addClass('re_bg');
		$(this).find('.b1').show();
		$(this).find('.jianjie').hide();
	})
		
	// 鼠标移出事件
	$('.re').mouseout(function(){
		$(this).removeClass('re_bg');
		$(this).find('.b1').hide();
		$(this).find('.jianjie').show();
	})

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
		imgs.src = "{% static '/myweb/img/fei/fei'+i+'.jpg'%}";
	},1000)
	}
		// 在线帮助
	$('.zai').hide()
	$('.zai').click(function(){
		$('.zai').popover('show')
	});