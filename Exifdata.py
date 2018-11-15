#!/usr/bin/env python3
# coding:utf-8

import argparse
import re
import os.path
from PIL import Image
from PIL.ExifTags import TAGS
from geopy.geocoders import Nominatim


# Gathering EXIF Data from image file and outputing result in text file
# Outfile is optionnal and automatically created if omited
def getMetaData(imgname, out=''):
    try:
        metaData = {}
        # Oprening image with Python Image Library (PIL)
        imgFile = Image.open(imgname)
        print(
            "NOTE: Getting Meta Data from '{}'..."
            .format(imgname))
        # Extracting EXIF information
        info = imgFile._getexif()
        # If EXIF data found
        if info:
            print(
                "NOTE: Found Meta Data for '{}'!"
                .format(imgname))

            for (tag, value) in info.items():
                tagname = TAGS.get(tag, tag)
                metaData[tagname] = value

            # If no output file specified,
            # outfile = 'image name + ExifData.txt
            if not out:
                outfile = "{}_ExifData.txt".format(
                    (str(imgname)).strip('.jpg'))

            # if output file specified,
            # output file = user input
            else:
                outfile = out

            print(
                "NOTE: Outputting EXIF Data to file '{}'"
                .format(outfile))
            # Opening output EXIF Data file
            with open(outfile, "w") as f:
                for (tagname, value) in metaData.items():
                    # Writing all Exif Data to output file
                    f.write(str(tagname)+"\t" +
                            str(value)+"\n")

                # Gatehring GPS Information
                lat = [float(x)/float(y)
                       for x, y in metaData['GPSInfo'][2]]
                latref = metaData['GPSInfo'][1]
                lon = [float(x)/float(y)
                       for x, y in metaData['GPSInfo'][4]]
                lonref = metaData['GPSInfo'][3]

                # Translating GPS Data
                lat = lat[0] + lat[1]/60 + lat[2]/3600
                lon = lon[0] + lon[1]/60 + lon[2]/3600
                if latref == 'S':
                    lat = -lat
                if lonref == 'W':
                    lon = -lon
                
                geolocator = Nominatim(user_agent="OpenMapQuest")
                location = geolocator.reverse("{}, {}".format(lat, lon))

                print(location.address)
                print(location.address)

                # Ouputting GPS data to GPS File
                gpsfile = "{}_GPSData.txt".format(
                    (str(imgname)).strip('.jpg'))
                print(
                    "NOTE: Outputting GPS Data to file '{}'"
                    .format(gpsfile))
                with open(gpsfile, "w") as f:
                    f.write("{}, {}\n{}".format(lat, lon, location.address))

                # Outputing Date Time the image was captured to DATE File
                datefile = "{}_CaptureDate.txt".format(
                    (str(imgname)).strip('.jpg'))
                date = metaData['DateTimeOriginal']
                print(
                    "NOTE: Outputting Capture Date to file '{}'"
                    .format(datefile))
                with open(datefile, "w") as f:
                    f.write(date)
        # No EXIF data in image
        else:
            print(
                "WARNING: No EXIF information found")
    except:
        print(
            "ERROR: Failed to process '{}'".format(imgname))


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "imgage", help="name of the JPEG image file to process")
    parser.add_argument(
        "--output", "-o", help="dump EXIF data to output file")
    args = parser.parse_args()
    if not re.findall(r'\.jpg', args.imgage):
        print(
            "WARNING: Input file must be a .jpg file !")
        exit()
    if not os.path.isfile(args.imgage):
        print(
            "WARNING: File: '{}' not found in the current directory !"
            .format(args.imgage))
        exit()
    if args.imgage:
        getMetaData(args.imgage, args.output)
    else:
        print(parser.usage)


if __name__ == '__main__':
    Main()
