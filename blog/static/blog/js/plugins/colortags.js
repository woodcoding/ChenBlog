/**
 * Created by chens on 2016/9/4 0004.
 */
var color = new Array(5);
color[0] = 'btn-primary';
color[1] = 'btn-success';
color[2] = 'btn-info';
color[3] = 'btn-warning';
color[4] = 'btn-danger';
    $(".tag").each(function(){
        var x = $(this).index()%5;
        $(this).toggleClass(color[x]);
    });
