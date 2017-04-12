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
    scale: 1, 
    fillColor: 'blue', 
    fillOpacity: 0.8
  };
  
  map.markers = map.markers || []
  downloadUrl(xmlUrl, function(data) 
  {
      var xml = data.responseXML;
      var promien = 300;
      document.getElementById("promien").innerHTML = promien;
      markers = xml.documentElement.getElementsByTagName("marker");
      for (var i = 0; i < markers.length; i++) 
      {
          var name = markers[i].getAttribute("name");
          var id = markers[i].getAttribute("id");
          var point = new google.maps.LatLng(
              parseFloat(markers[i].getAttribute("lat")),
              parseFloat(markers[i].getAttribute("lng")));
              
          var circle = {
               strokeColor: "#ff0000",
               strokeOpacity: 0.5,
               strokeWeight: 1,
               fillColor: "#ff0000",
               fillOpacity: 0.10,
               map: map,
               center: point,
               radius: promien };
          var drawCirle = new google.maps.Circle(circle);
          
          var marker = new google.maps.Marker(
          {
            map: map,
            position: point,
            title: name,
            icon: marker_icon
          });
          marker.addListener('click', function() {
          infoWindow.setContent(point.lat() +" " + point.lng());
          infoWindow.open(map, this);
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
        zoom: 12,
        center: myLatlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
    }
    geocoder = new google.maps.Geocoder();
    infoWindow = new google.maps.InfoWindow;
    map = new google.maps.Map(document.getElementById('map'), mapOptions);
      
    xmlUrl = "moje.xml";
     
    loadMarkers(); 
    
    var drawCirle = new google.maps.Circle({
           fillColor: "#000000",
           fillOpacity: 1,
           map: map,
           center: new google.maps.LatLng(52.232614, 21.080031),
           radius: 150 });
}

google.maps.event.addDomListener(window, 'load', initialise)
