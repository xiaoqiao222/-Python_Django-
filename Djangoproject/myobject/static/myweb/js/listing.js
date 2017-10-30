// 鼠标移入事件
	$(function(){
		$('.two').mouseover(function(){
				$(this).addClass('two_bg');
				$(this).find('.b1').show();
				$(this).find('.jianjie').hide();
				console.log(1)
		})
		$('.two').mouseout(function(){
				$(this).removeClass('two_bg');
				$(this).find('.b1').hide();
				$(this).find('.jianjie').show();
				console.log(1)
		})
	})


///返回按钮和图片切换
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