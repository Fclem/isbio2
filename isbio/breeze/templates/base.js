/**
 * Created by clem on 02/06/17.
 */
//Displays floating disposable error message box
function ShowError(HtmlContent) {
	$("#error_msg").removeClass("hidden");
	//$("#error_msg").innerHTML = HtmlContent;
	if (HtmlContent !== "") {
		var x = document.getElementById("error_msg_holder");
		if (x !== undefined) {
			x.innerHTML = HtmlContent;
		}
	}
}

$(document).ready(function () {
	var x = document.getElementById("error_msg_holder");
	if (x.innerHTML !== "" && x.innerHTML !== "<p></p>") {
		ShowError("");
	}
});

function fixDropDownSub(item) {

}

function fixDropDown() {
	//drop down
	var el = $('button.dropdown-toggle');
	for (var i = 0; i < el.length; i++) {
		el.eq(i).on("click", function () {
			var tg = $(this);
			var btGrp = tg.parents('div.btn-group').first();
			var modal = tg.parents('div.modal-body').first();
			if (btGrp.hasClass('open')) {
				//modal.(modal.height() - 450);
				modal.height(modal.height() - 450);
			} else {
				modal.height(modal.height() + 450);
			}
		});
	}
}

// prevents click on a submit button
function disableObj(name) {
	var clkBtn = $('#' + name + '')[0];
	//protect from double submission while sending
	if (clkBtn !== undefined) clkBtn.disabled = true;
}

function enableObj(name) {
	var clkBtn = $('#' + name + '')[0];
	if (clkBtn !== undefined) clkBtn.disabled = false;
}

function switchObj(name) {
	var clkBtn = $('#' + name + '')[0];
	if (clkBtn !== undefined) clkBtn.disabled = !clkBtn.disabled;
}

function isFunction(functionToCheck) {
	var getType = {};
	return functionToCheck && getType.toString.call(functionToCheck) === '[object Function]';
}
