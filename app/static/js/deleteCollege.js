$(function () {
    $(".btn-deleteCollege").click(function () {
        var code = $(this).attr('data-code');
        if (confirm("Are your sure you want to Delete College?")) {
            $.ajaxSetup({
                headers: {
                    'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
                }
            });
            $.ajax({
                url: '/college/delete',
                method: 'POST',
                data: { code: code },
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