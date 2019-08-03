function add_like(current_elem){
    var article_id = current_elem.attr('data-id');
    var praisecount = parseInt(current_elem.children('span').text().match(/\d+/));
    var flag = current_elem.attr('class')
    if (flag == 'action') {
        $.ajax({
            cache: false,
            type: "POST",
            url:"{% url 'blog:add_like' %}",
            data:{'article_id':article_id},
            async: true,
            beforeSend:function(xhr, settings){
                xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
             },

            success: function(data) {
                if(data.status == 'fail'){
                    window.location.href="{% url 'blog:index' %}";
                }else if(data.status == 'success'){
                    current_elem.attr('class','action actived');
                    current_elem.children('span').text(current_elem.children('span').text().replace(praisecount, praisecount + 1));
                }
            },
        });
    }else if(flag == 'action actived'){
        alert('您已经点过赞了');
    }
}

$('#Addlike').click(function(){
    add_like($(this));
});