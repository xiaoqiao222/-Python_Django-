	//按钮点击订单状态修改
	detailStatChange()
	function detailStatChange(){
		//发送ajax请求
		function doajax(ostatus,oid){
			$.ajax({
				url: "/myadmin/detailstatus",
				type: 'GET',
				dataType: 'json',
				data:{'ostatus':ostatus,'oid':oid},
				error:function() {
					alert("ajax加载失败！");
				},
			})
		}
		var jVerify = $('#J_verify');
		var jCancel = $('#J_cancel');
		$('#J_verify').click(function(){
			var ostatus = $('input[name=statuschange]').val();
			ostatus = 1;
			$('.ostate').text('已发货');
			var oid = $('input[name=orderid]').val();
			$('input[name=statuschange]').val(ostatus);
			doajax(ostatus,oid);

		});
		$('#J_cancel').click(function(){
			var ostatus = $('input[name=statuschange]').val()
			ostatus = 3;
			$('.ostate').text('无效订单');
			var oid = $('input[name=orderid]').val();
			$('input[name=statuschange]').val(ostatus);
			doajax(ostatus,oid);

		});
	}
