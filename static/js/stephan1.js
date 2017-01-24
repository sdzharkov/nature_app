$(document).ready(function() {



    jQuery(function($) {
        $("body").mainFm({

            /* Set the opening page.
            leave it blank value if you need to show the home page as a opening page*/
            currentPage: "!home",

            /* FlexSlider slideshow speed */
            slideshowSpeed: 5000

        });
    });




    //.parallax(xPosition, speedFactor, outerHeight) options:
    //xPosition - Horizontal position of the element
    //inertia - speed to move relative to vertical scroll. Example: 0.1 is one tenth the speed of scrolling, 2 is twice the speed of scrolling
    //outerHeight (true/false) - Whether or not jQuery should use it's outerHeight option to determine when a section is in the viewport
    $('.parallax').each(function() {
        $(this).parallax("50%", 0.4, true);
    });



    /* Initialize  - isotope Portfolio */

    $(function() {

        var $container = $('#gallery_isotope_1');
        var $optionSets = $('#options .option-set'),
            $optionLinks = $optionSets.find('a');

        $optionLinks.click(function() {
            var $this = $(this);

            // don't proceed if already selected
            if ($this.hasClass('selected')) {
                return false;
            }
            var $optionSet = $this.parents('.option-set');
            $optionSet.find('.selected').removeClass('selected');
            $this.addClass('selected');

            // make option object dynamically, i.e. { filter: '.my-filter-class' }
            var options = {},
                key = $optionSet.attr('data-option-key'),
                value = $this.attr('data-option-value');
            // parse 'false' as false boolean
            value = value === 'false' ? false : value;
            options[key] = value;
            if (key === 'layoutMode' && typeof changeLayoutMode === 'function') {
                // changes in layout modes need extra logic
                changeLayoutMode($this, options)
            } else {
                // otherwise, apply new options
                $container.isotope(options);
            }

            return false;
        });

    });

    // Portfolio isotope gallery initailize

    $('#gallery_isotope_1').isotope({
        itemSelector: '.item',
        layoutMode: 'fitRows'
    });


    // Portfolio isotope gallery categories Filter initialize
    jQuery(function($) {
        $('.portfolioPage').detailPage({
            filter: ".filter_options"
        })
    });


    // Email submit action
    // $("#email_submit").click(function() {

    // 	$('#reply_message').removeClass();
    // 	$('#reply_message').html('')
    // 	var regEx = "";

    // 	// validate Name
    // 	var name = $("input#name").val();
    // 	regEx=/^[A-Za-z .'-]+$/;
    // 	if (name == "" || name == "Name"  || !regEx.test(name)) {
    // 		$("input#name").val('');
    // 		$("input#name").focus();
    // 		return false;
    // 	}

    // 	// validate Email
    // 	var email = $("input#email").val();
    // 	regEx=/^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$/;
    // 	if (email == "" || email == "Email" || !regEx.test(email)) {
    // 		$("input#email").val('');
    // 		$("input#email").focus();
    // 		return false;
    // 	}

    // 	// validate comment
    // 	var comments = $("textarea#comments").val();
    // 	if (comments == "" || comments == "Comments..." || comments.length < 2) {
    // 		$("textarea#comments").val('');
    // 		$("textarea#comments").focus();
    // 		return false;
    // 	}

    // 	var dataString = 'name='+ $("input#name").val() + '&email=' + $("input#email").val() + '&comments=' + $("textarea#comments").val();
    // 	$('#reply_message').addClass('email_loading');

    // 	// Send form data to mailer.php
    // 	$.ajax({
    // 		type: "POST",
    // 		url: "mailer.php",
    // 		data: dataString,
    // 		success: function() {
    // 			$('#reply_message').removeClass('email_loading');
    // 			$('#reply_message').addClass('list3');
    // 			$('#reply_message').html("Mail sent sucessfully")
    // 			.hide()
    // 			.fadeIn(1500);
    // 				}
    // 			});
    // 	return false;

    // });


});
