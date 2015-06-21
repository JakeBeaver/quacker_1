var post = Backbone.Model.extend({
	urlRoot: '../authpost/',
	defaults: {
		body: ""
	}
});

var PostCollection = Backbone.Collection.extend({
    model: post,
    url:"../authpost/",
     parse : function(res) 
     {
         console.log('response inside parse' + res);
        return res;
     }

});
var postCol = new PostCollection();

function post_fetch() {
	postCol.fetch({
    	success: function() {
        	alert(JSON.stringify(postCol));
    	},
    	error: function() {
        	alert('Failed to fetch!');
    	}
	}
	
	);
};
