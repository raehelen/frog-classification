# import the necessary packages
import cv2, os, sqlite3
import names
import argparse
from thresholdbinary import *
from Featuredetect import *
from cascadefile import *
from time import gmtime, strftime

#construct the argument parser and parse the arguments
parser = argparse. ArgumentParser(
             description = "Script to simplify the use of the FrogFinder programme")
parser.add_argument("-i", "--input", required = True,
        help = "Path to input image")
parser.add_argument("-lat", "--latitude", required = True,
        help = "Latitude coordinates")
parser.add_argument("-long", "--longitude", required = True,
        help = "Longitude coordinates")
args = vars(parser.parse_args())



# open connection to database
conn = sqlite3.connect('C:/Python27/jonny/frogs.db')
c = conn.cursor()
c2 = conn.cursor()

# get current date and time
d = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# somehow set path here for input image
#imgPath = './frog9.jpg'
imgPath = (args["input"])

#open the input image
img = cv2.imread(imgPath)

#find the frog and crop it out of the image
cropped = doCascade(img)

# threshold the cropped image to binary
thresholded = doThreshold(cropped)

                    
# find the best match in our database
bestMatch = ""
maxMatches = 0
minMatches = 4

for template in os.listdir("frog_templates/"):

    # only interested in jpgs
    if template.endswith(".jpg"):
        
        
        templateimg = cv2.imread("frog_templates/" + template)
        
        nMatches = doHomography(templateimg, thresholded)
        
        if nMatches > maxMatches:
                bestMatch = template
                maxMatches = nMatches

#if the best is good enough, record the sighting
if maxMatches > minMatches:
    print "This frog is already in our database!"

    longitude = args["longitude"]
    latitude = args["latitude"]

    #that's your frog!
    c.execute("INSERT INTO sightings (longitude, latitude, time) VALUES (?, ?, ?)", (longitude, latitude, d,))
     
    
#otherwise, create new frog, and record the sighting
else:
    print "This is a new frog called "+str(names.get_full_name())
    
    name = names.get_full_name() # from your name generator
    image_path = './frog_templates/' + name + '.jpg' # where you saved the new template to
    cv2.imwrite(image_path, thresholded)

    longitude = args["longitude"]
    latitude = args["latitude"]

    #it's a new frog!
    c.execute("INSERT INTO frogs (name, image_path) VALUES (?, ?)", (name, image_path,))
    c2.execute("INSERT INTO sightings (longitude, latitude, time) VALUES (?, ?, ?)", (longitude, latitude, d,))
   

# Save (commit) the changes
conn.commit()

# close the connection
conn.close()
