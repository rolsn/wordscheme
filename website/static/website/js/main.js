$("#user-nav-tabs li").on('click', function(e) {
    var targetLink = $(e.currentTarget.children[0]).attr("href").slice(1);

    var profile_map = {
        bio         : "#user-bio",
        articles    : "#user-latest-articles",
        comments    : "#user-latest-comments"
    }

    $.each($(e.currentTarget).siblings(), function(index, el) {
        $(el).removeClass("active");
    });

    $.each(profile_map, function(hash, elid) {
        if (hash == targetLink) {
            $(elid).show();
            $(e.currentTarget).addClass("active");
        } else {
            $(elid).hide();
        }
    });

});
