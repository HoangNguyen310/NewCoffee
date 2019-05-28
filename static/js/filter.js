$('.my-filter').each(function(){
    let content = $(this).attr('data-content') || null;
    if(content != null && $(content).length > 0){
        $(this).on('click', 'li', function(){
            var filter = $(this).attr('data-filter') || null;
            if(filter == '*'){
                $(content).find('.filter').fadeIn(500);
            } else {
                $.when($(content).find('.filter').fadeOut(500)).done(function(){
                    $(content).find('.filter'+filter).fadeIn(500);
                });
            }
        });
    }
});