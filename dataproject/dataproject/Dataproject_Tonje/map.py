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
    <style>#map_1890221cfb5e4fdeaa128969b81ec2f7 {
        position: relative;
        width: 100.0%;
        height: 100.0%;
        left: 0.0%;
        top: 0.0%;
        }
    </style>
</head>
<body>    
    
    <div class="folium-map" id="map_1890221cfb5e4fdeaa128969b81ec2f7" ></div>
</body>
<script>    
    
    
        var bounds = null;
    

    var map_1890221cfb5e4fdeaa128969b81ec2f7 = L.map(
        'map_1890221cfb5e4fdeaa128969b81ec2f7', {
        center: [0, 0],
        zoom: 2,
        maxBounds: bounds,
        layers: [],
        worldCopyJump: false,
        crs: L.CRS.EPSG3857,
        zoomControl: true,
        });


    
    var tile_layer_dd0def8416a54140bd4fb034794fbecc = L.tileLayer(
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
}).addTo(map_1890221cfb5e4fdeaa128969b81ec2f7);
    

            var circle_f70eaab0c74a4f6a99a3b938529fb5fd = L.circle(
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
                .addTo(map_1890221cfb5e4fdeaa128969b81ec2f7);
            
    

            var circle_a08f022e51c2432b9aa3d1adf76cce90 = L.circle(
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
                .addTo(map_1890221cfb5e4fdeaa128969b81ec2f7);
            
    

            var circle_8c8a83b55c9f49cb82d764eeb7fef4ec = L.circle(
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
                .addTo(map_1890221cfb5e4fdeaa128969b81ec2f7);
            
    

            var circle_4a36780649a245bb88a9dd22e9326383 = L.circle(
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
                .addTo(map_1890221cfb5e4fdeaa128969b81ec2f7);
            
    

            var circle_7a280c86d5614fffb3c57fb05da6e711 = L.circle(
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
                .addTo(map_1890221cfb5e4fdeaa128969b81ec2f7);
            
    

            var circle_6fb0d90bfa88420f839643a1663b9df7 = L.circle(
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
                .addTo(map_1890221cfb5e4fdeaa128969b81ec2f7);
            
    

            var circle_00309a5c98f14181b1a1a0f33b6d596c = L.circle(
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
                .addTo(map_1890221cfb5e4fdeaa128969b81ec2f7);
            
    

            var circle_162d9edeed8549adae65621a78ce2c28 = L.circle(
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
                .addTo(map_1890221cfb5e4fdeaa128969b81ec2f7);
            
    

            var circle_ac4eb56243cd47ba9bb0e80b6a9c6a9d = L.circle(
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
                .addTo(map_1890221cfb5e4fdeaa128969b81ec2f7);
            
</script>