
(function(){
//
//Inicializamos el navbar
	$(document).ready(function(){
    	$('.sidenav').sidenav();
  	});

//Inicializamos el collapsible
	$(document).ready(function(){
        $('.collapsible').collapsible();
    });

//Inicializamos el formulario

    $(document).ready(function() {
        $('input#input_text, textarea#textarea2').characterCounter();
    });



	var TxtType = function(el, toRotate, period) {
        this.toRotate = toRotate;
        this.el = el;
        this.loopNum = 0;
        this.period = parseInt(period, 10) || 2000;
        this.txt = '';
        this.tick();
        this.isDeleting = false;
    };

    TxtType.prototype.tick = function() {
        var i = this.loopNum % this.toRotate.length;
        var fullTxt = this.toRotate[i];

        if (this.isDeleting) {
        this.txt = fullTxt.substring(0, this.txt.length - 1);
        } else {
        this.txt = fullTxt.substring(0, this.txt.length + 1);
        }

        this.el.innerHTML = '<span class="wrap">'+this.txt+'</span>';

        var that = this;
        var delta = 200 - Math.random() * 100;

        if (this.isDeleting) { delta /= 2; }

        if (!this.isDeleting && this.txt === fullTxt) {
        delta = this.period;
        this.isDeleting = true;
        } else if (this.isDeleting && this.txt === '') {
        this.isDeleting = false;
        this.loopNum++;
        delta = 500;
        }

        setTimeout(function() {
        that.tick();
        }, delta);
    };

    //inicializamos el tabs

    $(document).ready(function(){
        $('.tabs').tabs();
    });

    // funcion para texto que se escribe solo

	window.onload = function() {
        var elements = document.getElementsByClassName('typewrite');
        for (var i=0; i<elements.length; i++) {
            var toRotate = elements[i].getAttribute('data-type');
            var period = elements[i].getAttribute('data-period');
            if (toRotate) {
              new TxtType(elements[i], JSON.parse(toRotate), period);
            }
        }
        // INJECT CSS
        var css = document.createElement("style");
        css.type = "text/css";
        css.innerHTML = ".typewrite > .wrap { border-right: 0.08em solid #fff}";
        document.body.appendChild(css);
    };


    //funcion para el menu

		$(document).ready(function(){
		  		var altura = $('.menu').offset().top;
		  		// alert(altura);

		  		$(window).on('scroll', function(){
		  			if ($(window).scrollTop() > altura ){
		  				$('.menu').addClass("menu-fixed");
		  				$('.menu').addClass("z-depth-5");
		  			}else{
		  				$('.menu').removeClass("menu-fixed");
		  				$('.menu').removeClass("z-depth-5");
		  			}

		  		});
		  });



        



    /*    $(document).ready(function(){
            $('.parallax-window1').parallax({imageSrc: 'imagenes/paralax1.png'});
            $('.parallax-window2').parallax({imageSrc: 'imagenes/paralax2.png'});
            $('.parallax-window2').parallax({imageSrc: 'imagenes/paralax3.jpeg'});
        }());
*/



//funcion para el menu fixed
		  //var loguito = document.getElementById("logo");

/*		  $(document).ready(function(){
		  		var altura = $('.menu').offset().top;
		  		// alert(altura);

		  		$(window).on('scroll', function(){
		  			if ($(window).scrollTop() > altura ){
		  				$('.menu').addClass("menu-fixed");
		  				$('.menu').addClass("z-depth-2");
		  	//			loguito.setAttribute("src", "static/imagenes/logo-nav.png");

		  			}else{
		  				$('.menu').removeClass("menu-fixed");
		  				$('.menu').removeClass("z-depth-2");
		  	//			loguito.setAttribute("src", "static/imagenes/logo-navv.png");
		  			}

		  		});
		  });
*/
//    $(document).ready(function(){
        

  //      {% load staticfiles %}
          
        
    

/*    (function() {
        $('.parallax-window1').parallax({imageSrc: '../imagenes/paralax1.png'})
        $('.parallax-window2').parallax({imageSrc: '../imagenes/paralax2.png'})
        $('.parallax-window2').parallax({imageSrc: '../imagenes/paxalax3.jpeg'})
    }()); */

    


}());