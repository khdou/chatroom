// Insert code here to run when the DOM is ready
$(document).ready( function() {
    console.log("ready!");

    // Uses AJAX to send request to refresh page
    setInterval(function () {
        console.log("refreshing")
        var grumble_id = $(".grumble").first().attr("grumble-id");

        $.ajax({
            type: "GET",
            url: "/grumblr/get-new-grumbles/" + grumble_id,
            success: function (response) {
                grumble_list = $("#grumble_list");
                grumble_list.prepend(response);
            }

        });

    }, 10*1000);
});
