function downloadUrl(url,callback) {
  var request = window.ActiveXObject ?
       new ActiveXObject('Microsoft.XMLHTTP') :
       new XMLHttpRequest;
   
  request.onreadystatechange = function() {
      if (request.readyState == 4) {
          //request.onreadystatechange = doNothing;
          callback(request, request.status);
      }
  };
   
  request.open('GET', url, true);
  request.send(null);
}

function loadMarkers() {
    map.markers = map.markers || []
    downloadUrl(xmlUrl, function(data)) {
        var xml = data.responseXML;
        markers = xml.documentElement.getElementsByTagName("marker");
        for (var i = 0; i < markers.length; i++) {
            var name = markers[i].getAttribute("name");
            //var marker_image = markers[i].getAttribute('markerimage');
            var id = markers[i].getAttribute("id");
            var address = markers[i].getAttribute("address1")+"<br />"+markers[i].getAttribute("address2")+"<br />"+markers[i].getAttribute("address3")+"<br />"+markers[i].getAttribute("postcode");
            /*var image = {
              url: marker_image,
              size: new google.maps.Size(71, 132),
              origin: new google.maps.Point(0, 0),
              scaledSize: new google.maps.Size(71, 132)
            };*/
            var point = new google.maps.LatLng(
                parseFloat(markers[i].getAttribute("lat")),
                parseFloat(markers[i].getAttribute("lng")));
            var html = "<div class='infowindow'><b>" + name + "</b> <br/>" + address+'<br/></div>';
            var marker = new google.maps.Marker({
              map: map,
              position: point,
              icon: {path: google.maps.SymbolPath.CIRCLE, scale: 5, fillColor: 'red',
		fillOpacity: 0.8, strokeColor: 'gold',strokeWeight: 1 },
        map: map
      }); 
              title: name
            });
            map.markers.push(marker);
            bindInfoWindow(marker, map, infoWindow, html);
        }
    });
}
    
function initialise() {
    myLatlng = new google.maps.LatLng(54.559323,-3.321304);
    mapOptions = {
        zoom: 5,
        center: myLatlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
    }
    geocoder = new google.maps.Geocoder();
    infoWindow = new google.maps.InfoWindow;
    map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
     
    xmlUrl = "markers.xml";
     
    loadMarkers();  
}
initialise();
google.maps.event.addDomListener(window, 'load', initialise)