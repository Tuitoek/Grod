var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function () {
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)

		if (user == 'AnonymousUser') {
			addCookieItem(productId, action)
		} else {
			updateUserOrder(productId, action)
		}
	})
}

function updateUserOrder(productId, action) {
	console.log('User is authenticated, sending data...')

	var url = '/update_item/'

	fetch(url, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'X-CSRFToken': csrftoken,
			},
			body: JSON.stringify({
				'productId': productId,
				'action': action
			})
		})
		.then((response) => {
			return response.json();
		})
		.then((data) => {
			location.reload()
		});
}

function addCookieItem(productId, action) {
	console.log('User is not authenticated')

	if (action == 'add') {
		if (cart[productId] == undefined) {
			cart[productId] = {
				'quantity': 1
			}

		} else {
			cart[productId]['quantity'] += 1
		}
	}

	if (action == 'remove') {
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0) {
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}
	console.log('CART:', cart)
	document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"

	location.reload()
}

/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
function openNav() {
	document.getElementById("mySidebar").style.width = "250px";
	document.getElementById("main").style.marginLeft = "250px";
	document.body.style.backgroundColor = "goldenrod";
}

/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
function closeNav() {
	document.getElementById("mySidebar").style.width = "0";
	document.getElementById("main").style.marginLeft = "0";
	document.body.style.backgroundColor = "white";
}
var myCarousel = document.querySelector('#myCarousel')
var carousel = new bootstrap.Carousel(myCarousel)