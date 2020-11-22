$(window).load(function(){

    $("#approvebtn").click(function(){
    let username = $(this).attr("username");
    let csrf = $(this).attr("csrf");
    $.ajax({
      url: '/useradmin/approve/',
      data: {
        username: username,
        csrfmiddlewaretoken: csrf
      },
      type: 'post',
      cache: false,
      success: function (data) {
        $("#approve").html(data);
      }
    });

});
});