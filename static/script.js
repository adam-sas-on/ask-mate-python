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

			page = {notification:null, colorBtn:null};
			forms = {f:null, title:null, question:null, answer:null, button:null};

		}

		return instance;
	}

	function setUp(args){
		page.notification = getByID("notification");

		forms.f = document.getElementsByTagName("form");
		if(forms.f.length > 0) forms.f = forms.f[0];

		var elem = document.getElementsByTagName("body");
		if(elem.length > 0) cfg.bgColor = elem[0].style.backgroundColor;


	}

	function getByID(id_str){
		var result;
		try {
			result = document.getElementById(id_str);
		}catch(e){result=null;}
		return result;
	}

	return {
		getInstance: function() {
			return new App_();
		},
		ini:function(){
			var inst2 = instance;
			if(instance == null) inst2 = new App_();


			return inst2;
		}
	}
})();

