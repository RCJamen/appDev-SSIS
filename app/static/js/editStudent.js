$(document).ready(function () {
    $('.edit-btnStudent').click(function () {
        var id = $(this).data('id');
        var photo = $(this).data('photo');
        var firstname = $(this).data('firstname');
        var lastname = $(this).data('lastname');
        var coursecode = $(this).data('coursecode');
        var year = $(this).data('year');
        var gender = $(this).data('gender');

        $('#editIdInput').val(id);
        $('#editPhotoInput').val(photo);
        $('#editFirstnameInput').val(firstname);
        $('#editLastnameInput').val(lastname);
        $('#editCoursecodeInput').val(coursecode);
        $('#editYearInput').val(year);
        $('#editGenderInput').val(gender);
    });
});

$('#editStudentModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var photo = button.data('photo');
    var modal = $(this);
    modal.find('.picture-src').attr('src', photo);
});