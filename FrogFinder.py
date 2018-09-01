# import the necessary packages
import cv2, os, sqlite3
import names
from thresholdbinary import *
from Featuredetect import *
from cascadefile import *
from time import gmtime, strftime


# open connection to database
conn = sqlite3.connect('C:/Python27/jonny/frogs.db')
c = conn.cursor()

# get current date and time
d = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# somehow set path here for input image
imgPath = './frog1.jpg'

#open the input image
img = cv2.imread(imgPath)

#find the frog and crop it out of the image
cropped = doCascade(img)

# threshold the cropped image to binary
thresholded = doThreshold(cropped)

                    
# find the best match in our database
bestMatch = ""
maxMatches = 0
minMatches = 20

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

    #that's your frog!
    c.execute("INSERT INTO sightings (longitude, latitude, time) VALUES (-81.772342, 8.35217, ?)", (d,))
   
    
#otherwise, create new frog, and record the sighting
else:
    print "This is a new frog called "+str(names.get_full_name())
    name = names.get_full_name() # from your name generator
    image_path = './frog_templates/' + name + '.jpg' # where you saved the new template to
    cv2.imwrite(image_path, thresholded)

    #it's a new frog!
    c.execute("INSERT INTO frogs (name, image_path) VALUES (?, ?)", (name, image_path,))
    c.execute("INSERT INTO sightings (longitude, latitude, time) VALUES (-81.772342, 8.35217, ?)", (d,))
 

# Save (commit) the changes
conn.commit()

# close the connection
conn.close()
