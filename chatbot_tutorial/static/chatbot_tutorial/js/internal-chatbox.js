
// Function to simply format the text in the right way. May end up being more complicated when you have MCQs, etc.
function generate_formatted_chat_message(data){
	console.log(data)
	if(data.type == 'text'){
		message_text = '<span class="message-text">' + data.text + '</span>'
		return message_text;
	}
	console.log("invalid data format");
	return "";
}

// Function that adds a message to the chat window
function add_message_to_chat(data, formatted_div){
	var chat = $('#messages-container');
	var new_source = data["source"];
	if (new_source == "BOT"){
		chat.append('<div class="msg-row"><div class="col-xs-11 col-sm-11 col-md-11 col-lg-11 no-sides-padding msg-animate"><div class="bot-icon-div">Bot:</div><div class="panel message-panel bot-msg "><div class="panel-body bot-msg-body"><div><div class="message-text">'+formatted_div+'</div></div></div></div></div></div>');
	}else if(new_source == "CANDIDATE"){

		var child = $('<div class="msg-row">');
		$(child).append('<div class="row"><div class="col-xs-10 col-sm-10 col-md-10 col-lg-10  pull-right no-sides-padding msg-animate"><div class="panel message-panel user-msg"><div class="panel-body user-msg-body"><div class="message-text"><span></span></div></div></div><div class="user-msg-bubble">'+sessionStorage.getItem('username')+'</div></div>');
		$(child).find('span').html(formatted_div);
		chat.append(child);
	}
	$("#body-container").scrollTop( $('#body-container')[0].scrollHeight);	
}  


// Function taht is called when the server sends a message via websockets to my front end.
function processAndDisplayChatMessage(message){

	var content_data = JSON.parse(message.data);
	var formatted_div = generate_formatted_chat_message(
		content_data);
    if (content_data.disable_send_btn) {
        $("#messageSendButton").attr("disabled", true);
        $("#send-box").hide();
    } else {
        $("#messageSendButton").attr("disabled", false);
    }

    if (content_data.options) {
        $("#chat_options_con").html(content_data.options);
    } else {
        $("#chat_options_con").html("");
    }

	
	if(formatted_div.length > 0){
		add_message_to_chat(content_data, formatted_div);
	}
}


function sendTextMessage() {
    var count = 0

    if ($('#messageToSend').val() == "") {
        return
    }
    message = {}
    message.text = $('#messageToSend').val()
    message.command= 'send'
    message.timestamp = new Date();
    message.user_id = sessionStorage.getItem('user')

    $('#messageToSend').val('');
    console.log(count)
	chatsock.send(JSON.stringify(message));
	$("#message").val('').focus();
    return false;   
}
function sendBtnMessage(msg){
    var count = 0

    count += 1
    message = {}
    message.text = msg
    message.command= 'send'
    message.timestamp = new Date();
    console.log(count)
    // testing by passing a variable for client and server side communication.
    // By this way, user information can be passed by storing it in session\local storage
    message.user_id = sessionStorage.getItem('user')
    console.log(sessionStorage.getItem('user'))
	chatsock.send(JSON.stringify(message));
	$("#message").val('').focus();
    return false;

};

(function() {
$('#myModal').modal({backdrop: 'static', keyboard: false});
var html = '<option disabled selected value="0">Select Users</option>';
   // your page initialization code here
   // the DOM will be available here
if (sessionStorage.getItem('user') !== null) {
        sessionStorage.removeItem('user')
        sessionStorage.removeItem('username')
}
$.ajax({
		type: 'get',
        data: null,
		url: window.location.origin + '/mocker/get_users',
		success: function(result) {
            $.each( result.users, function( key, value ) {
              html += '<option value="'+value.id+'">'+value.username+'</option>';
            });
            $('.userList').html(html);
             $('#myModal').modal('show');
        }
	});})();
	function setUser() {
	    console.log($('#userList :selected').val());
	    console.log($('#userList :selected').text());
	    $('#myModal').modal('hide');
	    sessionStorage.setItem("user", $('#userList :selected').val());
	    sessionStorage.setItem("username",$('#userList :selected').text());
	}



