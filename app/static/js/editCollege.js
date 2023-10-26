$(document).ready(function () {
    $('.edit-btnCollege').click(function () {
        var code = $(this).data('code');
        var name = $(this).data('name');

        $('#editCodeInput').val(code);
        $('#editNameInput').val(name);
    });
});