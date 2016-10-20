import os

def getEnergycsv():
    '''The function downloads the 'Energy and Water Data Disclosure for Local Law 84 (2013)' csv
    based on Dr. Bianco's Citibike file download data.
    Author: shalmali 
    '''
    print ("Downloading")
    ### First I will check that it is not already there
    if not os.path.isfile(os.getenv("PUIDATA") + "/" + "m46j-75iy.csv"):
        if os.path.isfile("m46j-75iy.csv"):
            # if in the current dir just move it
            if os.system("mv " + "m46j-75iy.csv " + os.getenv("PUIDATA")):
                print ("Error moving file!, Please check!")
        #otherwise start looking for the zip file
        else:
            if not os.path.isfile(os.getenv("PUIDATA") + "/" + "m46j-75iy.csv"):
                if not os.path.isfile("m46j-75iy.csv"):
                    os.system("wget https://data.cityofnewyork.us/resource/m46j-75iy.csv")
                ###  To move it I use the os.system() functions to run bash commands with arguments
                os.system("mv " + "m46j-75iy.csv " + os.getenv("PUIDATA"))
            ### unzip the csv 
            #os.system("unzip " + os.getenv("PUIDATA") + "/" + datestring + "-citibike-tripdata.zip")
            #print("unzip " + os.getenv("PUIDATA") + "/" + datestring + "-citibike-tripdata.zip")
    ### One final check:
    if not os.path.isfile(os.getenv("PUIDATA") + "/" + "m46j-75iy.csv"):
        print ("WARNING!!! something is wrong: the file is not there!")

    else:
        print ("file in place, you can continue")