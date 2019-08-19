var App_ = (function(){
	var instance;

	function App_(){
		if(instance==null){
			instance=Object.create(App_.prototype);

			if(!Event.prototype.preventDefault){
				Event.prototype.preventDefault=function(){this.returnValue=false;};
			}
			if(!Event.prototype.stopPropagation){
				Event.prototype.stopPropagation=function(){this.cancelBubble=true;};
			}

		}

		return instance;
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

