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
    <style>#map_f49f8abbbb6945958480952d0d25f959 {
        position: relative;
        width: 100.0%;
        height: 100.0%;
        left: 0.0%;
        top: 0.0%;
        }
    </style>
</head>
<body>    
    
    <div class="folium-map" id="map_f49f8abbbb6945958480952d0d25f959" ></div>
</body>
<script>    
    
    
        var bounds = null;
    

    var map_f49f8abbbb6945958480952d0d25f959 = L.map(
        'map_f49f8abbbb6945958480952d0d25f959', {
        center: [0, 0],
        zoom: 2,
        maxBounds: bounds,
        layers: [],
        worldCopyJump: false,
        crs: L.CRS.EPSG3857,
        zoomControl: true,
        });


    
    var tile_layer_d9864ad1215340e5b5ad6bd91a352a92 = L.tileLayer(
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
}).addTo(map_f49f8abbbb6945958480952d0d25f959);
    

            var circle_5018377d488e4a079d1cd689ea4dde6b = L.circle(
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
                .addTo(map_f49f8abbbb6945958480952d0d25f959);
            
    

            var circle_23d2240fcb6648fe86da6757ae75e567 = L.circle(
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
                .addTo(map_f49f8abbbb6945958480952d0d25f959);
            
    

            var circle_71bf58faa68f44f7abb4e11689c50dbe = L.circle(
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
                .addTo(map_f49f8abbbb6945958480952d0d25f959);
            
    

            var circle_5600cbf0891a4a13a214e687001c1d31 = L.circle(
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
                .addTo(map_f49f8abbbb6945958480952d0d25f959);
            
    

            var circle_4761c415c4a54d648fde49bc7812b441 = L.circle(
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
                .addTo(map_f49f8abbbb6945958480952d0d25f959);
            
    

            var circle_3df25b80a9f245a383aa47b947484daa = L.circle(
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
                .addTo(map_f49f8abbbb6945958480952d0d25f959);
            
    

            var circle_cd59dc4711c540fcb10c854986c0620e = L.circle(
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
                .addTo(map_f49f8abbbb6945958480952d0d25f959);
            
    

            var circle_319a12e0d86b44de82106a3cef27131b = L.circle(
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
                .addTo(map_f49f8abbbb6945958480952d0d25f959);
            
    

            var circle_24aeb9e52e714e7fbccf87287734c797 = L.circle(
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
                .addTo(map_f49f8abbbb6945958480952d0d25f959);
            
</script>