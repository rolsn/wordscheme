$("#user-nav-tabs li a").on('click', function(e) {
    var target = $(e.currentTarget).attr("href").slice(1);

    var profile_map = {
        bio         : "#user-bio",
        articles    : "#user-latest-articles",
        comments    : "#user-latest-comments"
    }

    $.each(profile_map, function(hash, id) {
        if (hash == target) {
            $(id).show();
        } else {
            $(id).hide();
        }
    });

});
