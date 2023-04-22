$(document).ready(()=>{
    $("#addToCart").click((event)=>{
        event.preventDefault();
        
        // var bookID = event.target.attributes['data-book'].id;
        var furID = event.currentTarget.attributes['data-furniture'].value;
        var price = event.currentTarget.attributes['data-price'].value;
        // $(`#pricee`).text();
        var url = `/cart/add/${furID}`;
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
