$(document).ready(()=>{
    $("#addToFavs").click((event)=>{
        event.preventDefault();
        
        // var bookID = event.target.attributes['data-book'].id;
        var furID = event.currentTarget.attributes['data-furniture'].value;
        // $(`#pricee`).text();
        var url = `/favs/add/${furID}`;
        debugger
        $.ajax({
            
            url: url,
            method: `POST`,
            headers: {
                "x-csrf-token": $("input[name='csrfmiddlewaretoken']").val(),
                contentType: 'application/json',
                
            },
            data: {
                "quantity_buying": 1,
                "price": price
            },
            success: () => {
                
                alert("Работает")
            },
            error: () => {
                
                alert("Ошибочка")
            }
        })


        // alert("");
    });
})
