$(document).ready(function () {
    $('.edit-btnCourse').click(function () {
        // Get data-code and data-name from the clicked button
        var code = $(this).data('code');
        var name = $(this).data('name');
        var collegecode = $(this).data('collegecode');

        // Set the values of the input fields in the modal
        $('#editCodeInput').val(code);
        $('#editNameInput').val(name);
        $('#editCollegecodeInput').val(collegecode);
    });
});