var App_ = (function(){
	var page, forms, cfg, instance;

	function App_(){
		if(instance==null){
			instance=Object.create(App_.prototype);

			cfg = {delegate:0, minMsg:10, bgColor:""};
			if( Element.prototype.addEventListener) cfg.delegate = 1;
			else if(Element.prototype.attachEvent ) cfg.delegate = 2;


			if(!Event.prototype.preventDefault){
				Event.prototype.preventDefault=function(){this.returnValue=false;};
			}
			if(!Event.prototype.stopPropagation){
				Event.prototype.stopPropagation=function(){this.cancelBubble=true;};
			}

			page = {notification:null, colorBtn:null, votes:null};
			forms = {f:null, title:null, question:null, answer:null, button:null};

		}

		return instance;
	}

	function setUp(args){
		page.notification = getByID("notification");
		/* page.colorBtn = getByID("..."); */

		forms.f = document.getElementsByTagName("form");
		if(forms.f.length > 0){
			forms.f = forms.f[0];
			getForm(args);
		} else forms.f = null;

		var elem = document.getElementsByTagName("body");
		if(elem.length > 0) cfg.bgColor = elem[0].style.backgroundColor;

		page.votes = document.getElementsByClassName("votes");
	}
	function getForm(args){
		var nodes = forms.f.getElementsByTagName("input");
		for(var i = nodes.length-1; i >= 0; i--){
			if(nodes[i].type == "submit") forms.button = nodes[i];
			else if(nodes[i].name == "title") forms.title = nodes[i];
		}

		nodes = forms.f.getElementsByTagName("textarea");
		if(nodes.length > 0){
			if(nodes[0].name == "question") forms.question = nodes[0];
			else if(nodes[0].name == "answer") forms.answer= nodes[0];
		}


	}

	function getByID(id_str){
		var result;
		try {
			result = document.getElementById(id_str);
		}catch(e){result=null;}
		return result;
	}

	function clearNode(node){
		while(node.firstChild) node.removeChild(node.firstChild);
	}

	function typeMessages(node, messages){
		if(!node) return;

		clearNode(node);
		for(var i = 0; i < messages.length; i++){
			node.appendChild(document.createTextNode(messages[i]) );
			node.appendChild(document.createElement("br") );
		}
	}

	function validate(e){
		var message = [];
		if(forms.title !== null && forms.title.value.length < 1) message.push("Please type any title for the question you want to share.");
		if(forms.question !== null && forms.question.value.length < 1) message.push("Question should not be empty when it is expected to be valuable - please type any question.");
		if(forms.answer !== null && forms.answer.value.length < cfg.minMsg) message.push("Please type any answer longer than " + cfg.minMsg);

		if(message.length > 0){
			var e2 = (e)?e:window.event;
			e2.preventDefault();

			typeMessages(page.notification, message);
			return false;
		}
		return true;
	}

	function take_vote(e){
		var e2 = (e)?e:window.event, linkClicked = e2.target || e2.srcElement;

		linkClicked.removeEventListener("click", take_vote);

		linkClicked.parentNode.removeChild(linkClicked);
		/* TODOs: e2.preventDefault(); send ajax and "ready state" function adds +1 or -1 to corresponding votes; */
	}

	function run(){

		if(cfg.delegate == 1){
			if(forms.f) forms.f.addEventListener("submit", validate, false);
			for(var i = page.votes.length - 1; i >= 0; i--) page.votes[i].addEventListener("click", take_vote);
		} else if(cfg.delegate == 2){
			if(forms.f) forms.f.attachEvent("onsubmit", validate);
		} else {
			if(forms.f) forms.f.onsubmit = validate;
		}
	}

	return {
		getInstance: function() {
			return new App_();
		},
		ini:function(){
			var inst2 = instance, values;
			if(instance == null) inst2 = new App_();

			values = Array().slice.call(arguments);
			setUp(values);
			run();
			return inst2;
		}
	}
})();

