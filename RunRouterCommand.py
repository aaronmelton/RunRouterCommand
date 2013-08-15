#!/usr/bin/env python
#
# RunRouterCommand.py
# Copyright (C) 2012-2013 Aaron Melton <aaron(at)aaronmelton(dot)com>
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


import datetime	# Required for date format
import Exscript	# Required for SSH, queue & logging functionality
import os		# Required to determine OS of host

from Exscript                   import Queue, Host, Logger
from Exscript.protocols 		import SSH2
from Exscript.util.file			import get_hosts_from_file
from Exscript.util.log          import log_to
from Exscript.util.decorator    import autologin
from Exscript.util.interact     import read_login
from Exscript.util.report		import status,summarize


def fileExist(fileName):
# Check current path for existing file
	try:
		with open(fileName, 'r') as openedFile:
			# If file exists (can be opened), return true
			return 1
	except IOError:
		# If file does not exists (can't be opened), return false
		return 0

logger = Logger()	# Log stuff
@log_to(logger)	# Logging decorator; Must precede runRouterCommand!
@autologin()	# Exscript login decorator; Must precede runRouterCommand!
def runRouterCommand(job, host, socket):
	socket.execute("terminal length 0")	# Disable user-prompt to page through terminal output
										# Exscript doesn't always recognize Cisco IOS
										# for socket.autoinit() to work correctly

	outputDirectory = ('results_'+date+'/')	# Define directory to hold terminal output files
	if not os.path.exists(outputDirectory): os.mkdir(outputDirectory) # Create config file directory if it doesn't exist
		
	outputFileName = host.get_name()+'_results_'+date+'.txt'	# Define output filename based on hostname and date
	outputFile = file(outputDirectory+outputFileName, 'w')		# Open output file (will overwrite contents)

	commandList = open(commandFile, 'r')		# Open file containing router commands
	line = commandList.readlines()				# Read input file line-by-line
	
	for x in range(0, len(line)):			# Loop through contents of input file
		socket.execute(line[x])				# Execute command on router
		outputFile.write(socket.response)	# Write router results to output file
	
	commandList.close()						# Close input file
	outputFile.close()					# Close output file
	socket.send('exit\r')				# Send the "exit" command to log out of router gracefully
	socket.close()						# Close SSH connection

	
# Determine OS in use and clear screen of previous output
os.system('cls' if os.name=='nt' else 'clear')

print "Run Router Command v1.1.10"
print "--------------------------"
print

# Define file with router IP Addresses or Hostnames
routerFile = 'routers.txt'
commandFile = 'commands.txt'

# Check for existence of routerFile; If exists, continue with program
if fileExist(routerFile):
	# Check for existence of commandFile; If exists, continue with program
	if fileExist(commandFile):

		# Define 'date' variable for use in the output filename
		date = datetime.datetime.now()		# Determine today's date
		date = date.strftime('%Y%m%d')	# Format date as YYYYMMDD
		
		# Read hosts from specified file & remove duplicate entries, set protocol to SSH2
		hosts = get_hosts_from_file(routerFile,default_protocol='ssh2',remove_duplicates=True)
		userCreds = read_login()	# Prompt the user for his name and password
		
		print # Required for pretty spacing. :)
		
		queue = Queue(verbose=1, max_threads=4)	# Minimal message from queue, 4 threads
		queue.add_account(userCreds)			# Use supplied user credentials
		queue.run(hosts, runRouterCommand)		# Create queue using provided hosts
		queue.shutdown()						# End all running threads and close queue
		
		print status(logger)	# Print current % status of operation to screen
		
		logFile = open('status_'+date+'.log', 'w')	# Open 'status.log' file
		logFile.write(summarize(logger))	# Write results of program to file
		logFile.close()						# Close 'status.log' file

	# If commandFile does not exist, create example and exit
	else:
		# Attempt to open CommandFile to create an example
		try:
			with open (commandFile, 'w') as exampleFile:
				# Write example command to commandFile
				exampleFile.write("show run\n")
				# Print error message
				print "Required file "+commandFile+" not found; One has been created for you."
				print "This file must contain a list, one per line, of commands to send to the"
				print "router."
		# If unable to write file for whatever reason, just print error message
		except IOError:
				# Print error message
				print "Required file "+commandFile+" not found."
				print "This file must contain a list, one per line, of commands to send to the"
				print "router."
	
# If routerFile does not exist, create example and exit
else:
	# Attempt to open routerFile to create an example
	try:
		with open (routerFile, 'w') as exampleFile:
			# Write example IP Addresses or Hostnames to routerFile
			exampleFile.write("192.168.1.1\n192.168.1.2\nRouterA\nRouterB\nRouterC\netc...")
			# Print error message
			print "Required file "+routerFile+" not found; One has been created for you."
			print "This file must contain a list, one per line, of Hostnames or IP addresses the"
			print "application will then connect to."
	# If unable to write file for whatever reason, just print error message
	except IOError:
		# Print error message
		print "Required file "+routerFile+" not found."
		print "This file must contain a list, one per line, of Hostnames or IP addresses the"
		print "application will then connect to."
