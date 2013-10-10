define([],
function() {
    
    /*
    var dummy_config = {
        entity_name : 
        //string = key of this object in all_config, name of objectstore in IDB
        //for - accessing this object 
        
        'rest_api_url': '/coco/api/v1/village/',
        //string - the rest url for this entity
    
        'dashboard_display': {
            listing: false,         //whether to provide listing option for this entity on dashboard
            add: false              //whether to provide add option for this entity on dashboard
        },
    
        -----------------------------------Listing configs---------------------------------
        page_header: 'Village',  
        //string = The name that needs to shown in headers 

        list_table_header_template: 'village_table_template',  
        //HTML template - The id of template used as coloumn headers in list page

        list_table_row_template: 'village_list_item_template',  
        //HTML template - The id of template used to create rows of list table. 
        //This template is passed the model json.
        -----------------------------------------------------------------------------------
    
        ----------------------------------Form configs-------------------------------------
        foreign_entities: {
            f_entity_name:{         //the entity_name of foreign element
                attribute_name:{    //the attribute name of this foreign element in json
                    
                    'placeholder': 'string - the id of element in form's html where the dropdown of this f_entity is inserted',
                    
                    'name_field': 'string - the attribute name in f_entity's json which needs to be shown in its dropdown',
                    
                    'dependency': [{    // whether this elements's dropdown depends on value of other form elements
                        'source_form_element': 'village',   // attribute name of source element in json
                        'dep_attr': 'village'   //the attribute name in json of dependent f_entity which refers to source f_entity
                        'src_attr' : //to compare dep_attr of dependent element with a particular attribute in source f_entity
                    }],
                    
                    'filter': { //whether to filter the objects of foreign entity before rendering into dropdown
                        attr: 'group',  //the attribute name in f_entity's json to filter on
                        value: null     //desired value of the attr
                    },
    
                    id_field: "person_id", // the name of id field for this f_entity in denormalised json                         
                }
            },
    
            f_entity_name:{         //the entity_name of foreign element
                attribute_name:{    //the attribute name of this foreign element in json
                    
                    'dependency': [{    // whether this elements's dropdown depends on value of other form elements
                        'source_form_element': 'village',   // attribute name of source element in json
                        'dep_attr': 'village'   //the attribute name in json of dependent f_entity which refers to source f_entity
                    }],

                    id_field: "person_id", // the name of id field for this f_entity in denormalised json     

                    //would not use options template to render its objects - would use the specfied template    
                    // won't be denormalised, wud be converted offline to online, 
                    //any field to be denormalised or converted offline to online can be declared - 
                    //this shd be clubbed and put as foreign entity of expanded.   
                    'expanded': { 
                        template: 'person_pma_template', // the template to use instead of options
                        placeholder: 'pmas',    // the id of placeholder in form's HTML
                        TODO: the following two should be merged and converted to same format as foreign_entities
                        denormalize: { // any field in expanded template to be denormalised     
                            "expressed_adoption_video": {
                                name_field: 'title' //used as key for name in denormalised object
                            }
                        },
                        foreign_fields: { // any more field in expanded template for offline to online conv
                            "expressed_adoption_video": {
                                entity_name: "video"  //the entity_name for this f_entity element
                            }
                        },
                        extra_fields: ["expressed_question", "interested", "expressed_adoption_video"]
                    }
                }
            }
        },    
        //object - describes the foreign keys in the json of this entity's model.
        //To convert between online offline namespaces, denormalize-normalize json    
    
        inline: {
            'entity': 'person',     //entity name of inline
    
            'default_num_rows': 10,         //default num of rows to show
    
            "template": "person_inline",    //id of template used to render inline
            //Include any jquery validation desired inside html of rows 
            //TODO: need to explain the <%index%> tags required in inlines
    
            "foreign_attribute": {
                'host_attribute': ["id", "group_name"],
                'inline_attribute': "group"
            },
            "header": "person_inline_header",
            'borrow_attributes': [{
                'host_attribute': 'village',
                'inline_attribute': 'village'
            }]
        },      
        //object - describes inlines to be included in this entity's form

        bulk:{},     
        //object - if multiple objects of this entity type can be saved through its add form, describe configs of object 
        ------------------------------------------------------------------------------------
    }
    */
    
    // //This template would be passed the json of inline model and shall produce the desired row
//     TODO: maybe instead of relying on users to use templating lang we should fill the rows ourselves in js code, like we are doing in form!

    var person_configs = {
    	'entity_name' : 'person',
    	'rest_api_url' : '/api/v1/Persons/',
    	'dashboard_display' : {
    		listing : true,
    		add : true
    	},
    	'page_header' : 'Person',
    	'list_table_header_template' : 'person_table_template',
    	'list_table_row_template': 'person_list_item_template',
    	'add_template_name': 'person_add_edit_template',
        'edit_template_name': 'person_add_edit_template',
        'foreign_entities': {
        	'state':{
        		'state':{
        			'placeholder': 'id_state',
        			'name_field': 'name'
        		},
        	},
        },
        'sort_field': 'name',
        'form_field_validation': {
        	ignore: [],
        	rules: {
        		name: {
        			required: true,
        			minlength: 2,
                    maxlength: 100,
        		},
        	},
        	messages: {
				person_name: {
					required: 'Person name is required',
					minlength: 'Person name  should contain at least 2 characters',
					maxlength: 'Person Name should contain at most 100 characters',
				},
        	},
        
        highlight: function(element, errorClass, validClass) {
            $(element)
                .parent('div')
                .parent('div')
                .addClass("error");

        },
        unhighlight: function(element, errorClass, validClass) {
            $(element)
                .parent('div')
                .parent('div')
                .removeClass("error");

        },
        errorElement: "span",
        errorClass: "help-inline"
        }
    };
    
	var state_configs = {
        'page_header': 'State',
        'list_table_header_template': 'state_table_template', 
        'list_table_row_template': 'state_list_item_template',
    	'add_template_name': 'state_add_edit_template',
        'edit_template_name': 'state_add_edit_template',
        'rest_api_url': '/api/v1/State/',
        'entity_name': 'state',
        'dashboard_display': {
            listing: true,
            add: true
        },
        'sort_field': 'name'
    };


        var misc = {
        download_chunk_size: 2000,
        background_download_interval: 5 * 60 * 1000,
        inc_download_url: "/get_log/",
        reset_database_check_url: '/coco/reset_database_check/',
        
    };

    return {
        state: state_configs,
        person: person_configs,
        misc:misc
    }

});
