<!DOCTYPE html>
<head>    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    <script>L_PREFER_CANVAS=false; L_NO_TOUCH=false; L_DISABLE_3D=false;</script>
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.4.0/dist/leaflet.js"></script>
    <script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.4.0/dist/leaflet.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://rawcdn.githack.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css"/>
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
    
    <meta name="viewport" content="width=device-width,
        initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <style>#map_415cfa49ff874db0b42c11cec093237e {
        position: relative;
        width: 100.0%;
        height: 100.0%;
        left: 0.0%;
        top: 0.0%;
        }
    </style>
</head>
<body>    
    
    <div class="folium-map" id="map_415cfa49ff874db0b42c11cec093237e" ></div>
</body>
<script>    
    
    
        var bounds = null;
    

    var map_415cfa49ff874db0b42c11cec093237e = L.map(
        'map_415cfa49ff874db0b42c11cec093237e', {
        center: [56.2639, 9.5018],
        zoom: 6.1,
        maxBounds: bounds,
        layers: [],
        worldCopyJump: false,
        crs: L.CRS.EPSG3857,
        zoomControl: true,
        });


    
    var tile_layer_7aba433dd23e430991eccc8c527ddc02 = L.tileLayer(
        'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        {
        "attribution": null,
        "detectRetina": false,
        "maxNativeZoom": 18,
        "maxZoom": 18,
        "minZoom": 0,
        "noWrap": false,
        "opacity": 1,
        "subdomains": "abc",
        "tms": false
}).addTo(map_415cfa49ff874db0b42c11cec093237e);
    
            var circle_marker_bdbcf23554b5458a9e35be12d130b5f3 = L.circleMarker(
                [56.2639, 9.5018],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": false,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 23,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_415cfa49ff874db0b42c11cec093237e);
            
    
            var popup_a9280ac850e5411e9e86b539bc6f185e = L.popup({maxWidth: '100%'
            
            });

            
                var html_ee386e0acd934db1a8c53eaf82741694 = $(`<div id="html_ee386e0acd934db1a8c53eaf82741694" style="width: 100.0%; height: 100.0%;">Denmark</div>`)[0];
                popup_a9280ac850e5411e9e86b539bc6f185e.setContent(html_ee386e0acd934db1a8c53eaf82741694);
            

            circle_marker_bdbcf23554b5458a9e35be12d130b5f3.bindPopup(popup_a9280ac850e5411e9e86b539bc6f185e)
            ;

            
        
</script>