function saveContent(content_name) {
    var data = $('form').serialize();
    data += '&content_name=' + content_name
    console.log(data)
    $.post('/save_content/',data,function(data){
        console.log('the ajax call was made')
        if(data['saved']){
            console.log('data saved')
        }
        else {
            $('form').html(data['form']);
        }
    });
}

$(document).ready(function(){
//    $('form').submit(function(e){
//        //e.preventDefault()
//        //saveContent($('form').attr('id'))
//    })
})
