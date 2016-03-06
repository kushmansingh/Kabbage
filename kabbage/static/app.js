console.log('Loaded js');
function submitForm () {
  console.log('Submit');
  // Do ajax call here
}
$(function (){
  $('#submit').bind('click', submitForm);
});