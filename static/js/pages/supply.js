function addToCart(supply_url){
    $.get('/add_to_cart', {'supply_url': supply_url }, function(data){
               console.log('supply added');
           });
}

$(document).ready(function(){

    $('.addToCart').click(function(){
        addToCart(getUrlParam('supply'))
    })
});
