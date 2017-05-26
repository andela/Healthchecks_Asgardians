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
//            var value = $( profile.report_frequency)
//            $("input[name='report-frequency']").val(['value']);

    });
});