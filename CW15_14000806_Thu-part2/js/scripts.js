/*!
* Start Bootstrap - Shop Homepage v5.0.4 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

$(function (){
    $.get(`https://reqres.in/api/users`, function (data) {
        // data.map(x=> {})
        $.each(data.data, function (index, value) {
            $(".row").append(
                `<div class="col mb-5">
                    <div class="card h-100">
                        <!-- Product image-->
                        <img class="card-img-top" src="${value.avatar}" alt="" />
                        <!-- Product details-->
                        <div class="card-body p-4">
                            <div class="text-center">
                                <!-- Product name-->
                                <h5 class="fw-bolder">${value.first_name} - ${value.last_name}</h5>
                                <!-- Product price-->
                                ${value.email}
                            </div>
                        </div>
                        <!-- Product actions-->
                        <div class="text-center card-footer p-4 pt-0 border-top-0 bg-transparent">
                            
                            <!-- Button trigger modal -->
                            <button type="button" class="show-detail btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" value_id="${value.id}" value_name="${value.first_name} - ${value.last_name}" value_email="${value.email}" value_img="${value.avatar}">View details</button>
                            
                            <button class="add_cart btn btn-outline-dark mt-auto" value_id="${value.id}" value_name="${value.first_name} - ${value.last_name}" value_email="${value.email}" value_img="${value.avatar}"">add to cart</button>
                        </div>
                    </div>
                </div>`
            )
        
        });
    });



    $("body").on('click', '.show-detail', function(){
        $('.modal-body').empty()
        $(".modal-body").append(
            `<div class="col mb-5">
                <div class="card h-100">
                    <!-- Product image-->
                    <img class="card-img-top" src="${$(this).attr('value_img')}" alt="..." />
                    <!-- Product details-->
                    <div class="card-body p-4">
                        <div class="text-center">
                            <!-- Product name-->
                            <h5 class="fw-bolder">${$(this).attr('value_name')}</h5>
                            <!-- Product price-->
                            ${$(this).attr('value_email')}
                        </div>
                    </div>
                    <!-- Product actions-->

                </div>
            </div>`
        )
    });



    $("body").on('click', '.add_cart', function(){
        console.log('sd')
        console.log("storage before", storage);
        let value_id = $(this).attr('value_id')
        let value_avatar = $(this).attr('value_img')
        let value_email = $(this).attr('value_email')
        let value_name = $(this).attr('value_name')
        
        let data_obj = { 'value_id': value_id, 'value_img': value_avatar, 'value_email': value_email, 'value_name': value_name }

        var storage = JSON.parse(localStorage.getItem("cart"));

        
        if (storage == null) {
            storage = [];
            storage.push(data_obj);
            localStorage.setItem("cart", JSON.stringify(storage));
            the_cart();
        }
        else if (storage.length != 0) {
            storage.push(data_obj);
            localStorage.setItem("cart", JSON.stringify(storage));
            the_cart();
        }
    });
            


    function the_cart() {
        var the_card = JSON.parse(localStorage.getItem("cart"));
        if (the_card == null) {
            $("#the_cart").text("0");
        }
        else if (the_card.length > 0) {
            $("#the_cart").text(the_card.length);
        }
    }
    the_cart();

    $('#basket').on('click' ,function () {
        $('.modal-body').empty()
        var storage = JSON.parse(localStorage.getItem("cart"));
        if (!storage){

        }
        else{

            $.each(storage, function (index, value) {
            var inner_modal =
            `<div class="row my-2">
                <div class="col-2">
                    <img src="${value.value_img}" alt="." class="img-fluid rounded">
                </div>
                <div class="col-2">
                    <p>${value.value_name}</p>
                </div>
                <div class="col-6">
                    <p> ${value.value_email}</p>
                </div>
                <div class="col-2">
                </div>
            </div>`

            $('.modal-body').append(inner_modal)
            })
        }
    })



    $("body").on('click', '.del', function(){
        $('.modal-body').empty()
        localStorage.removeItem("cart")
        the_cart();

    });
    
});
        
