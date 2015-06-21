var bounce = "/accounts/login/"

var post = Backbone.Model.extend({urlRoot: 'http://0.0.0.0:8080/authpost/', defaults: {body:""}});

function post_fetch(name="") {
    var adres = "http://0.0.0.0:8080/apifetch/"+ name
	var PostCollection = Backbone.Collection.extend({model: post,url:adres});
	var postCol = new PostCollection();
	postCol.fetch(
	{
    success: function() {
    		document.getElementById("posts").innerHTML = "";
    		postCol.each(function(model){
			var postStr = JSON.stringify(model)
			var username = JSON.parse(postStr).owner
			var postBody = JSON.parse(postStr).body
			//console.log(postStr); 
				var post = document.createElement("div");
				body='<blockquote id="quote">'
				body+='<footer>'+username+'  <a href="#" onclick="post_fetch(\''+ username + '\')"><cite title="Source Title">profile</cite></a></footer>'
				body+='<p>'+postBody+'</p>'
				body+='</blockquote>'
				
				
			document.getElementById("posts").appendChild(post);
			post.innerHTML = body;
		});
    },
    error: function() {
        alert('I can\'t load '+ name +'\'s posts');
    }
}
	);
};



function fetch_now() {
	var fetchThis = document.getElementById("fetch_js").value;
	post_fetch(fetchThis);
}
function post_reg() {
	var newBody = document.getElementById("post_js").value;

	var newPost = new post({
		body: newBody
	});
newPost.toJSON()
newPost.save({success:setTimeout(function(){post_fetch()}, 500)});
document.getElementById("post_js").value = ""
;
};

var user = Backbone.Model.extend({urlRoot: 'http://0.0.0.0:8080/user/'});
function whois() {
    var adres = "http://0.0.0.0:8080/user/"
	var userCollection = Backbone.Collection.extend({model: post,url:adres});
	var userCol = new userCollection();
	userCol.fetch(
	{
    success: function() {
    	if(userCol.isEmpty()){
    		window.location.replace(bounce);
    	}
    	else {
    		userCol.each(function(model){
				var userStr = JSON.stringify(model)
				var name = JSON.parse(userStr).username
				var x = name
				console.log(userStr); 
				document.getElementById("user").innerHTML = name
				document.getElementById("profile_button").setAttribute("onclick","post_fetch('"+name+"')");
								var adres = "http://0.0.0.0:8080/apifetch/"+ x
				var PostCollection = Backbone.Collection.extend({model: post,url:adres});
				var postCol = new PostCollection();
				
				postCol.fetch({success:function(collection) {
				var post_count = collection.length;
				console.log(collection.length);
				document.getElementById("post_count_js").innerHTML = post_count;
				}})

		});}
    },
    error: function() {
        alert('I can\'t load '+ name +'\'s posts');
    }
}
	);
};

