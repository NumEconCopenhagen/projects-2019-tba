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
    <style>#map_fd0ab67f426748ee92a83e7fd0affda4 {
        position: relative;
        width: 100.0%;
        height: 100.0%;
        left: 0.0%;
        top: 0.0%;
        }
    </style>
</head>
<body>    
    
    <div class="folium-map" id="map_fd0ab67f426748ee92a83e7fd0affda4" ></div>
</body>
<script>    
    
    
        var bounds = null;
    

    var map_fd0ab67f426748ee92a83e7fd0affda4 = L.map(
        'map_fd0ab67f426748ee92a83e7fd0affda4', {
        center: [0, 0],
        zoom: 2,
        maxBounds: bounds,
        layers: [],
        worldCopyJump: false,
        crs: L.CRS.EPSG3857,
        zoomControl: true,
        });


    
    var tile_layer_ef32c1cc84a642fba89595d0961c48cd = L.tileLayer(
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
}).addTo(map_fd0ab67f426748ee92a83e7fd0affda4);
    

            var circle_5955bfec1c0b45ed8f04e5a4276480fc = L.circle(
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
                .addTo(map_fd0ab67f426748ee92a83e7fd0affda4);
            
    

            var circle_c7faa17d903f4547b526e14c28bad119 = L.circle(
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
                .addTo(map_fd0ab67f426748ee92a83e7fd0affda4);
            
    

            var circle_344da70376fa43e083fb4027c32dd47a = L.circle(
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
                .addTo(map_fd0ab67f426748ee92a83e7fd0affda4);
            
    

            var circle_b6cebfd45cfd4f6db02e06cd9a7efca9 = L.circle(
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
                .addTo(map_fd0ab67f426748ee92a83e7fd0affda4);
            
    

            var circle_7c8979d5648e470c935c17e150a671ed = L.circle(
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
  "radius": 20186.552298132898,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_fd0ab67f426748ee92a83e7fd0affda4);
            
    

            var circle_3d7194c3b487454980aac822239a4cdf = L.circle(
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
                .addTo(map_fd0ab67f426748ee92a83e7fd0affda4);
            
    

            var circle_709df8f57e604cf8a904ace602615bad = L.circle(
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
                .addTo(map_fd0ab67f426748ee92a83e7fd0affda4);
            
    

            var circle_6e5eaca4153f4c4993483b2e3995cf42 = L.circle(
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
                .addTo(map_fd0ab67f426748ee92a83e7fd0affda4);
            
    

            var circle_c7a5977052594f06ba40a50f5095cfe2 = L.circle(
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
  "radius": 725631.104194458,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_fd0ab67f426748ee92a83e7fd0affda4);
            
</script>