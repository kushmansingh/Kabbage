console.log('Loaded js');

function submitForm () {
  var values = $('form').serializeArray();
  var data = {}
  for (var i = values.length - 1; i >= 0; i--) {
    data[values[i].name] = values[i].value;
  };
  $('#error').addClass('hidden')
  $('span').remove();
  $('.form-group').removeClass('has-error')
  $.ajax({
    url: '/prequal',
    type: 'POST',
    dataType: 'json',
    data: data,
    success: function(result) {
    },
    error: function(result) {
      if(!result.responseJSON){
        $('#error').removeClass('hidden');
        debugger
        $('#error').text(result.status+' '+result.responseText);
      };
      for (var key in result.responseJSON) {
        $('input[name='+key+']').parent().addClass('has-error');
        $('input[name='+key+']').after(
          '<span class="help-block">'+result.responseJSON[key]+'</span>');
      }
    }
  });
}

$(function (){
  $('#submit').bind('click', submitForm);
});
