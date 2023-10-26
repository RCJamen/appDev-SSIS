$(document).ready(function () {
    $('.edit-btnCourse').click(function () {
        var code = $(this).data('code');
        var name = $(this).data('name');
        var collegecode = $(this).data('collegecode');

        $('#editCodeInput').val(code);
        $('#editNameInput').val(name);
        $('#editCollegecodeInput').val(collegecode);
    });
});