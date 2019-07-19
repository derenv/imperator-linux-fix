#!/usr/bin/python3
#-------------------------------------------------------------------------------
# Name:        imperator launcher
# Purpose:     launch imperator launcher from desktop icon
#
# Author:      Deren Vural
#
# Created:     01/07/2019
# Copyright:   (c) deren 2019
# Licence:     open source GIVE CREDIT FOR COPIED
#-------------------------------------------------------------------------------

#imports
import sys, getopt, configparser
from os import path, chdir, getcwd
from subprocess import call

def validate_and_run(data):
    if data == '':
        print("!no input directory setting provided")
        sys.exit(2)
    elif path.isdir(data):
        print("..non-empty and existing input directory..")
        directory = path.realpath(data)

        print("..moving to directory '"+directory+"'..")
        #move to directory
        chdir(directory)
        print("..now in '"+getcwd()+"'..")
                        
        #check if launcher file exists
        print("..checking if '"+path.join(path.curdir, "Paradox Launcher")+"' exists..")
        if path.isfile(path.join(path.curdir, "Paradox Launcher")):
            print("..launcher found..")

            #launch
            call(path.join(path.curdir, "Paradox Launcher"))
        else:
            print("!no launcher detected in folder!")
            sys.exit(2)
    else:
        print("!input directory setting does not exist!")
        sys.exit(2)
                
def main(argv):
    #vars
    directory = ""
    
    try:
        #get arguments
        opts, args = getopt.getopt(argv,"hi:",["input="])
        print(opts)

        #check if too many
        if(len(opts) > 1 | len(args) > 0):
            print("!invalid arguements passed!")
            sys.exit(2)
        #check if one exists and if valid
        elif(len(opts) == 1):
            print("..valid options..")
            #check if help request
            for opt, arg in opts:
                if opt == '-h':
                    print("usage : launch.py")
                    print("        launch.py -i <inputdirectory> or launch.py --directory <inputdirectory>")
                    print("        launch.py -h")
                    print("launching with no parameter uses the config.txt file")
                    print("the input directory should be the launcher directory inside the Imperator directory.")
                    sys.exit()
                elif opt in ("-i", "--input"):
                    print("..parsing options..")
                    
                    #check if directory exists
                    validate_and_run(arg)
        else:
            #parse config file
            config = configparser.ConfigParser()
            config.readfp(open(r'config.txt'))
            data = config.get('settings', 'directory')
            
            validate_and_run(data)
    except getopt.GetoptError:
        print("!invalid arguements passed!")
        sys.exit(2)

if __name__ == '__main__':
    main(sys.argv[1:])
