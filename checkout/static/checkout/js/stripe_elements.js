var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
// Style of card input
var style = {
  base: {
    color: '#212529',
    fontFamily: '"Josefin Sans", sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#c3c1c1'
    }
  },
  invalid: {
    color: '#dc3545',
    iconColor: '#dc3545'
  }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');


// Handle validation errors on the card number input if user enters incorrect card details
card.addEventListener('change', function (event) {
  var errorDiv = document.getElementById('card-errors');
  if (event.error) {
      var html = `
          <span>
              <i class="fas fa-times"></i>
          </span>
          <span>${event.error.message}</span>
      `;
      $(errorDiv).html(html);
  } else {
      errorDiv.textContent = '';
  }
});