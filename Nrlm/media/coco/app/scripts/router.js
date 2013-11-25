// Filename: router.js
define([
  'jquery',
  'underscore',
  'backbone',
  'views/app_layout',
  'configs',
  'auth'
], function(jquery, underscore, backbone, AppLayout, configs, Auth){
  
    var AppRouter = Backbone.Router.extend({
        routes: {
            "": "home",
            ":entity/list": "list",
            ":entity/add": "add",
            ":entity/edit/:id": "edit",
            "login": "login"
        },
        home: function() {
            this.check_login_wrapper()
                .done(function(){
                    AppLayout.render_home_view();
                });
        },
        list: function(entity_name) {
        	if(this.check_url_wrapper(entity_name) && this.check_list_url_remove_wrapper(entity_name)){
        		this.check_login_wrapper()
                .done(function(){
                    AppLayout.render_list_view(entity_name);
                });
        	}
        	else{
        		alert("You are not authorized to view this page. Please contact your administrator.");
        	}
        },
        add: function(entity_name) {
        	if(this.check_url_wrapper(entity_name) && this.check_add_url_remove_wrapper(entity_name)){
        		this.check_login_wrapper()
                .done(function(){
                    AppLayout.render_add_edit_view(entity_name, null);
                });
        	}
        	else{
        		alert("You are not authorized to view this page. Please contact your administrator.");
        	}
            
        },
        edit: function(entity_name, id) {
        	if(this.check_url_wrapper(entity_name) && this.check_add_url_remove_wrapper(entity_name)){
        		this.check_login_wrapper()
                .done(function(){
                    AppLayout.render_add_edit_view(entity_name, parseInt(id));
                });
        	}
        	else{
        		alert("You are not authorized to view this page. Please contact your administrator.");
        	}
        },
        login: function(){
            AppLayout.render_login();
        },
        check_url_wrapper: function(entity_name){
        	if(typeof configs[entity_name] == 'undefined'){
        		return false;
        	}
        	else{
        		return true;
        	}
        },
        check_list_url_remove_wrapper: function(entity_name){
            var listing = false;
            if(configs[entity_name].dashboard_display)
            {
            	listing = configs[entity_name].dashboard_display.listing;
            }
            return listing;
        },
        check_add_url_remove_wrapper: function(entity_name){
            var add = true;
            var enable_months = [];
            if(configs[entity_name].dashboard_display)
            {
                add = configs[entity_name].dashboard_display.add;
                enable_months = configs[entity_name].dashboard_display.enable_months;
            }
            if(typeof enable_months != 'undefined'){
            	var d = new Date();
                n = d.getMonth();
                n=n+1;
                res=$.inArray(n, enable_months);
                if(res === -1){
                	add=false;
                }
            }
            return add;
        },        
        check_login_wrapper: function(){
            var dfd = new $.Deferred();
            console.log("Authenticating before routing");
            Auth.check_login()
                .fail(function(err){
                    console.log("UnAuthenticated");
                    dfd.reject();
                    window.Router.navigate("login",{
                        trigger:true
                    });
                })
                .done(function(){
                    console.log("Authenticated");
                    dfd.resolve();
                });
            return dfd;    
        }

    });
  
  var initialize = function(){
    console.log("Initializing router");
    var app_router = new AppRouter();
    window.Router = app_router;
    Backbone.history.start();
  };
  
  return {
    initialize: initialize
  };
});