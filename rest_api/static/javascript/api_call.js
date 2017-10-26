$(document).ready(function(){
    // call the get api to render the all todo_list
    function GetTodoListData(e){
        var todo_list_table_body = $('.container').find('#todo_list_items').find('tbody');
        $.ajax({
            type: 'GET',
            url: '/api/todolist_apis/',
            success: function(result) {
                $.each(result, function(i,item){
                    var table_row = $('<tr></tr>')
                    $(table_row).append('<td>'+item.title+'</td>');
                    $(table_row).append('<td>'+item.description+'</td>');
                    $(table_row).append('<td><button type="button" class="btn btn-danger" id="'+ item.id+'">Delete</button></td>');
                    $(table_row).append('<td><button type="button" class="btn btn-primary" id="'+ item.id+'">Edit</button></td>');
                    $(todo_list_table_body).append($(table_row));
                });
            }
        });
     }
    // api call for delete the tasks
    $(document).on('click', '.btn-danger', function(e) {
        var todo_clicked_button = $(this);
        var todo_list_id = $(todo_clicked_button).attr('id');
        var api_url = '/api/todolist_apis/' + todo_list_id;
        $.ajax({
            type: 'DELETE',
            url: api_url,
            success: function(result) {
                $(todo_clicked_button).parent().parent().remove();
            }
        });
    });

    // Api call to add the data
    var submit_form = $('#add_todo_list');
    $(submit_form).submit(function(e) {
        $.ajax({
            type: 'post',
            url: '/api/todolist_apis/',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({'title': $('#title').val(), 'description': $('#description').val()}),
            success: function(data) {
                console.log(data);
                $('#title').val('');
                $('#description').val('');
                $('.container').find('#todo_list_items').find('tbody').find('tr').remove();
                GetTodoListData();
            },
            error: function( jqXhr, textStatus, errorThrown ){
                console.log( errorThrown );
            }
         });
        e.preventDefault();
    });
    GetTodoListData();
});
