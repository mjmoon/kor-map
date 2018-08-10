var widthFull = 800,
    aspectRatio = 1,
    mapMargin = {left: 20, right: 20, top: 20, bottom: 20},
    defOpacity = 0.5,
    defStrokewidth = 2;
var ctprvnDiv = d3.select("#ctprvn-nm"),
    sigDiv = d3.select("#sig-nm"),
    emdDiv = d3.select("#emd-nm");
var mainSvg = d3.select("#main-map")
        .append("svg")
        .attr("width", widthFull)
        .attr("height", aspectRatio*widthFull)
        .attr("viewBox", "0,0," + widthFull + "," + widthFull*aspectRatio)
        .attr("preserveAspectRatio", "xMinYMin meet")
        .classed("svg-content-responsive", true),
    map = mainSvg.append("g"),
    ocean = map.append("rect")
        .attr("width", widthFull)
        .attr("height", aspectRatio*widthFull)
        .attr("class", "ocean"),
    color = d3.scaleOrdinal(d3.schemeCategory10);
    currDim = d3.select(".svg-content-responsive").node().getBoundingClientRect(),
    zoom = d3.zoom()
       .scaleExtent([1, 5])
       .translateExtent([[0,0],[widthFull, widthFull*aspectRatio]]),
    currTransform = [0,0],
    initScale = 1;

// Select the tooltip div
var tooltip = d3.select("#tooltip")
        .style("opacity", 0);

// Back button
var back = mainSvg.append("g")
        .classed("back-button", true)
        .attr("transform", "translate(20,20)")
        .style("opacity", 0);
back.append("polyline")
    .attr("points", "0,18 9,0 18,18");
var backText = back.append("text")
        .attr("x", 30)
        .attr("y", 20);

