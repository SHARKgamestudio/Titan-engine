'#############################################'
'################### TITAN ###################'
'#############################################'
'### open-source numworks sprite generator ###'
'#############################################'

# importing modules
from PyQt5 import QtCore, QtGui, QtWidgets # importing 'pyQt5' for GUI
from PIL import Image # importing 'PIL' module for computing images
from PyQt5.QtCore import pyqtSlot # importing pyQt5_slot for signals

# creating the object
class Ui_window(object):

    # initiate the UI
    def setupUi(self, window):

# window
        window.setObjectName("window")
        window.resize(600, 600)
        window.setMinimumSize(QtCore.QSize(600, 600))
        window.setMaximumSize(QtCore.QSize(600, 600))
        window.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.mainWin = QtWidgets.QWidget(window)
        self.mainWin.setObjectName("mainWin")

# logo
        self.Logo = QtWidgets.QWidget(self.mainWin)
        self.Logo.setGeometry(QtCore.QRect(40, 10, 524, 111))
        self.Logo.setStyleSheet("background-image: url(:/Logo/LogoWhite.png);")
        self.Logo.setObjectName("Logo")
        self.FileValue = QtWidgets.QLineEdit(self.mainWin)
        self.FileValue.setGeometry(QtCore.QRect(90, 240, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)

# text_field
        self.FileValue.setFont(font)
        self.FileValue.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.FileValue.setStyleSheet("border-style: none;\n""border-radius:15px;\n""\n""background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(106, 249, 255, 255), stop:1 rgba(217, 131, 255, 255));")
        self.FileValue.setText("")
        self.FileValue.setAlignment(QtCore.Qt.AlignCenter)
        self.FileValue.setPlaceholderText("")
        self.FileValue.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.FileValue.setObjectName("FileValue")
        self.FileTitle = QtWidgets.QLabel(self.mainWin)
        self.FileTitle.setGeometry(QtCore.QRect(30, 180, 541, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)

# text_field Title
        self.FileTitle.setFont(font)
        self.FileTitle.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.FileTitle.setFocusPolicy(QtCore.Qt.NoFocus)
        self.FileTitle.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(53, 53, 53);")
        self.FileTitle.setTextFormat(QtCore.Qt.RichText)
        self.FileTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.FileTitle.setWordWrap(False)
        self.FileTitle.setObjectName("FileTitle")
        self.FileDescription = QtWidgets.QLabel(self.mainWin)
        self.FileDescription.setGeometry(QtCore.QRect(30, 212, 541, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)

#text_field Description
        self.FileDescription.setFont(font)
        self.FileDescription.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.FileDescription.setFocusPolicy(QtCore.Qt.NoFocus)
        self.FileDescription.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(53, 53, 53);")
        self.FileDescription.setTextFormat(QtCore.Qt.RichText)
        self.FileDescription.setAlignment(QtCore.Qt.AlignCenter)
        self.FileDescription.setWordWrap(False)
        self.FileDescription.setObjectName("FileDescription")

# frames
        self.Frame = QtWidgets.QWidget(self.mainWin)
        self.Frame.setGeometry(QtCore.QRect(20, 160, 561, 141))
        self.Frame.setStyleSheet("background-color: rgb(53, 53, 53);\n""border-radius: 25px;")
        self.Frame.setObjectName("Frame")
        self.Frame2 = QtWidgets.QWidget(self.mainWin)
        self.Frame2.setGeometry(QtCore.QRect(20, 320, 561, 261))
        self.Frame2.setStyleSheet("background-color: rgb(53, 53, 53);\n""border-radius: 25px;")
        self.Frame2.setObjectName("Frame2")
        self.OptionsTitle = QtWidgets.QLabel(self.Frame2)
        self.OptionsTitle.setGeometry(QtCore.QRect(10, 20, 541, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)

# options Title
        self.OptionsTitle.setFont(font)
        self.OptionsTitle.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.OptionsTitle.setFocusPolicy(QtCore.Qt.NoFocus)
        self.OptionsTitle.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(53, 53, 53);")
        self.OptionsTitle.setTextFormat(QtCore.Qt.RichText)
        self.OptionsTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.OptionsTitle.setWordWrap(False)
        self.OptionsTitle.setObjectName("OptionsTitle")
        self.OptionsDescription = QtWidgets.QLabel(self.Frame2)
        self.OptionsDescription.setGeometry(QtCore.QRect(10, 50, 541, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)

# options Description
        self.OptionsDescription.setFont(font)
        self.OptionsDescription.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.OptionsDescription.setFocusPolicy(QtCore.Qt.NoFocus)
        self.OptionsDescription.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(53, 53, 53);")
        self.OptionsDescription.setTextFormat(QtCore.Qt.RichText)
        self.OptionsDescription.setAlignment(QtCore.Qt.AlignCenter)
        self.OptionsDescription.setWordWrap(False)
        self.OptionsDescription.setObjectName("OptionsDescription")
        self.comments = QtWidgets.QRadioButton(self.Frame2)
        self.comments.setGeometry(QtCore.QRect(180, 90, 191, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)

        # ___--- RADIO BUTTONS ---___ #

# generate_comments Button
        self.comments.setFont(font)
        self.comments.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.comments.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comments.setAutoFillBackground(False)
        self.comments.setStyleSheet("color: rgb(255, 255, 255);")
        self.comments.setIconSize(QtCore.QSize(64, 64))
        self.comments.setAutoExclusive(False)
        self.comments.setObjectName("comments")
        self.security = QtWidgets.QRadioButton(self.Frame2)
        self.security.setGeometry(QtCore.QRect(190, 120, 171, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)

# generate_security Button
        self.security.setFont(font)
        self.security.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.security.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.security.setAutoFillBackground(False)
        self.security.setStyleSheet("color: rgb(255, 255, 255);")
        self.security.setIconSize(QtCore.QSize(64, 64))
        self.security.setAutoExclusive(False)
        self.security.setObjectName("security")

# generate_convex_collision Button
        self.convex = QtWidgets.QRadioButton(self.Frame2)
        self.convex.setGeometry(QtCore.QRect(190, 150, 171, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.convex.setFont(font)
        self.convex.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.convex.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.convex.setAutoFillBackground(False)
        self.convex.setStyleSheet("color: rgb(255, 255, 255);")
        self.convex.setIconSize(QtCore.QSize(64, 64))
        self.convex.setAutoExclusive(False)
        self.convex.setObjectName("convex")

# generate_trigger_collision Button
        self.collision = QtWidgets.QRadioButton(self.Frame2)
        self.collision.setGeometry(QtCore.QRect(190, 180, 171, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.collision.setFont(font)
        self.collision.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.collision.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.collision.setAutoFillBackground(False)
        self.collision.setStyleSheet("color: rgb(255, 255, 255);")
        self.collision.setIconSize(QtCore.QSize(64, 64))
        self.collision.setAutoExclusive(False)
        self.collision.setObjectName("collision")


        # ___--- GENERATE BUTTON ---___ #
        self.GenerateButton = QtWidgets.QPushButton(self.Frame2)
        self.GenerateButton.setGeometry(QtCore.QRect(100, 220, 341, 31))
        self.GenerateButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(106, 249, 255, 255), stop:1 rgba(217, 131, 255, 255));\n""border-radius: 15px")
        self.GenerateButton.setObjectName("GenerateButton")
        self.GenerateButton.clicked.connect(self.generateSprite)
        self.Frame.raise_()
        self.Logo.raise_()
        self.FileValue.raise_()
        self.FileTitle.raise_()
        self.FileDescription.raise_()
        self.Frame2.raise_()
        window.setCentralWidget(self.mainWin)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def generateSprite(self):

# variables
        fileName = self.FileValue.text() # file path
        generateComments = self.comments.isChecked() # comments
        generateSizeSecurity = self.security.isChecked() # security
        generateCollision = self.convex.isChecked() # convex
        generateTrigger = self.collision.isChecked() # trigger
        PAL = list() # declare list for store pixels RGB
        width = 0
        height = 0

# testing print
        print("fileName : " + fileName)
        print("generateComments : " + str(generateComments))
        print("generateSizeSecurity : " + str(generateSizeSecurity))
        print("generateCollision : " + str(generateCollision))
        print("generateTrigger : " + str(generateTrigger))

        if(fileName == "!help"): # verify if the command !help as been taped
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
            picture = Image.open('Resources/' + fileName)
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

# show code in the console with the user customs args
            if "dont pay attention, just here for testing" == "dont pay attention, just here for testing":
                if generateComments == True:
                    print("# importing graphical module")
                print("from kandinsky import *")
                print("")
                if generateComments == True:
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
                if generateSizeSecurity == True:
                    print("  if scale < 1:")
                    print("    scale = 1")
                if generateComments == True:
                    print("#pixels-matrices")
                print("  while i < " + str(height*width) + ":")
                if generateComments == True:
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
                if generateComments == True:
                    print("#draw 'Y' pixels")
                print("      internalX = 0")
                print("      internalY += (1*scale)")
                print("")
                # trigger collision
                if(generateTrigger == True):
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
                if(generateCollision == True):
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


# translate (if needed) the differents GUI elements
    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "TITAN / mainpanel"))
        self.FileTitle.setText(_translate("window", "Input your file name :"))
        self.FileDescription.setText(_translate("window", "WARNING : your file should be in the \"/Reources\" folder."))
        self.OptionsTitle.setText(_translate("window", "Select your options :"))
        self.OptionsDescription.setText(_translate("window", "WARNING : please notice that each features take extra space on your calculator"))
        self.comments.setText(_translate("window", "generate simples comments"))
        self.security.setText(_translate("window", "generate security-system"))
        self.convex.setText(_translate("window", "generate convex-collision"))
        self.collision.setText(_translate("window", "generate trigger-collision"))
        self.GenerateButton.setText(_translate("window", "Generate Sprite"))
import resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())