//import $ from 'jquery';
//
//$(() => {
//    $('.camera_control a').on('click', function (e) {
//        e.preventDefault();
//        const url = $(this).attr('href');
//        fetch(url)
//          .then(response => console.log(response.json()));
//    })
//})

import React from 'react';
import ReactDOM from 'react-dom/client';

import SingleCamera from '../pages/SingleCamera';

const root = ReactDOM.createRoot(document.getElementById('root'));

// TODO: Pass a config from global val

root.render(
  <React.StrictMode>
    <SingleCamera />
  </React.StrictMode>
);

