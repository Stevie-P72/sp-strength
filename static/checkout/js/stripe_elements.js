var stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1)
var stripe_secret_key = $('#id_client_secret').text().slice(1,-1)

var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#stripe_card');

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
  ev.preventDefault();
  card.update({'disabled': true})
  $('submit-btn').attr('disabled', true)
  stripe.confirmCardPayment(stripe_secret_key, {
    payment_method: {
      card: card,
      
    }
  }).then(function(result) {
    if (result.error) {
        card.update({'disabled': false})
        $('submit-btn').attr('disabled', false)
      
      console.log(result.error.message);
    } else {
      
      if (result.paymentIntent.status === 'succeeded') {
          form.submit()
        
      }
    }
  });
});