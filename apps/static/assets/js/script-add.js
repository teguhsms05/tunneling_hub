$(function () {
    let validator = $('form.needs-validation').jbvalidator({
        language: "{{ ASSETS_ROOT }}/js/en.json",
        errorMessage: true,
        successClass: true,    
    });

    //new custom validate methode
    validator.validator.custom = function (el, event) {

        if ($(el).is('[name=password]') && $(el).val().length < 5) {
            return 'Your password must be at least 5 characters long.';
        }
        

        return '';
    }

    let validatorServerSide = $('form.validatorServerSide').jbvalidator({
        errorMessage: true,
        successClass: true,
    });

})
$(document).ready(function() {
    $('#example').addClass('nowrap').dataTable({
        responsive: true,
    });
});

function successCpanel(msg) {
    Swal.fire({
        title: msg,
        text: 'Group Domain added successfully',
        icon: 'success',
        showConfirmButton: false,
        timer: 3000
    });
}
function duplicateCpanel(msg) {
    Swal.fire({
        title: msg,
        text: 'Please change the group domain ',
        icon: 'error',
        showConfirmButton: false,
        timer: 3000
    });
}
function deleteCpanel(msg) {
    Swal.fire({
        title: msg,
        text: 'Group Domain successfully ',
        icon: 'success',
        showConfirmButton: false,
        timer: 3000
    });
}