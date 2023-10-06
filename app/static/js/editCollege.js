$(document).ready(function () {
    $('.edit-btnCollege').click(function () {
        // Get data-code and data-name from the clicked button
        var code = $(this).data('code');
        var name = $(this).data('name');

        // Set the values of the input fields in the modal
        $('#editCodeInput').val(code);
        $('#editNameInput').val(name);
    });
});