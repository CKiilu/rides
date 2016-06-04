function initMap() {
    var latlng = {
        lat: -1.2921,
        lng: 36.8219
    }
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 14,
        center: latlng,
    });
    var marker = new google.maps.Marker({
        position: latlng,
        map: map,
    });
    map.addListener('click', function(position) {
        map.setZoom(14);
        var latlng = {
            lat: position.latLng.lat(),
            lng: position.latLng.lng(),
        }
        map.panTo(latlng);
        marker.setPosition(latlng);
        console.log(latlng);
    });
}

function getUserLocation() {
    var browserSupportFlag = new Boolean();
    var initialLocation;
    var latlng;
    // W3 Geolocation Supported
    if (navigator.geolocation) {
        browserSupportFlag = true;
        navigator.geolocation.getCurrentPosition(function(position){
            latlng = {
                lat: position.coords.latitude,
                lng: position.coords.longitude,
            }
        });
    }
    // Geolocation not supported
    else{
        browserSupportFlag = false;
        console.log('no support')
    }
}

getUserLocation();