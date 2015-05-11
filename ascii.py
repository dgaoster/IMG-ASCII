'''
ASCII Art maker
Creates an ascii art image from an arbitrary image
Created on 7 Sep 2009
 
@author: Steven Kay (Modified by David Gao.)
'''
 
from PIL import Image
import random
from bisect import bisect
 
# greyscale = [                     # ORIGINAL
#             " ",
#             " ",
#             ".,-",
#             "_ivc=!/|\\~",
#             "gjez2]/(YL)t[+T7Vf",
#             "mdK4ZGbNDXY5P*Q",
#             "W8KMA",
#             "#%$"
#             ]

greyscale = [                     
            " ",
            " ",
            ".,-",
            "_ivc=!/|\\~",
            "gjez2]/(YL)t[+T7Vf",
            "mdK4ZGbNDXY5P*Q",
            "@",
            "#%$"
            ]

zonebounds = [36,72,108,144,180,216,252]
"***CHOOSE IMAGE HERE***"
""" im = Image.open("<insert directory>") """
#im = Image.open("/Users/DavidGao/Documents/ProfilePic.jpg")
im = Image.open("/Users/DavidGao/Downloads/pusheen1.png")
#im = Image.open("/Users/DavidGao/Downloads/pusheen-laptop.jpg")
#im = Image.open("/Users/DavidGao/Downloads/pusheen scooter.jpg")
im = im.resize((160, 75), Image.BILINEAR)
im = im.convert("L") # convert to mono
 
str = ""
for y in range(0,im.size[1]):
    for x in range(0,im.size[0]):
        lum = 255 - im.getpixel((x,y))
        row = bisect(zonebounds,lum)
        possibles = greyscale[row]
        str += possibles[random.randint(0, len(possibles) - 1)]
    str += "\n"
 
print(str) #final output



