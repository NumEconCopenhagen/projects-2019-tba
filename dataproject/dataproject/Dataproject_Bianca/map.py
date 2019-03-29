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
    <style>#map_a4de8a884bf94cb9b1901fff514a0260 {
        position: relative;
        width: 100.0%;
        height: 100.0%;
        left: 0.0%;
        top: 0.0%;
        }
    </style>
</head>
<body>    
    
    <div class="folium-map" id="map_a4de8a884bf94cb9b1901fff514a0260" ></div>
</body>
<script>    
    
    
        var bounds = null;
    

    var map_a4de8a884bf94cb9b1901fff514a0260 = L.map(
        'map_a4de8a884bf94cb9b1901fff514a0260', {
        center: [56.2639, 9.5018],
        zoom: 6.1,
        maxBounds: bounds,
        layers: [],
        worldCopyJump: false,
        crs: L.CRS.EPSG3857,
        zoomControl: true,
        });


    
    var tile_layer_84b8877b956d422b88da604ac6da639b = L.tileLayer(
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
}).addTo(map_a4de8a884bf94cb9b1901fff514a0260);
    
            var circle_marker_036eb0207dd645e4b5c65788de64ba5d = L.circleMarker(
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
  "radius": 30,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_a4de8a884bf94cb9b1901fff514a0260);
            
    
            var popup_e67403d5f3934a889763b499c2b93110 = L.popup({maxWidth: '100%'
            
            });

            
                var html_7b0f5cd96b784baab92ea43d530256ee = $(`<div id="html_7b0f5cd96b784baab92ea43d530256ee" style="width: 100.0%; height: 100.0%;">Denmark</div>`)[0];
                popup_e67403d5f3934a889763b499c2b93110.setContent(html_7b0f5cd96b784baab92ea43d530256ee);
            

            circle_marker_036eb0207dd645e4b5c65788de64ba5d.bindPopup(popup_e67403d5f3934a889763b499c2b93110)
            ;

            
        
</script>