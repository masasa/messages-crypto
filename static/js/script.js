
function changeSubmitButtonText(){
	var e = document.getElementById("submit_button");
	if (e.value=="Encrypt Message") e.value = "Decrypt Message";
	else e.value = "Encrypt Message";
}

function isASCII(str) {
	return /^[\x00-\x7F]*$/.test(str);
}


function validateForm() {
	
	var errKey = "";
	var errMsg = "";
	var inputOk = true;
	var key = document.forms["code_form"]["key"].value;
	var msg = document.forms["code_form"]["msg"].value;

	// handeling the key validation
	if (key == null || key == ""){
		errKey = "Key box can't be empty."
		inputOk = false;
	}else if(!isASCII(key)){
		errKey = "Key box must contains only english letters, numbers and symbols."
		inputOk = false;
	}

	// handeling the message validation
	if (msg == null || msg == ""){
		errMsg = "Message box can't be empty."
		inputOk = false;
	}else if(!isASCII(msg)){
		errMsg = "Message box must contains only english letters, numbers and symbols."
		inputOk = false;
	}

	if(!inputOk){
		document.getElementById("key_err").textContent = errKey;
		document.getElementById("msg_err").textContent = errMsg;
		return false;
	}
}

