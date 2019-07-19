# imperator-linux-fix

## description

-A fix for linux versions of Imperator: Rome (1.0.1+) which fail to load the launcher from steam (only tested on Ubuntu 19.04)

-The input directory should be the launcher directory inside the Imperator directory

-Launching with no parameter uses the config.txt file

-To work with steam add the python file as a non-steam game in Library; rename as desired e.g. 'Imperator: Rome FIX'. this will use the config file location.

## usage
```
launch.py       <- uses config file

launch.py -i <inputdirectory> or launch.py --directory <inputdirectory>
  
launch.py -h
```
