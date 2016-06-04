var req_type;


$('button').click(function() {
    var cur_class = $(this).attr('class');
    if (cur_class == "products") {
        req_type = 'products';
    }
    else if (cur_class == "price") {
        req_type = 'price';
    }
    else if (cur_class == "time") {
        req_type = 'time';
    }
});


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
        if (req_type) {
            getUserLocation(latlng);
        }
    });
}

function getUserLocation(end) {
    var browserSupportFlag = new Boolean();
    var initialLocation;
    var latlng;
    // W3 Geolocation Supported
    if (navigator.geolocation) {
        browserSupportFlag = true;
        navigator.geolocation.getCurrentPosition(function(position) {
            latlng = {
                lat: position.coords.latitude,
                lng: position.coords.longitude,
            }
            $.ajax({
                type: 'GET',
                url: '/coords/',
                data: {
                    start: latlng,
                    end: end,
                    type: req_type
                },
                success: function(data) {
                    $('#response').text(data);
                },
            })
        });
    }
    // Geolocation not supported
    else {
        browserSupportFlag = false;
        console.log('no support')
    }
}