var Profile = Backbone.Model.extend({
	urlRoot: '0.0.0.0:8080/user/',
	defaults: {
		mail: "a",
		login: "b",
		pswd: "c"
	}
});


function post_reg_temp() {
	var newMail = document.getElementById("form_mail").value;
	var newLogin = document.getElementById("form_login").value;
	var newPswd = document.getElementById("form_pswd").value;

	var newProfile = new Profile({
		mail: newMail,
		login: newLogin,
		pswd: newPswd
	});
var json_model = newProfile.toJSON();
alert(JSON.stringify(newProfile));
newProfile.save();
};

var Post = Backbone.Model.extend({
	urlRoot: 'http://0.0.0.0:8080/post/',
	defaults: {
		body: ""
	}
});



function post_reg() {
	var newBody = document.getElementById("form_mail").value;

	var newPost = new Post({
		body: newBody
	});
alert(JSON.stringify(newPost));
newPost.save();
};
