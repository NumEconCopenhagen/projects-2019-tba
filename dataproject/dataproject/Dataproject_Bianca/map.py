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
    <style>#map_07d1d5b9ec00463094ddcbb3b577c028 {
        position: relative;
        width: 100.0%;
        height: 100.0%;
        left: 0.0%;
        top: 0.0%;
        }
    </style>
</head>
<body>    
    
    <div class="folium-map" id="map_07d1d5b9ec00463094ddcbb3b577c028" ></div>
</body>
<script>    
    
    
        var bounds = null;
    

    var map_07d1d5b9ec00463094ddcbb3b577c028 = L.map(
        'map_07d1d5b9ec00463094ddcbb3b577c028', {
        center: [56.2639, 9.5018],
        zoom: 6.1,
        maxBounds: bounds,
        layers: [],
        worldCopyJump: false,
        crs: L.CRS.EPSG3857,
        zoomControl: true,
        });


    
    var tile_layer_5bf8e38d30d2492ab45e89d4e1968c49 = L.tileLayer(
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
}).addTo(map_07d1d5b9ec00463094ddcbb3b577c028);
    
            var circle_marker_b6b6766ff5ae40e19ba79b2593e43b79 = L.circleMarker(
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
                .addTo(map_07d1d5b9ec00463094ddcbb3b577c028);
            
    
            var popup_05465acc97e140e996694dbd72288123 = L.popup({maxWidth: '100%'
            
            });

            
                var html_9f3d3debd17a4feb9defbc455ea92880 = $(`<div id="html_9f3d3debd17a4feb9defbc455ea92880" style="width: 100.0%; height: 100.0%;">Denmark</div>`)[0];
                popup_05465acc97e140e996694dbd72288123.setContent(html_9f3d3debd17a4feb9defbc455ea92880);
            

            circle_marker_b6b6766ff5ae40e19ba79b2593e43b79.bindPopup(popup_05465acc97e140e996694dbd72288123)
            ;

            
        
</script>