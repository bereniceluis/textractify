/*  ==========================================
    SHOW UPLOADED IMAGE
* ========================================== */
function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      $("#imageResult").attr("src", e.target.result);
    };
    reader.readAsDataURL(input.files[0]);
  }
}

$(function () {
  $("#upload").on("change", function () {
    readURL(input);
  });
});

/*$("input[type=file]").change(function (e) {
  $in = $(this);
  $in.next().html($in.val());
});*/

