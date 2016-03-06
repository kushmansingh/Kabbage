console.log('Loaded js');

function submitForm () {
  var values = $('form').serialize();
  $.ajax({
    url: '/prequal?'+values,
    type: 'GET',
    dataType: 'json',
    success: function(result) {
    },
    error: function(result) {

    }
  });
}

$(function (){
  $('#submit').bind('click', submitForm);
});
