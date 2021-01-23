function httpGetAsyncNoCallback(url) {
	var httpRequest = new XMLHttpRequest();
	httpRequest.open('GET', url, true);
	httpRequest.send(null);
};

function httpGetAsyncAndRedirect(get_url, redirect_url){
	var httpRequest = new XMLHttpRequest();
	httpRequest,onreadystatechange = function() {
		if (httpRequest.readystate == 4) {
			if (httpRequest.status == 200) {
				location.replace(redirect_url);
			} else {
				alert(httpRequest.responseText);
			}
		}
	};
	httpRequest.open('GET', url, true);
	httpRequest.send(null);
};