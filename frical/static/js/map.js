$(document).on('ready', even);
function even(e){
    new GMaps({
        div: '#gmap',
        lat: -12.043333,
        lng: -77.028333,
    });
}