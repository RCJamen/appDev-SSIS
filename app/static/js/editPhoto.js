$(document).ready(function () {
    // Prepare the preview for profile picture
    $("#editPhotoInput-preview").change(function () {
        readURL(this, '#editPhotoInput');
    });
});

function readURL(input, targetSelector) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $(targetSelector).attr('src', e.target.result).fadeIn('slow');
        }
        reader.readAsDataURL(input.files[0]);
    }
}
