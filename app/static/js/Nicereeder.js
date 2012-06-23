

var NICEREEDER = (function() {

	function initListeners() {
		$(".new-subscription").click(function() {
			loadSubscriptionForm();
		});
		$(".read-subscription").click(function() {
			loadSubscription(this);
		});
		$(".close-reeder").click(function() {
			closeModal();
		});
	}

	function loadSubscriptionForm() {
		showNewSubscriptionModal();
	}

	function loadSubscription(element) {
		showModal();
		$("#reeder_head").html(
			'<div class="progress progress-success progress-striped active">' +
			'<div class="bar"></div></div>');
		$("#reeder_content").html('');
		$.post("_ajax/load_rss/", 
			{
				"id_rss": $(element).attr("id")
			},
			function(data) {
				$("#reeder_head").html(data[0]['name']);
				for (var i in data) {
					$("#reeder_content").append(formatEntry(data[i]));
				}
			}
		);
	}

	function formatEntry(entry) {
		var html = 
		'<div class="entry">' +
			'<h1><a target="_blank" href="' + entry['url'] 
				+ '">' + entry['title'] + 
			'</a></h1>' +
			entry['body'] +
		'</div>';
		return html;
	}

	function showNewSubscriptionModal() {
		$(".form").show();
		$(".mask").show();
	}

	function showModal() {
		$(".reeder").show();
		$(".mask").show();
	}

	function closeModal() {
		$(".reeder").hide();
		$(".mask").hide();
	}

	var init = function() {
		initListeners();
	};

	return {
		init: init
	}

})(NICEREEDER);