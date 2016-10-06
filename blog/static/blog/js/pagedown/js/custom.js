/**
 * Created by chens on 2016/10/6 0006.
 */
$(document).ready(function(){
	fixwidth();
});
$(window).resize(function(){
    fixwidth();
});

function  fixwidth() {
    //自适应编辑框宽度
    var width = $("#id_title").width()+25;
	$("#id_text").css("width", width);
    $("#id_text_wmd_preview").css("width", width);
}