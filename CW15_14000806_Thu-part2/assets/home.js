var users = [];
$(document).ready(function () {
  $.get("https://reqres.in/api/users", function (data, status) {
    $.each(data.data, function (index, value) {
      let the_option = `<option value="${value.id}">${value.first_name} ${value.last_name}</option>`;
      $("#selectusers").append(the_option);
    });

    $("#selectusers").change(function () {
      var selected_user = $(this).children("option:selected").val();
      var exist_data = users.findIndex((user) => user.id == selected_user);

      if (exist_data === -1) {
        $.get(
          `https://reqres.in/api/users/${selected_user}`,
          function (data, status) {
            users.push(data.data);
            let chd = $("#user_info");
            chd.find("img").attr("src", data.data.avatar);
            chd
              .find("h5")
              .text(`${data.data.first_name} ${data.data.last_name}`);
            chd.find("p").text(`email : ${data.data.email}`);
          }
        );
      } else {
        users.map((data, index) => {
          if (data.id === Number(selected_user)) {
            let chd = $("#user_info");
            chd.find("img").attr("src", data.avatar);
            chd.find("h5").text(`${data.first_name} ${data.last_name}`);
            chd.find("p").text(`email : ${data.email}`);
          }
        });
      }
    });
  });
});
