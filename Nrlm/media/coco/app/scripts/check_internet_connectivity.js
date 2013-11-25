define(['jquery'], function($) {
	var check_connectivity={
			is_internet_connected : function(){
//				return navigator.onLine;
				return $.get("/coco/check_connectivity/");
//				var check=false;
//				var dfd = new $.Deferred();
//				//var $obj= $.get("/coco/check_connectivity/");
//				var $obj=$.get({
//					url: "/coco/check_connectivity/",
//					cache: false
//				});
//				$obj.done(function(resp){
////					alert("Connectivity true");
////					check=true;
//					return dfd.resolve();
//				})
//				$obj.fail(function(resp){
////					alert("connectivity false");
////					check=false;
//					return dfd.reject(resp);
//				})
////				alert(check);
//				return dfd.promise();
	        },
	}
	return check_connectivity;
});