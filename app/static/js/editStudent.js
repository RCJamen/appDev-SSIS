$(document).ready(function () {
    $('.edit-btnStudent').click(function () {
        var id = $(this).data('id');
        var firstname = $(this).data('firstname');
        var lastname = $(this).data('lastname');
        var coursecode = $(this).data('coursecode');
        var year = $(this).data('year');
        var gender = $(this).data('gender');

        $('#editIdInput').val(id);
        $('#editFirstnameInput').val(firstname);
        $('#editLastnameInput').val(lastname);
        $('#editCoursecodeInput').val(coursecode);
        $('#editYearInput').val(year);
        $('#editGenderInput').val(gender);
    });
});
