/**
 * 1-hbnb.js : Manipulates the DOM of 2-hbnb.html
 */

$(function () {
  const amenities = [];

  $('.amenity-check').on('click', function () {
    const amenity = {
      id: $(this).attr('data-id'),
      name: $(this).attr('data-name')
    };

    if ($(this).is(':checked')) {
      amenities.push(amenity);
    } else {
      const amenityIds = amenities.map(a => a.id);
      const index = amenityIds.indexOf(amenity.id);
      if (index > -1) {
        amenities.splice(index, 1);
      }
    }

    // Update the h4 with the list of amenities in the array
    const amenityNames = amenities.map(a => a.name);
    const selectAmenities = amenityNames.join(', ');
    if (selectAmenities.length > 20) {
      $('h4.select-amenities').text(selectAmenities.substring(0, 19) + '...');
    } else {
      $('h4.select-amenities').text(selectAmenities);
    }
  });
  
  $.get('http://0.0.0.0:5001/api/v1/status/', function (resp) {
    if (resp.status === 'OK') {
      $('div#api_status').addClass('available');
    } else {
      $('div#api_status').removeClass('available');
    }
  });
$.ajax({
    type: 'POST',
    url: 'http://0.0.0.0:5001/api/v1/places_search/',
    data: '{}',
    contentType: 'application/json',
    dataType: 'json',
    success: function (data) {
      for (let place of data) {
        $('.places').append('<article><div class="title"><h2>' + place['name'] + '</h2><div class="price_by_night">' + place['price_by_night'] + '</div></div><div class="information"><div class="max_guest"><i class="fa fa-users fa-3x" aria-hidden="true"></i><br />' + place['max_guest'] + ' Guests</div><div class="number_rooms"><i class="fa fa-bed fa-3x" aria-hidden="true"></i><br />' + place['number_rooms'] + ' Bedrooms</div><div class="number_bathrooms"><i class="fa fa-bath fa-3x" aria-hidden="true"></i><br />' + place['number_bathrooms'] + ' Bathroom</div></div><div class="user"><div class="description">' + place['description'] + '</div></article>');
      }
    }
  });
});
