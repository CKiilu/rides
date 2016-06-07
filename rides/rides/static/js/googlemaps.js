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
                    data = JSON.parse(data);
                    if (data.products) {
                        data = data.products;
                        $('#response').empty();
                        for (val in data) {
                            $('#response').append('<h3>Product '+(+val+1)+'</h3>');
                            $('#response').append('<p>Capacity: ' + data[val].capacity + '</p>');
                            $('#response').append('<p>Description: ' + data[val].description + '</p>');
                            $('#response').append('<p>Product Name: ' + data[val].display_name + '</p>');
                            $('#response').append('<h4>Price details</h4>');
                            $('#response').append('<p>Price Details: Cost per distance - ' + data[val].price_details.cost_per_distance + 'km  Cost per Minute - ' + data[val].price_details.cost_per_minute + '</p>');
                        }
                    }
                    else if (data.times) {
                        data = data.times;
                        $('#response').empty();
                        for (val in data) {
                            $('#response').append('<h3>Time '+(+val+1)+'</h3>');
                            $('#response').append('<p>Localized Product Name: ' + data[val].localized_display_name + '</p>');
                            $('#response').append('<p>Estimate: ' + data[val].estimate + '</p>');
                            $('#response').append('<p>Product Name: ' + data[val].display_name + '</p>');
                            $('#response').append('<p>Product ID: ' + data[val].product_id + '</p>');
                        }
                    }
                    else if (data.prices) {
                        data = data.prices;
                        $('#response').empty();
                        for (val in data) {
                            $('#response').append('<h3>Price '+(+val+1)+'</h3>');
                            $('#response').append('<p>Distance: ' + data[val].distance + ' km</p>');
                            $('#response').append('<p>Estimate: ' + data[val].estimate + '</p>');
                            $('#response').append('<p>Duration: ' + data[val].duration + ' minutes</p>');
                        }
                    }
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