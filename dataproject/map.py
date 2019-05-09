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
    <style>#map_951bb6f7f8124d8dba1ffef77936d5bc {
        position: relative;
        width: 100.0%;
        height: 100.0%;
        left: 0.0%;
        top: 0.0%;
        }
    </style>
</head>
<body>    
    
    <div class="folium-map" id="map_951bb6f7f8124d8dba1ffef77936d5bc" ></div>
</body>
<script>    
    
    
        var bounds = null;
    

    var map_951bb6f7f8124d8dba1ffef77936d5bc = L.map(
        'map_951bb6f7f8124d8dba1ffef77936d5bc', {
        center: [0, 0],
        zoom: 2,
        maxBounds: bounds,
        layers: [],
        worldCopyJump: false,
        crs: L.CRS.EPSG3857,
        zoomControl: true,
        });


    
    var tile_layer_a2a2b4ded3664164aed793b6a229ef08 = L.tileLayer(
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
}).addTo(map_951bb6f7f8124d8dba1ffef77936d5bc);
    

            var circle_8e461eb51bb74492a442a2e620ef0913 = L.circle(
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
  "radius": 168362.3112440325,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_951bb6f7f8124d8dba1ffef77936d5bc);
            
    

            var circle_e1d2d24ea22743779f726f06c8f2f847 = L.circle(
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
  "radius": 68407.68879013935,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_951bb6f7f8124d8dba1ffef77936d5bc);
            
    

            var circle_7c30cb204d3f4955b8ff46678abe102c = L.circle(
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
  "radius": 870621.1683684015,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_951bb6f7f8124d8dba1ffef77936d5bc);
            
    

            var circle_e3284d49da16438991fa39256d99a5be = L.circle(
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
  "radius": 461049.417796218,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_951bb6f7f8124d8dba1ffef77936d5bc);
            
    

            var circle_66affffa3d634341a8759a6acd39f8e7 = L.circle(
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
  "radius": 20418.0535683165,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_951bb6f7f8124d8dba1ffef77936d5bc);
            
    

            var circle_7e3deba33374461693cc50bce5d15e5d = L.circle(
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
  "radius": 667615.145788758,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_951bb6f7f8124d8dba1ffef77936d5bc);
            
    

            var circle_3a7f853885c641dc8e953dd442cd27f2 = L.circle(
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
  "radius": 34370.400196587754,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_951bb6f7f8124d8dba1ffef77936d5bc);
            
    

            var circle_6b3827695edc45c69f0439c3938ec45f = L.circle(
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
  "radius": 66588.04500326354,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_951bb6f7f8124d8dba1ffef77936d5bc);
            
    

            var circle_9e11e439ce3e4a00aa707fcdd3fd25d7 = L.circle(
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
  "radius": 727002.3153721425,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_951bb6f7f8124d8dba1ffef77936d5bc);
            
</script>