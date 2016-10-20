import os

def getshapecsv():
    '''The function downloads the 'Emappluto_16v1.zip'
    Author: Shalmali
    '''
    print ("Downloading")
    ### First I will heck that it is not already there
    if not os.path.isfile(os.getenv("PUIDATA") + "/" + "Manhattan/"):
        if os.path.isfile("Manhattan/"):
            # if in the current dir just move it
            if os.system("mv " + "Manhattan " + os.getenv("PUIDATA")):
                print ("Error moving file!, Please check!")
        #otherwise start looking for the zip file
        else:
            if not os.path.isfile(os.getenv("PUIDATA") + "/" + "mappluto_16v1.zip"):
                if not os.path.isfile("mappluto_16v1.zip"):
                    os.system("wget https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/mappluto_16v1.zip")
                ###  To move it I use the os.system() functions to run bash commands with arguments
                os.system("mv " + "mappluto_16v1.zip " + os.getenv("PUIDATA"))
            ### unzip the csv
            if os.system("unzip " + os.getenv("PUIDATA") + "/" + "mappluto_16v1.zip"):
                print("Unzipped")
                os.system("mv " + "Manhattan " + os.getenv("PUIDATA"))
                os.system("rm -r Bronx/")
                os.system("rm -r Brooklyn/")
                os.system("rm -r Queens/")
                os.system("rm -r Staten_Island/")
    ### One final check:
    if not os.path.isfile(os.getenv("PUIDATA") + "/" + "Manhattan/MNMapPLUTO.shp"):
        print ("WARNING!!! something is wrong: the file is not there!")

    else:
        print ("file in place, you can continue")