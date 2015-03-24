#!/bin/sh

rm -f *City.json *County.json hrCounties.json
rm -f *-topo.json

#shapefile=tl_2013_us_county.shp
#shapefile=cb_2013_us_county_20m.shp
shapefile=cb_2013_us_county_500k.shp
#shapefile=tl_2013_51_cousub.shp

ogr2ogr -f GeoJSON -where "STATEFP IN ( '51' ) AND COUNTYFP IN ( '550', '620', '073', '650', '093', '095', '700', '710', '735', '740', '175', '800', '810', '181', '830', '199' )" hrCounties.json ${shapefile}

#ogr2ogr -f GeoJSON -where "STATEFP IN ( '51' ) AND COUNTYFP IN ( '550' )" chesapeakeCity.json ${shapefile}
#ogr2ogr -f GeoJSON -where "STATEFP IN ( '51' ) AND COUNTYFP IN ( '620' )" franklinCity.json ${shapefile}
#ogr2ogr -f GeoJSON -where "STATEFP IN ( '51' ) AND COUNTYFP IN ( '073' )" gloucesterCounty.json ${shapefile}
#ogr2ogr -f GeoJSON -where "STATEFP IN ( '51' ) AND COUNTYFP IN ( '650' )" hamptonCity.json ${shapefile}
#ogr2ogr -f GeoJSON -where "STATEFP IN ( '51' ) AND COUNTYFP IN ( '093' )" isleOfWightCounty.json ${shapefile}
#ogr2ogr -f GeoJSON -where "STATEFP IN ( '51' ) AND COUNTYFP IN ( '095' )" jamesCityCounty.json ${shapefile}
#ogr2ogr -f GeoJSON -where "STATEFP IN ( '51' ) AND COUNTYFP IN ( '700' )" newportNewsCity.json ${shapefile}
#ogr2ogr -f GeoJSON -where "STATEFP IN ( '51' ) AND COUNTYFP IN ( '710' )" norfolkCity.json ${shapefile}
#ogr2ogr -f GeoJSON -where "STATEFP IN ( '51' ) AND COUNTYFP IN ( '735' )" poquosonCity.json ${shapefile}
#ogr2ogr -f GeoJSON -where "STATEFP IN ( '51' ) AND COUNTYFP IN ( '740' )" portsmouthCity.json ${shapefile}
#ogr2ogr -f GeoJSON -where "STATEFP IN ( '51' ) AND COUNTYFP IN ( '175' )" southhamptonCounty.json ${shapefile}
#ogr2ogr -f GeoJSON -where "STATEFP IN ( '51' ) AND COUNTYFP IN ( '800' )" suffolkCity.json ${shapefile}
#ogr2ogr -f GeoJSON -where "STATEFP IN ( '51' ) AND COUNTYFP IN ( '181' )" surryCounty.json ${shapefile}
#ogr2ogr -f GeoJSON -where "STATEFP IN ( '51' ) AND COUNTYFP IN ( '810' )" virginiaBeachCity.json ${shapefile}
#ogr2ogr -f GeoJSON -where "STATEFP IN ( '51' ) AND COUNTYFP IN ( '830' )" williamsburgCity.json ${shapefile}
#ogr2ogr -f GeoJSON -where "STATEFP IN ( '51' ) AND COUNTYFP IN ( '199' )" yorkCounty.json ${shapefile}

topojson -o hrCounties-topo.json --id-property COUNTYFP --properties name=NAME -- hrCounties.json

#topojson -o chesapeakeCity-topo.json -- chesapeakeCity.json 
#topojson -o franklinCity-topo.json -- franklinCity.json 
#topojson -o gloucesterCounty-topo.json -- gloucesterCounty.json 
#topojson -o hamptonCity-topo.json -- hamptonCity.json 
#topojson -o isleOfWightCounty-topo.json -- isleOfWightCounty.json 
#topojson -o jamesCityCounty-topo.json -- jamesCityCounty.json 
#topojson -o newportNewsCity-topo.json -- newportNewsCity.json 
#topojson -o norfolkCity-topo.json -- norfolkCity.json 
#topojson -o poquosonCity-topo.json -- poquosonCity.json 
#topojson -o portsmouthCity-topo.json -- portsmouthCity.json 
#topojson -o southhamptonCounty-topo.json -- southhamptonCounty.json 
#topojson -o suffolkCity-topo.json -- suffolkCity.json 
#topojson -o surryCounty-topo.json -- surryCounty.json 
#topojson -o virginiaBeachCity-topo.json -- virginiaBeachCity.json 
#topojson -o williamsburgCity-topo.json -- williamsburgCity.json 
#topojson -o yorkCounty-topo.json -- yorkCounty.json 
