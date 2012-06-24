/**
 * niceReeder
 *
 * @author Javi Manzano | @jgasteiz
 */

var NICEREEDER = (function() {

	/**
	 * Initializes click listeners
	 *
	 * @method initListeners
	 */
	function initListeners() {
		$(".new-subscription").click(function() {
			showNewSubscriptionForm();
		});
		$(".read-subscription").click(function() {
			location.href = "/subscription/" + this.id;
		});
		$(".close-reeder").click(function() {
			closeModal();
		});
	}

	/**
	 * For creating a new subscription
	 *
	 * @method loadSubscriptionForm
	 */
	function showNewSubscriptionForm() {
		$(".form").show();
		$(".mask").show();
	}


	var init = function() {
		initListeners();
	};

	return {
		init: init
	}

})(NICEREEDER);