/**
 * 1-hbnb.js : Manipulates the DOM of 2-hbnb.html
 */

$(function () {
  $('.amenities .popover input').on('click', function () {
    const amenities = [];
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
    $('.amenities h4').text(selectAmenities);
  });
  $.get('http://0.0.0.0:5001/api/v1/status/', function (resp) {
    if (resp.status === 'OK') {
      $('div#api_status').addClass('available');
    } else {
      $('div#api_status').removeClass('available');
    }
  })
});
