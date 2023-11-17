$(document).ready(function () {
    // Prepare the preview for profile picture
    $("#wizard-picture").change(function () {
        readURL(this, '#wizardPicturePreview');
    });
});
