## ReadMe File for create-users.py Script
### Description
create-users.py is a Python 3 script that uses information from an input file to automatically create users in Linux.

### Operation
#### 1. Formatting the Input File
The first step of using the create-users.py script is to create an input file of all the users that need to be created and their attributes. Once that file is created, it needs to be formatted so that the program can correctly interpret it. The format of a line, each of which describes one user, is below:
```
name:password:lastName:firstName:group
```
If the user needs to belong to more than one group, then each group will be separated with a comma, like so:
```
name:password:lastName:firstName:group1,group2
```
If the user doesn't need to belong to any groups, then the '-' character should be put in place of a group name:
```
name:password:lastName:firstName:-
```
Lastly, if  a line needs to be ignored by the script, then a '#' should be put in front of it:
```
#name:password:lastName:firstName:group
```
These formatting rules must be followed exactly or the script will produce errors and/or create the users incorrectly.

#### 2. Preparing to Run the Script
The script is designed to be run by using the Linux command line. Before the script can be run, it needs to be given the correct permissions by having this command run:
```
chmod a+x [PATH TO create-users.py]
```

#### 3. Running the Script
To run the script in the Linux command line, a command should be entered that follows this format:
```
sudo ./[PATH TO create-users.py] < [PATH TO INPUT FILE]
```
Alternatively, the command could follow this format:
```
cat [PATH TO INPUT FILE] | sudo ./[PATH TO create-users.py]
```