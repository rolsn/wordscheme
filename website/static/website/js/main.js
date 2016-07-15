$(".sitenav-tabs li").on('click', function(e) {
    var targetLink = $(e.currentTarget.children[0]).attr("href").slice(1);

    var profile_map = {
        bio         : "#user-bio",
        articles    : "#user-latest-articles",
        guilds      : "#user-guilds",
        following   : "#user-latest-following",
        leader      : "#guilds-leader",
        member      : "#guilds-member",
        invites     : "#guilds-invites"
    }

    $(e.currentTarget).siblings().removeClass("active");

    $.each(profile_map, function(hash, elid) {
        if (hash == targetLink) {
            $(elid).show();
            $(e.currentTarget).addClass("active");
        } else {
            $(elid).hide();
        }
    });

});

$("#user-banner button").on('click', function(e) {
    $(e.currentTarget).toggleClass('following').toggleClass('follow')
})

$("#article-rating").on('click', function(e) {
    $(e.currentTarget).toggleClass('article-like').toggleClass('article-liked')
})
