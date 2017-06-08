$(function() {

    $(".member-remove").click(function() {
        var $this = $(this);

        $("#rtm-email").text($this.data("email"));
        $("#remove-team-member-email").val($this.data("email"));
        $('#remove-team-member-modal').modal("show");

        return false;
    });

});
$(function(){
    $('#send_report').change(function(){
        if ($(this).is(':checked')) {
            $('#frequency').show();
        }else{
           // $('#monthly').prop('checked', true);
            $('#frequency').hide();
        }
    });
});

$(document).on('change','.check-selected',function(){
var row = $(this).closest('tr');
var atLeastOneIsChecked = $('.check-selected:checked').length > 0;
var emailField =  $('#itm-email').val();
    if($(this).is(':checked'))
    {
      $(row).find('.scope').prop("disabled",false);
      $(row).find('.scope').prop("checked",true);
    }
    else
    {
      $(row).find('.scope').prop("disabled",true);
    }

    if ((atLeastOneIsChecked) && !(emailField == "")){
        $('.send-invite').prop("disabled", false)
    }
    else {
        $('.send-invite').prop("disabled", true)
    }
});