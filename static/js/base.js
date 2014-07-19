function merge(obj1,obj2){
    var obj3 = {};
    for (var attrname in obj1) { obj3[attrname] = obj1[attrname]; }
    for (var attrname in obj2) { obj3[attrname] = obj2[attrname]; }
    return obj3;
}

function getList(model, ordBy){
    $.get('/get_list',{'model':model,'ord_by':ordBy},function(data){
       $('#cards').html(data)
    });
}

function search(model, q){
    $.get('/search',{'model':model, 'q':q}, function(data){
       $('#cards').html(data);
    });
}

function login(){
    $.post('/login/',$('#sign-in-form').serialize(),function(data){
        console.log(data)
        location.reload()
    })
}

function getUrlParam(name){
    var url = window.location.href
    var param = url.split('/' + name + '/')[1]
    param = param.slice(0,param.length-1)
    console.log(param)
    return param
}

$(document).ready(function(){
   //$('#sign-in-form').submit(function(e){
   $('#sign-in-form').submit(function(e){
       console.log('sign in form submited');
       login();
       e.preventDefault();
   });

});