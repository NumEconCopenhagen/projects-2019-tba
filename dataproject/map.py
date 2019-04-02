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
    <style>#map_aa87fc3786184dcabc69fa513977d5d0 {
        position: relative;
        width: 100.0%;
        height: 100.0%;
        left: 0.0%;
        top: 0.0%;
        }
    </style>
</head>
<body>    
    
    <div class="folium-map" id="map_aa87fc3786184dcabc69fa513977d5d0" ></div>
</body>
<script>    
    
    
        var bounds = null;
    

    var map_aa87fc3786184dcabc69fa513977d5d0 = L.map(
        'map_aa87fc3786184dcabc69fa513977d5d0', {
        center: [0, 0],
        zoom: 2,
        maxBounds: bounds,
        layers: [],
        worldCopyJump: false,
        crs: L.CRS.EPSG3857,
        zoomControl: true,
        });


    
    var tile_layer_b6ce296db79d41e6b1bf6f081a078f20 = L.tileLayer(
        'https://{s}.tiles.mapbox.com/v3/mapbox.world-bright/{z}/{x}/{y}.png',
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
}).addTo(map_aa87fc3786184dcabc69fa513977d5d0);
    

            var circle_b2e512c543d642a4935b2a3ba88fee4d = L.circle(
                [-14.235, -51.9253],
                {
  "bubblingMouseEvents": true,
  "color": "green",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "green",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 112241.540829355,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_aa87fc3786184dcabc69fa513977d5d0);
            
    

            var circle_4c965877b8cd49c1bc27c1d98a5f3d74 = L.circle(
                [33.5449, 103.149],
                {
  "bubblingMouseEvents": true,
  "color": "green",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "green",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 45605.1258600929,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_aa87fc3786184dcabc69fa513977d5d0);
            
    

            var circle_a6db735231f245ca85e35e9f61355d44 = L.circle(
                [56.2639, 9.5018],
                {
  "bubblingMouseEvents": true,
  "color": "green",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "green",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 580414.112245601,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_aa87fc3786184dcabc69fa513977d5d0);
            
    

            var circle_a7a206ed58c3441fabea59c846d7e744 = L.circle(
                [40.4637, -3.7492],
                {
  "bubblingMouseEvents": true,
  "color": "green",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "green",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 307366.278530812,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_aa87fc3786184dcabc69fa513977d5d0);
            
    

            var circle_0b35169311af4074ad0bf232d87d9d11 = L.circle(
                [20.5937, 78.9629],
                {
  "bubblingMouseEvents": true,
  "color": "green",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "green",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 13457.701532088598,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_aa87fc3786184dcabc69fa513977d5d0);
            
    

            var circle_29b4425af6db4169815cd6b6469951ba = L.circle(
                [36.2048, 138.2529],
                {
  "bubblingMouseEvents": true,
  "color": "green",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "green",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 445076.763859172,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_aa87fc3786184dcabc69fa513977d5d0);
            
    

            var circle_399e818ec1cb417cbbde02dfdc31bc69 = L.circle(
                [9.082, 8.6753],
                {
  "bubblingMouseEvents": true,
  "color": "green",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "green",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 22913.6001310585,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_aa87fc3786184dcabc69fa513977d5d0);
            
    

            var circle_bac8866c346e468d9a38fa12e1faebd4 = L.circle(
                [38.9697, 59.5563],
                {
  "bubblingMouseEvents": true,
  "color": "green",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "green",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 44392.0300021757,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_aa87fc3786184dcabc69fa513977d5d0);
            
    

            var circle_062c1bd372cf4dff856e105dcf765f41 = L.circle(
                [37.0902, -95.7129],
                {
  "bubblingMouseEvents": true,
  "color": "green",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "green",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 483754.069462972,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_aa87fc3786184dcabc69fa513977d5d0);
            
</script>