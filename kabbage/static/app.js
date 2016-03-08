console.log('Loaded js');

function gotoResults(result) {
  var queryString = $.param(result);
  var redirect = window.location.href + 'result?' + queryString;
  console.log(redirect);
  window.location.href = redirect;
}

function submitForm (e) {
  e.preventDefault();
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
      gotoResults(result);
    },
    error: function(result) {
      if(!result.responseJSON){
        $('#error').removeClass('hidden');
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
