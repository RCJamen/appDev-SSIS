$(function () {
    $(".btn-deleteStudent").click(function () {
        var id = $(this).attr('data-id');
        if (confirm("Are your sure you want to Delete Student?")) {
            $.ajaxSetup({
                headers: {
                    'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
                }
            });
            $.ajax({
                url: '/student/delete',
                method: 'POST',
                data: { id: id },
                success: function (result) {
                    console.log(result);
                    if (result.success) {
                        alert(result.message);
                        location.reload()
                    } else {
                        alert(result.message);
                    }
                }
            });
        }
    });
});