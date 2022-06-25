'#############################################'
'################### TITAN ###################'
'#############################################'
'### open-source numworks sprite generator ###'
'#############################################'

# importing modules
from PIL import Image # importing 'PIL' module for computing images

# declaring variables
PAL = list() # declare list for store pixels RGB

width = 0 # declare int for store width of the image
height = 0 # declare int for store height of the image

path = str(input("Input the name of your file (with the extention) or type {!help} to see more infos")) # set the File-path to user image

# show documentation
if(path == "!help"): # verify if the command !help as been taped
    print("Extentions supported : ")
    print(".jpg")
    print(".png")
    print(".ico")
    print("-----------------------")
    print("Warning : ")
    print("- Your image must be in {/Resources} folder.")
    print("- Your image must be smaller than 13x13 (otherwise it will be too heavy for your calculator).")
    print("- Dont reduce the colors number of your image, the process take every RGB of every pixel, so that dont have effects on performances. ")
# generate list with the Path arguments
else:
    print("generating...")

# get informations from the image and convert it of 'RGBA' to 'RGB' for be supported by numworks
    picture = Image.open('Resources/' + path)
    picture = picture.convert('RGB')
    width = picture.size[0]
    height = picture.size[1]
# proccessing the image
    for y in range(0, height):
        for x in range(0, width):

            RGB = picture.getpixel((x,y))
            R,G,B = RGB
            PAL.append(RGB)
    print("Code#0000 : Sprite successfully generated !")


# generate the source-code for driving the Sprite
def generateSprite():
# checking user preferences
    # WARNING : all the options take extra memory, to optimise your workflow, please use just what you need !
    generateComments = input("Do you want to generate comments ? (true/false)") # if set to true, this will generate simples comments in the Sprite source-code to help devs to modify it
    generateSizeSecurity = input("Do you want to generate size-security ? (true/false)") # if set to true, when a scale smaller than '0' will be input, this will rescale the matrice at '1' to avoid errors
    generateCollision = input("Do you want to generate convex-collision ? (true/false)") # if set to true, this will generate collision that can return a direction for the implementation of physics
    generateTrigger = input("Do you want to generate trigger-collision ? (true/false)") # if set to true, this will generate a simple, non directional collision, for triggering actions

# show code in the console with the user customs args
    if str(input("Here are your settings :  generateComments="+generateComments+"   generateSizeSecurity="+generateSizeSecurity+"   generateCollision="+generateCollision+"   generateTrigger="+generateTrigger+"   If you are ok with these settings, just tape {done}")):
        if generateComments == "true":
            print("# importing graphical module")
        print("from kandinsky import *")
        print("")
        if generateComments == "true":
            print("#fuction called by the others modules")
        print("def draw(x,y,scale):")
        if generateComments == "true":
            print("#declaring variables")
        print("  i = 0")
        print("  sprite = " + str(PAL))
        print("")
        print("  img_width = " + str(width))
        print("  img_height = " + str(height))
        print("  internalX = 0")
        print("  internalY = 0")
        print("")
        # security system
        if generateSizeSecurity == "true":
            print("  if scale < 1:")
            print("    scale = 1")
        if generateComments == "true":
            print("#pixels-matrices")
        print("  while i < " + str(height*width) + ":")
        if generateComments == "true":
            print("#draw 'X' pixels")
        print("    if internalX < (img_width*scale):")
        print("      if color(sprite[i]) == color(1,1,1):")
        print("        internalX += (1*scale)")
        print("        i += 1")
        print("      else:")
        print("        fill_rect(internalX+x,internalY+y,scale,scale,sprite[i])")
        print("        internalX += (1*scale)")
        print("        i += 1")
        print("    else:")
        if generateComments == "true":
            print("#draw 'Y' pixels")
        print("      internalX = 0")
        print("      internalY += (1*scale)")
        print("")
        # trigger collision
        if(generateTrigger == "true"):
            print("def triggerCollision(originX,originY,x,y,scale):")
            print("  img_width = " + str(width))
            print("  img_height = " + str(height))
            print("  if originX < x < originX+(img_width*scale):")
            print("    if originY < y < originY+(img_height*scale):")
            print("        return True")
            print("    else:")
            print("      return False")
            print("  else:")
            print("    return False")
        # convex collision
        if(generateCollision == "true"):
            print("def ConvexCollision(originX,originY,x,y,scale):")
            print("  img_with = 13")
            print("  img_height = 13")
            print("")
            print("  if (originX+(img_with*scale))-((img_with*scale)/4) < x < originX+(img_with*scale):")
            print("    if originY < y < originY+(img_height*scale):")
            print("      return 'right'")
            print("  else:")
            print("    if originX < x < (originX+(img_with*scale)/4):")
            print("      if originY < y < originY+(img_height*scale):")
            print("        return 'left'")
            print("    else:")
            print("      if originY < y < originY+(img_height*scale/4):")
            print("        if originX < x < originX+(img_with*scale):")
            print("          return 'up'")
            print("      else:")
            print("        if (originY+(img_height*scale))-((img_height*scale)/4) < y < originY+(img_height*scale):")
            print("          if originX < x < originX+(img_with*scale):")
            print("            return 'down'")

'### 2022, SHARKstudio ###'