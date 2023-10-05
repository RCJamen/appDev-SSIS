$(function () {
    $(".btn-delete").click(function () {
        var code = $(this).attr('data-id');
        if (confirm("Are your sure?")) {
            $.ajaxSetup({
                headers: {
                    'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
                }
            });
            $.ajax({
                url: url,
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