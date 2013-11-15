define(['jquery', 'configs'], function($, configs) {
	var check_connectivity={
			is_internet_connected : function(){
//				return navigator.onLine;
				var dfd = new $.Deferred();
				$.get("/coco/check_connectivity/")
				.done(function(resp){
					return dfd.resolve();
				})
				.fail(function(resp){
					return dfd.reject(resp);
				});    
				return dfd.promise();
	        },
	}
	return check_connectivity;
});