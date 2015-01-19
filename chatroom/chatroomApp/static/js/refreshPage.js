// Insert code here to run when the DOM is ready
$(document).ready( function() {
    console.log("ready!");

    // Uses AJAX to send request to refresh page
    setInterval(function () {
        console.log("refreshing")
        var message_id = $(".message").last().attr("data-message-id");

        $.ajax({
            type: "GET",
            url: "/chat/get-new-messages/" + message_id,
            success: function (response) {
                message_list = $("#message_list");
                message_list.append(response);
            }

        });

    }, 10*1000);
});
