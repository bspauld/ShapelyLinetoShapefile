

import os, sys

import fiona
from fiona.crs import from_epsg
from shapely.geometry import mapping, Point, Polygon, LineString

import datetime as dt
from datetime import timedelta,datetime


inputFile = open('C:/Work/temp/test.txt', 'r')

outpath = 'C:/Work/temp/'


#output shapefile
outShape = 'LineTest.shp'


print("input and output files set")

#empty list for the data in the text file
datalist = []

#output crs
crs = fiona.crs.from_epsg(4326)

schema = {
        'geometry': 'LineString',
        'properties': {'LineID': 'int','PointID':'int','Lon':'float','Lat':'float',},
    }


datalist = [line.split(' ') for line in inputFile.readlines()]


print ((len(datalist)))


with fiona.open(outpath+outShape, 'w', driver='ESRI Shapefile',crs = crs, schema = schema) as c:
    for i in range(len(datalist)):
        lineID = datalist[i][0]
        pointID = datalist[i][1]

        lonVal = float(datalist[i][2])
        latVal = float(datalist[i][3])

        lonVal2 = float(datalist[i+1][2])
        latVal2 = float(datalist[i+1][3])

        Point1 = Point(lonVal,latVal)
        Point2 = Point(lonVal2,latVal2)


        linestring = LineString([Point1,Point2])

        c.write({
                        'geometry': mapping(linestring),
                        'properties': {'LineID': lineID,'PointID':pointID,'Lon':lonVal,'Lat':latVal, },
                        })

c.close()
