
$(document).ready(function(){
    //getList('food','name')

    $('#sort-by button').click(function(){
        console.log($(this).val());
        getList('food',$(this).val());
    });
});
