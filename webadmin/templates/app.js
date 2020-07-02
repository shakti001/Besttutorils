 $(document).ready(function() {
    $('.username').editable({
        mode: 'inline',
    });
});
$(document).ready(function () {
    
    $('#table_id').DataTable();
});

    ClassicEditor
        .create( document.querySelector( '.kt-ckeditor-1' ) )
        .catch( error => {
            console.error( error );
        } );

    ClassicEditor
        .create( document.querySelector( '.kt-ckeditor-2' ) )
        .catch( error => {
            console.error( error );
        } );


    ClassicEditor
        .create( document.querySelector( '.kt-ckeditor-3' ) )
        .catch( error => {
            console.error( error );
        } );
    $(function () {
            $("#sortable").sortable();
            $("#sortable").disableSelection();
        });

        $(document).ready(function () {

            $('.sortable').nestedSortable({
                handle: 'div',
                items: 'li',
                toleranceElement: '> div',
                collapsible: true,
                maxLevels: 5
            });

        });

