function getNurtional(food, amount){
    $.get('/get_nutritional',{'food':food,'amount':amount}, function(data){
        $('#nutritional').html(data);
    });
}

$(document).ready(function(){
   getNurtional(getUrlParam('food'),100);
   $('input').change(function(){
      getNurtional(getUrlParam('food'), $(this).val())
   });
});