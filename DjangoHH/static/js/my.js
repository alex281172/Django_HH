//alert('Hello Js!');

    var button = document.querySelector("#btn-text");
    //console.log(button);

    function foo(event)
    {
        window.location.href = 'https://neural-university.ru/';

    //    alert('Привет!');
        element = event.target;

        if ( element.classList.contains('btn-info') )
        {
            var new_class = 'btn-danger';
            var old_class = 'btn-info';
        }
        else {
            var new_class = 'btn-info';
            var old_class = 'btn-danger';
        }

        element.classList.remove(old_class);
        element.classList.add(new_class);
    }

    button.addEventListener('click', foo, false);

    // ajax
    $( document ).on('click', '#ajax-btn', function(event) {
        console.log('Step 1');
            $.ajax({
                    url: '/users/update-token-ajax/',
                    success: function (data) {
                        // data - ответ от сервера
                        console.log('Step 3')
                        console.log(data);
                        $('#token').html(data.key);
                    },
                });
    });

//$( document ).on('click', '#cities', function(event) {
//        $.ajax({
//                url: 'http://127.0.0.1:8000/api/v0/cities/',
//                success: function (data) {
//                    // data - ответ от сервера
//                    //console.log(data);
//                    for (i = 0; i < data.length; i++) {
//                        // словарь
//                       item = data[i];
//                       name = item.name;
//                       $('#div_cities').append('<li>' + name + '</li>' );
//                    }
//                },
//        });
//});
//
//$( document ).on('click', '#skills', function(event) {
//        $.ajax({
//                url: 'http://127.0.0.1:8000/api/v0/skills/',
//                success: function (data) {
//                    // data - ответ от сервера
//                    //console.log(data);
//                    for (i = 0; i < data.length; i++) {
//                        // словарь
//                       item = data[i];
//                       name = item.name;
//                       $('#div_skills').append('<li>' + name + '</li>' );
//                    }
//                },
//            });
//});
//
//
//$( document ).on('click', '#all', function(event) {
//        $.ajax({
//                url: 'http://127.0.0.1:8000/api/v0/cities/',
//                success: function (data) {
//                    // data - ответ от сервера
//                    //console.log(data);
//                    for (i = 0; i < data.length; i++) {
//                        // словарь
//                       item = data[i];
//                       name = item.name;
//                       $('#div_cities').append('<li>' + name + '</li>' );
//                    }
//                },
//        });
//                $.ajax({
//                url: 'http://127.0.0.1:8000/api/v0/skills/',
//                success: function (data) {
//                    // data - ответ от сервера
//                    //console.log(data);
//                    for (i = 0; i < data.length; i++) {
//                        // словарь
//                       item = data[i];
//                       name = item.name;
//                       $('#div_skills').append('<li>' + name + '</li>' );
//                    }
//                },
//         });
//
//
//});
//
