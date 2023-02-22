/**
 * 1-hbnb.js : Manipulates the DOM of 1-hbnb.html
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
});
