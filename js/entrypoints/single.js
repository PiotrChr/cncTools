import $ from 'jquery';

$(() => {
    $('.camera_control a').on('click', function (e) {
        e.preventDefault();
        const url = $(this).attr('href');
        fetch(url)
          .then(response => console.log(response.json()));
    })
})