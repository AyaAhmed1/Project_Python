$(function(){
'use strict';
//hide placeholder
$('[placeholder]').focus(function(){
	$(this).attr('data-text',$(this).attr('placeholder'));
	$(this).attr('placeholder','');

}).blur(function(){
	$(this).attr('placeholder',$(this).attr('data-text'));
});
// add * torequired field
$('input').each(function()
{

if($(this).attr('required')==='required')
{
	$(this).after('<span>*</span>');
}

});
//convert password field to text field on hover

var passfield =$(".password");
$('.show-pass').hover(function()
{
	passfield.attr('type','text');

},function(){
	passfield.attr('type','password');
}

)

$(".confirm").click(function(){
return confirm('are you sure?')

})

});