// Read level 1 map data
d3.json('data/plot/kor_admin_1.topojson').then(function(data1){
    var lvl1 = topojson.feature(data1, data1.objects.TL_SCCO_CTPRVN),
        lvl2, lvl3,
        projection = d3.geoNaturalEarth1(),
        path = d3.geoPath()
            .projection(projection);
    lvl1.features.forEach(function(d) { d.id = d.properties.CTPRVN_CD; });

    // reusuable draw function
    function redraw(selected) {
        // hide tooltip
        tooltip.transition()
            .duration(200)
            .style("opacity", 0);
        // refit projection
        projection.fitExtent([
            [mapMargin.left,mapMargin.top],
            [currDim.width - mapMargin.right, currDim.height - mapMargin.bottom]
        ], selected);
        // reset zoom
        mainSvg.transition().duration(750).call(zoom.transform, d3.zoomIdentity);
        initTranslate = projection.translate(),
        initScale = projection.scale();
        // redraw map
        var area = map.selectAll(".area")
                .data(selected.features, function(d) { return d.id; })
        area.exit().remove();
        area.enter().append("path")
            .attr("class", "area")
            .on("mouseover", mouseoverHandler)
            .on("mouseout", mouseoutHandler)
            .on("click", clickHandler)
            .attr("d", path)
            .attr("fill", function(s, i) {
                return (s.properties.LVL_1_EN==null)?"#000000":color(i);
            })
            .style("fill-opacity", defOpacity);
    }
    redraw(lvl1);

    // Read level 2 map data
    d3.json('data/plot/kor_admin_2.topojson').then(function(data2){
        // Read level 3 map data
        d3.json('data/plot/kor_admin_3.topojson').then(function(data3){
            lvl2 = topojson.feature(data2, data2.objects.TL_SCCO_SIG),
            lvl3 = topojson.feature(data3, data3.objects.TL_SCCO_EMD);
            lvl2.features.forEach(function(d) { d.id = d.properties.SIG_CD; });
            lvl3.features.forEach(function(d) { d.id = d.properties.EMD_CD; });
        });
    });

    // mouse interaction handlers
    back
        .on("mouseover", function(){
            if(currRegion.length > 0) { d3.select(this).style("opacity", 1); }
        })
        .on("mouseout", function(){
            if(currRegion.length > 0) { d3.select(this).style("opacity", defOpacity); }
        })
        .on("click", clickoutHandler);
    ocean.on("click", clickoutHandler);
    var currRegion = [];
    function clickHandler(d) {
        switch(currRegion.length){
            case 0:
                back.style("opacity", defOpacity);
                backText.text("전국지도");
                currRegion = [{key: "LVL_1_EN", value: d.properties.LVL_1_EN}];
                redraw(filterGeo(lvl2, currRegion));
                break;
            case 1:
                backText.text(d.properties.LVL_1_KR + " 지도");
                currRegion = [
                    {key: "LVL_1_EN", value: d.properties.LVL_1_EN},
                    {key: "LVL_2_EN", value: d.properties.LVL_2_EN}
                ];
                redraw(filterGeo(lvl3, currRegion));
                break;
            case 2:
                break;
            default:
                throw "unreachable";
        }
    }
    function clickoutHandler() {
        switch(currRegion.length){
            case 2:
                backText.text("전국지도");
                sigDiv.html("");
                currRegion.pop();
                redraw(filterGeo(lvl2, currRegion));
                break;
            case 1:
                back.style("opacity", 0);
                ctprvnDiv.html("");
                currRegion = [];
                redraw(lvl1);
                break;
            case 0:
                break;
            default:
                throw "unreachable";
        }
    }
    function mouseoverHandler(d) {
        // display selected region name
        var tooltipText = d.properties.LVL_1_KR + "<br />" + d.properties.LVL_1_EN;
        ctprvnDiv.html(tooltipText);
        if(currRegion.length>0) {
            tooltipText = d.properties.LVL_2_KR + "<br />" + d.properties.LVL_2_EN;
            sigDiv.html(tooltipText);
        }
        if(currRegion.length>1) {
            tooltipText = d.properties.EMD_KOR_NM + "<br/>" + d.properties.EMD_ENG_NM;
            emdDiv.html(tooltipText);
        }
        tooltip.html(tooltipText);
        tooltip
            .style("left", (d3.mouse(this)[0]) + "px")
            .style("top", (d3.mouse(this)[1] - 28) + "px")
            .raise()
            .transition()
            .duration(200)
            .style("opacity", 0.9);
        // highlight selected region
        d3.select(this).raise();
        d3.select(this)
            .style("stroke-width", 0)
            .style("fill-opacity", 1);
    }
    function mouseoutHandler(d) {
        if(currRegion.length<1) { ctprvnDiv.html(""); }
        if(currRegion.length<2) { sigDiv.html(""); }
        emdDiv.html("");
        tooltip.transition()
            .duration(200)
            .style("opacity", 0);
        d3.select(this)
            .style("stroke-width", defStrokewidth)
            .style("fill-opacity", defOpacity);
    }
    // enable zooming
    function zoomed() {
        var newScale = initScale * d3.event.transform.k;
        projection
            .translate([
                (initTranslate[0] * d3.event.transform.k) + d3.event.transform.x,
                (initTranslate[1] * d3.event.transform.k) + d3.event.transform.y
            ])
            .scale(newScale);
        map.selectAll("path").attr("d", path);
    }
    mainSvg.call(zoom.on("zoom", zoomed));

    // resize on window
    window.addEventListener("resize", function(){
        currDim = d3.select(".svg-content-responsive").node().getBoundingClientRect();
        switch(currRegion.length){
            case 0:
                redraw(lvl1);
                break;
            case 1:
                redraw(filterGeo(lvl2, currRegion));
                break;
            case 2:
                redraw(filterGeo(lvl3, currRegion));
                break;
            default:
                throw "unreachable";
        }
    });
});

// filter to focus on regions
function filterGeo(data, filter) {
    var res = {type: "FeatureCollection"};
    res.features = data.features.filter(function(d) {
        var b = 1;
        filter.forEach(function(f) {
            b = b & (d.properties[f.key]==f.value);
        });
        return b;
    });
    return res;
}

// toggle dark color theme
function toggleTheme() {
    if(d3.select("#k-map").classed("dark")){
        d3.select("#k-map").classed("dark", false);
        defOpacity = 0.5;
        map.selectAll(".area").style("fill-opacity", defOpacity);
    } else {
        d3.select("#k-map").classed("dark", true);
        defOpacity = 0.9;
        map.selectAll(".area").style("fill-opacity", defOpacity);
    }
}
