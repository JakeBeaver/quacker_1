var bounce = "/accounts/login/"
var post = Backbone.Model.extend({urlRoot: 'http://0.0.0.0:8080/authpost/', defaults: {body:""}});
var comment = Backbone.Model.extend({urlRoot: 'http://0.0.0.0:8080/comments/', defaults: {body:"",post:0}});

var which = 0;
function count_comments(id)
{

//id = typeof id !== 'undefined' ? name : "";
    var adres = "http://0.0.0.0:8080/comments/" + id; 
    var self=this;
    console.log("adres: " + adres);
	var PostCollection = Backbone.Collection.extend({model: comment,url:adres});
	var comCol= new PostCollection();
    comCol.fetch({success:function(collection) { document.getElementById("post"+id).innerHTML = collection.length}})
}

function post_fetch(name) {
//  var temptemp = name;
name = typeof name !== 'undefined' ? name : "";

//alert('test:' + name + '\n' + temptemp);
    var adres = "http://0.0.0.0:8080/apifetch/"+ name;
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
			var postId = JSON.parse(postStr).id
			console.log(postStr); 
			console.log("postId: " + postId); 
			count_comments(postId);
				var post = document.createElement("div");
				body='<blockquote id="quote">'
				body+='<footer>'+username+'  <a href="#" onclick="post_fetch(\''+ username + '\')"><cite title="Source Title">profile</cite></a></footer>'
				body+='<p>'+postBody+'</p>'
				body+='<footer><a href="#" onclick="comment_fetch('+postId+')"><cite title="Source Title"> comments</cite></a> - <span id="post'+postId+'"></span></footer>'
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

function comment_list_fetch(postId) {
//  var temptemp = name;

//alert('test:' + name + '\n' + temptemp);
    var adres = "http://0.0.0.0:8080/comments/"+ postId;
	var PostCollection = Backbone.Collection.extend({model: comment,url:adres});
	var postCol = new PostCollection();
	postCol.fetch(
	{
    success: function() {
    		//document.getElementById("comments").innerHTML = "";
    		postCol.each(function(model){
			var postStr = JSON.stringify(model)
			var username = JSON.parse(postStr).owner
			var postBody = JSON.parse(postStr).body
			//console.log(postStr); 
			//console.log("postId: " + postId); 
			//count_comments(postId);
				var post = document.createElement("div");
				body='<blockquote id="quote">'
				body+='<footer>'+username+'  <a href="#" onclick="post_fetch(\''+ username + '\')"><cite title="Source Title">profile</cite></a></footer>'
				body+='<p>'+postBody+'</p>'
			    body+='</blockquote>'
				
				
			document.getElementById("comments").appendChild(post);
			post.innerHTML = body;
		});
    },
    error: function() {
        alert('I can\'t load comments');
    }
    
}
	);
};

function comment_fetch(postId) {
//  var temptemp = name;

//alert('test:' + name + '\n' + temptemp);
    var adres = "http://0.0.0.0:8080/apifetch/id="+ postId;
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
			var postId = JSON.parse(postStr).id
			console.log(postStr); 
			console.log("postId: " + postId); 
			//count_comments(postId);
				var post = document.createElement("div");
				body='<blockquote id="quote">'
				body+='<footer>'+username+'  <a href="#" onclick="post_fetch(\''+ username + '\')"><cite title="Source Title">profile</cite></a></footer>'
				body+='<p>'+postBody+'</p>'
				body+='<div id="comments"></div>'
				//form
				body+='<form class="form-horizontal">'
			    body+='<div class="form-group form-mg">'
				body+='<div class="col-sm-10">'
				body+='<textarea placeholder="Quack about this!" id="post_comment"class="form-control" rows="2"></textarea>'
			    body+='</div>'
				body+='<button onclick="comment_reg('+postId+');document.getElementById(\'sound\').play()" id="quack" type="button" class="btn btn-default navbar-btn">QUACK!</button>'
				body+='</div>'
				body+='</form>'
				//body+='<div id="comments"></div>'
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
	comment_list_fetch(postId)
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
document.getElementById("post_js").value = "";
};

function comment_reg(postId) {
	var newBody = document.getElementById("post_comment").value;

	var newPost = new comment({
		body: newBody,
		post: postId
	});
newPost.toJSON()
newPost.save({success:setTimeout(function(){comment_fetch(postId)}, 500)});
document.getElementById("post_comment").value = "";
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
				//console.log(userStr); 
				document.getElementById("user").innerHTML = name
				document.getElementById("profile_button").setAttribute("onclick","post_fetch('"+name+"')");
								var adres = "http://0.0.0.0:8080/apifetch/"+ x
				var PostCollection = Backbone.Collection.extend({model: post,url:adres});
				var postCol = new PostCollection();
				
				postCol.fetch({success:function(collection) {
				var post_count = collection.length;
				//console.log(collection.length);
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

