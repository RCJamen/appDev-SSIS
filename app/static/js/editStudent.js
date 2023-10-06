$(document).ready(function () {
    $('.edit-btnStudent').click(function () {
        // Get data-code and data-name from the clicked button
        var id = $(this).data('id');
        var firstname = $(this).data('firstname');
        var lastname = $(this).data('lastname');
        var coursecode = $(this).data('coursecode');
        var year = $(this).data('year');
        var gender = $(this).data('gender');

        // Set the values of the input fields in the modal
        $('#editIdInput').val(id);
        $('#editFirstnameInput').val(firstname);
        $('#editLastnameInput').val(lastname);
        $('#editCoursecodeInput').val(coursecode);
        $('#editYearInput').val(year);
        $('#editGenderInput').val(gender);
    });
});
