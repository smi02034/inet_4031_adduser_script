#!/usr/bin/python3
import os
import re
import sys

def main():
	for line in sys.stdin:
		match = re.match("^#", line)
		fields = line.strip().split(':') # Strips any whitespace and splits the attributes of the user into an array

		if match or len(fields) != 5: # Checks if the line starts with # or if it doesn't have five fields
			continue # If so, then we go to the next iteration in the for loop to skip the line

		username = fields[0]
		password = fields[1]

		gecos = "%s %s,,," % (fields[3],fields[2])

		groups = fields[4].split(',') # Creates an array of groups that the user will be a part of

		print("==> Creating user account for %s..." % (username))
		cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
		print(cmd)
		os.system(cmd) # Sends the command as a terminal input

		print("==> Setting the password for %s..." % (username))
		cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
		print(cmd)
		os.system(cmd) # Sends the command as a terminal input

		for group in groups: # Goes through each group the user needs to be assigned to and assigns it to that group
			if group != '-': # Checks that the group is not '-' because '-' is put when there are no groups
				print("==> Assigning %s to the %s group..." % (username, group))
				cmd = "/usr/sbin/adduser %s %s" % (username, group)
				print(cmd)
				os.system(cmd) # Sends the command as a terminal input


if __name__ == "__main__":
	main()
