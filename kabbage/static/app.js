console.log('Loaded js');

function submitForm () {
  var values = $('form').serializeArray();
  var data = {}
  for (var i = values.length - 1; i >= 0; i--) {
    data[values[i].name] = values[i].value;
  };
  $.ajax({
    url: '/prequal',
    type: 'POST',
    dataType: 'json',
    data: data,
    success: function(result) {
    },
    error: function(result) {

    }
  });
}

$(function (){
  $('#submit').bind('click', submitForm);
});
