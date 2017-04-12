function downloadUrl(url,callback) {
  var request = window.ActiveXObject ?
       new ActiveXObject('Microsoft.XMLHTTP') :
       new XMLHttpRequest;
   
  request.onreadystatechange = function() 
  {
      if (request.readyState == 4) 
      {
          callback(request, request.status);
      }
  };
   
  request.open('GET', url, true);
  request.send(null);
}

function loadMarkers() 
{
  var marker_icon =
  {
    path: google.maps.SymbolPath.CIRCLE, 
    scale: 2, 
    fillColor: 'blue', 
    fillOpacity: 0.8, 
    strokeColor: 'blue'//,
    //strokeWeight: 1 
  };
  
  map.markers = map.markers || []
  downloadUrl(xmlUrl, function(data) 
  {
      var xml = data.responseXML;
      
      markers = xml.documentElement.getElementsByTagName("marker");
      for (var i = 0; i < markers.length; i++) 
      {
          var name = markers[i].getAttribute("name");
          var id = markers[i].getAttribute("id");
          var point = new google.maps.LatLng(
              parseFloat(markers[i].getAttribute("lat")),
              parseFloat(markers[i].getAttribute("lng")));
          
          var marker = new google.maps.Marker(
          {
            map: map,
            position: point,
            title: name,
            icon: marker_icon
          });
          map.markers.push(marker);
          document.getElementById("licznik").innerHTML = i;
      }
  });
}

function initialise() 
{
    myLatlng = new google.maps.LatLng(52.241453, 21.033378);
    mapOptions = {
        zoom: 11,
        center: myLatlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
    }
    geocoder = new google.maps.Geocoder();
    infoWindow = new google.maps.InfoWindow;
    map = new google.maps.Map(document.getElementById('map'), mapOptions);
      
    xmlUrl = "wybrane.xml";
     
    loadMarkers(); 
}

google.maps.event.addDomListener(window, 'load', initialise)
