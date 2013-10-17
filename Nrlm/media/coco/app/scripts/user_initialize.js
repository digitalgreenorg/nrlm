define([
    'auth',
    'offline_utils',
    'configs',
    'jquery',
    'form_field_validator',
  ], function(Auth, Offline, all_configs){
    
    var run = function(){
        $.validator.addMethod('allowedChar',
            validateUniCodeChars, 'Enter a string.'
        );
        $.validator.addMethod('validateDate',
            validateDate, 'Enter the date in the form of YYYY-MM-DD.'
        );
        $.validator.addMethod('validateTime',
            validateTime, 'Enter the time in the form of HH:MM. Use 24 hour format'
        );
		$.validator.addMethod('timeOrder',
            timeOrder, 'End time should be later than start time'
        );
		$.validator.addMethod('dateOrder',
            dateOrder, 'End date should be later than start date'
        );
		$.validator.addMethod('datecheck',
	            datecheck, 'End date should be later than start date'
	        );
		$.validator.addMethod('validateYear',
				validateYear, 'End date should be later than start date'
	        );
/*		$.validator.addMethod('CheckDates',function(i,element) 
				 {
		      return IsValidDate(element);

		 }, "Please enter a correct date");
		$.validator.addClassRules({
		     dateRequired: { required:true, CheckDates:true}
		 });
*/        reset_database_check();
    } 
    
  /*  function IsValidDate(_element)
    {
        // just a hack function to take an element, get the drop down fields within it with a particular class name ending with day /month/ year and perform a basic date time test
        var $dateFields =  $("#" + _element.id).parent();

        day = 28;
        month = $dateFields.children(".dateRequired:[name$='month']");
        year = $dateFields.children(".dateRequired:[name$='year']");

        var $newDate = month.val() + " " + day.val() + " " + year.val();
        consol.log($newDate)
        var scratch = new Date($newDate );

        if (scratch.toString() == "NaN" || scratch.toString() == "Invalid Date") 
        {
            return false;
        } else {
            return true;
        }
    } */
     
    function reset_database_check(){
        if(!all_configs.misc.onLogin)
            return;
        Auth.check_login()
            .done(function(){
                if(!navigator.onLine)
                    return;
                all_configs.misc.onLogin(Offline, Auth);    
            });
    }
    
    function validateUniCodeChars(value) {
    	if(value) {
    		var alphabetCharset = /^[a-zA-Z ]+$/;
    		var strictUniCodeChars = /.*[^\\x20-\\x7E].*/;
    		if(alphabetCharset.test(value)) {
    			return true;
    		} 
    		if(strictUniCodeChars.test(value)) {
    			return true;
    		} else {
    			return false;
    		}
    	} else {
    		return true;
    	}
    }

    function validateDate(value) {
    	var check = false;
    	var re = /^\d{4}\-\d{1,2}\-\d{1,2}$/;
    	if( re.test(value)) {
    		var adata = value.split('-');
    		var year = parseInt(adata[0],10);
    		var month = parseInt(adata[1],10);
    		var day = parseInt(adata[2],10);
    		var xdata = new Date(year,month-1,day);
    		if ( ( xdata.getFullYear() === year ) && ( xdata.getMonth() === month - 1 ) && ( xdata.getDate() === day ) ){
    			check = true;
    		} else {
    			check = false;
    		}
    	} else {
    		check = false;
    	}
    	return check;
    }

    function validateTime(value) {
    	var check = false;
    	var adata = value.split(':');
    	var hours = parseInt(adata[0],10);
    	var minutes = parseInt(adata[1],10);
    	if((hours > 24) && (minutes > 60)) {
    		check=false;
    	} else {
    		check = true;
    	}
    	return check;
    }

    function datecheck(value, element, options){
    	var check = false;
    	var mon = $('#'+options.month).val();
    	var year = value;
    	var mapping = {Jan : 1 , Feb : 2, Mar : 3, Apr : 4, May : 5, Jun : 6, Jul : 7, Aug : 8, Sep : 9, Oct : 10, Nov : 11, Dec : 12};
    	var month=mapping[mon]-1;
    	var entry_date=new Date(year,month,1);
    	var myDate=new Date();
    	if (myDate>entry_date)
    	  {
    	  check=true;
    	  }
    	else
    	  {
    	  check=false;
    	  }
    	return check;
    }
 
    function validateYear(value){
    	var check = false;
    	var fyyear=value;
    	var now = new Date();
    	var currentyear= now.getFullYear();
    	if (currentyear==fyyear-1)
    		check=true;
    	else
    		check=false;
    	return check;
    }
    
	function dateOrder(value, element, options){
		var check = false;
		var start = $('#'+options.video_production_start_date).val();
		//console.log("START DATE = " + start + ' END = ' + value);

		startDate = start.split('-');
		endDate = value.split('-');
		
		if(endDate[0]>startDate[0] || String(endDate).length === 0){
			check = true;
		}
		else if (endDate[0] === startDate[0]){
			if(endDate[1]>startDate[1]){
				check = true;
			}
			else if(endDate[1] === startDate[1]){
				if(endDate[2] >= startDate[2]){
					check = true;
				}
			}
		}	
		return check;	
	}
	

	function timeOrder(value, element, options){
		var check = false;
		var start = $('#'+options.start_time).val();
		var end = value;
		if(start < end){
			check = true;
		}
		else{
			check = false;
		}
		return check;
	}
    return {
        run: run
    };


});
