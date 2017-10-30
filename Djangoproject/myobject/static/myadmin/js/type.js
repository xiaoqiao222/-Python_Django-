<script type="text/javascript">
		$(function(){
			$.ajax({
				url: "{% url 'typeinsert' 0 %}",
				type: 'get',
				data: {},
				dataType: 'json',
				success:function(res){
					var data=res.data;
					for (var i = 0; i < data.length; i++) {
						$('<option value="'+data[i].id+'">'+data[i].name+'</option>').appendTo('select:last')
					 }
				},
				// error:function() {
				// 	alert('ajax加载失败')
				// }
			});
			$("select").live('change', function(){
				//获取选中的id号
				var id =$(this).val();
				$(this).nextAll().remove();
				$.ajax({
					url: '/typeinsert/'+id,
					type: 'get',
					dataType: 'json',
					data: {},
					success:function(res){
						if(res.data.length<1)
							return;
						var data=res.data;
						var select=$('<select><select>');
						for (var i = 0; i < data.length; i++) {
							$('<option value="'+data[i].id+'">'+data[i].name+'</option>').appendTo(select)
						};
						$("select :last").after(select)
					}
				})
				
			});
		})
</script>