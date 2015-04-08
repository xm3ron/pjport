$(document).ready(function() {
	
	//if submit button is clicked
	$('#submit').click(function () {		
		
		//Get the data from all the fields
		var name = $('input[name=name]');
		var email = $('input[name=email]');
		var regx = /^([a-z0-9_\-\.])+\@([a-z0-9_\-\.])+\.([a-z]{2,4})$/i;
		var comment = $('textarea[name=message]');
		var returnError = false;
		
		//Simple validation to make sure user entered something
		//Add your own error checking here with JS, but also do some error checking with PHP.
		//If error found, add hightlight class to the text field
		if (name.val()=='') {
			name.addClass('error');
			returnError = true;
		} else name.removeClass('error');
		
		if (email.val()=='') {
			email.addClass('error');
			returnError = true;
		} else email.removeClass('error');		
		
		if(!regx.test(email.val())){
          email.addClass('error');
          returnError = true;
		} else email.removeClass('error');
		
		
		if (comment.val()=='') {
			comment.addClass('error');
			returnError = true;
		} else comment.removeClass('error');
		
		// Highlight all error fields, then quit.
		if(returnError == true){
			return false;	
		}
		
		//organize the data
		
		var data = 'name=' + name.val() + '&email=' + email.val() + '&message='  + encodeURIComponent(comment.val());

		//disabled all the text fields
		$('.text').attr('disabled','true');
		
		//show the loading sign
		$('.loading').show();

        console.log("eccomi");
		
		//start the ajax
		$.ajax({
			//this is the php file that processes the data and sends email
            url: "http://api.piergiorgiofaraglia.it/sendmail",

			//GET method is used
			type: "POST",

			//pass the data			
			data: data,		

            dataType: 'jsonp',
			
			//Do not cache the page
			cache: false,
			
			//success
			success: function (html) {				
                console.log(html);
				//if contact.php returned 1/true (send mail success)
				if (html==1) {
				
					//show the success message
					$('.done').fadeIn('slow');
					
					$(".form").find('input[type=text], textarea').val("");
					
				//if contact.php returned 0/false (send mail failed)
				} else alert('Sorry, unexpected error. Please try again later.');				
			},
                      error: function(jqXHR, textStatus, errorThrown) 
                                    {
					//show the success message
					$('.done').fadeIn('slow');
					
					$(".form").find('input[type=text], textarea').val("");
                                                      console.log(errorThrown);
                                                                 }
		});
		
		//cancel the submit button default behaviours
		return false;
	});	
});	
