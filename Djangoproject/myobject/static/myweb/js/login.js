<!-- 判断用户输入  -->
<script>
	var NameOk=false;
	var PaddOk=false;
	//丧失焦点事件
	$('input').focus(function(){
	//获取焦点时,给予提示信息
	var at = $(this).attr('readme');
	$(this).css('color','blue');
	$(this).css('border','1px solid green');
    })

	$('input[name=username]').blur(function(){
		//获取用户信息
		var v =$(this).val();
		var reg = /^[0-9]\d{10}$/;
		if(reg.test(v)){
			$(this).css('color','green');
			$(this).css('border','1px solid green');
			//修改全局变量
			NameOk = true;
		}else{
			$(this).css('color','red');
			$(this).css('border','1px solid red');
			//修改全局变量
			NameOk=false;
		}
	})
	$('input[name=password]').blur(function(){
		//获取用户信息
		var v =$(this).val();
		var reg=/^\w{6,18}$/;
		if(reg.test(v)){
			$(this).css('color','green');
			$(this).css('border','1px solid green');
			PassOk=true;
		}else{
			$(this).css('border','1px solid red');
			PassOk=false;
		}
	})
	
	//表单提交事件 submit
	$('form').submit(function(){
		//触发input 丧失焦点事件
		$('input').trigger('blur');

		//判断如果都正确
		if(NameOk && PassOk ){	
			return true;
		}
		//阻止默认行为
		return false;
	})
	var i = document.getElementById('session');
	console.log(i);
	window.onload = function(){
		if(i = '<a href="#" id = "session"></a>'){
			$('.users').hide()
			$('.ss').show()
		}else{
			$('.ss').hide()
			$('.users').show()
			
		}
	};
</script>