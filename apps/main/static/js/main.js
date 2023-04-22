$(document).ready(() => {
    $("[id^='furniture']").click((event) => {
        var roomID = event.target.attributes['data-room-id'].value;
        // var wqe = `http://localhost:8000/get_furniture_by_room_id/${roomID}`;
        // debugger
        $.ajax({
            url: `http://localhost:8000/get_furniture_by_room_id/${roomID}`,
            method: 'GET',
            headers: {
                contentType: 'application/json',
            },
            success: (response) => {
                console.log(response)
                $("#result").html('');
                response.forEach(furniture=> {
                    $("#result").append(`
                        <div class="col-4">
                            <div class="card-title">
                            <a href="#">
                                <img class="img-fluid" src="${furniture.image}" alt="">
                            </a>
                            </div>
                            <div class="card-body">
                                <h4 class="card-title">
                                    <a href="/production/${furniture.url}">${furniture.title}</a>
                                </h4>
                                <h5> ${furniture.room} </h5>
                                <p class="card-text">${furniture.price}</p>
                            </div>
                        </div>
                    `);
                });
            },
            error: () => {
                alert("Ошибочка")
            }
        })

    });
})
