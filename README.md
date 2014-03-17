# RunRouterCommand.py #
----------

## About ##
**RunRouterCommand.py** is a Python application that executes specified commands on a Cisco router.

## Dependencies ##
Exscript module [https://github.com/knipknap/exscript/](https://github.com/knipknap/exscript/)

## Requirements ##
1. This application is hard-coded to use the SSH2 protocol; If SSH v2 is not
   enabled on your router(s), you will need to:
   * Add `ip ssh version 2` to your Cisco router(s) configuration and any
       associated access-list changes.
   or
   * Alter the `default_protocol` variable in the `get_hosts_from_file`
       function to use a different protocol enabled on your router(s).
2. A valid username/password.

## Assumptions ##
1. This application was written for use on Cisco IOS devices and cannot be
   guaranteed to work on other makes/model routers.
2. This application assumes that you have enable privileges on each router
   in order to execute privileged command.  If you do not have sufficient 
   user privileges, this application will not work as designed.

## Limitations ##
1. This application uses the same username/password to access ALL routers. If
   your routers use unique usernames/passwords, then this script will not work.
   If a password is stored in the `settings.cfg` file, it must be Base64 encoded.
2. A correctly-formatted config file (default filename is `settings.cfg`).
3. A correctly-formatted router file (default filename is `routers.txt`).
4. A correctly-formatted command file (default filename is `commands.txt`).

## Functionality ##
1. Upon execution, the application will search it's local directory for a
   config file, `settings.txt`, if one was not provided through the command
   line during execution `python DownloadRouterConfig.py --config CONFIGFILE`.
   If a config file was not found or specified, a sample one will be created and
   the application will exit (END).  Edit this file to your specifications
   before launching the application again.
2. Upon execution, the application will search for the routerFile variable
   specified in the config file (default filename is `routers.txt`).  If that
   file cannot be found, a sample one will be created and the application will
   exit (END).  Edit this file to your specifications before launching the
   application again.
3. Upon execution, the application will search for the commandFile variable
   specified in the config file (default filename is `commands.txt`).  If that
   file cannot be found, a sample one will be created and the application will
   exit (END).  Edit this file to your specifications before launching the
   application again.
4. The application will open an SSH v2 connection to each router in the
   `routers.txt` file.  If the user specified their login credentials in the
   config file, they will be used.  Otherwise, the application will prompt the
   user to provide their login credentials upon execution.
5. The application will pass a `terminal length 0` command to the router to
   avoid any page breaks which will interrupt router output.  (It has been my
   experience in testing that the `autoinit()` function provided by Exscript
   fails to detect Cisco IOS on some routers in our environment.)
6. The application will read the contents of the `commands.txt` file line by
   line and pass them to the router as if they were being entered directly at
   terminal.  Be advised that if the router requires extra time to process
   a command or you attempt to pass too large a command list to the router, it
   may overwhelm the copy-paste buffer and the router may not successfully
   execute some commands.
7. The application will write the the results of the commands as if you were
   seeing the output in the terminal.  These results will be written to 
   a file using the format, `HOSTNAME_Results_YYYYMMDD.txt`, where HOSTNAME is
   the hostname (or IP address) specified in the `routers.txt` file and
   YYYYMMDD is the numerical Year-Month-Day of the box executing the
   application. These files will be stored in the directory specified by the
   `backupDirectory` variable in the `settings.cfg` file, or the parent directory
   of the application if no value was specified.  If this file already exists, 
   the filename will be appended with an integer that will continue to increment 
   until the application finds a filename that does not currently exist in that 
   directory.
8. The application will write a `RunRouterCommand_YYYYMMDD.log` file that 
   identifies the connectivity results from each router.  This file will be 
   stored in the directory specified by the `logFileDirectory` variable in the 
   `settings.cfg` file, or the parent directory of the application if no value 
   was specified.  If this file already exists, the filename will be appended 
   with an integer that will continue to increment until the application finds 
   a filename that does not currently exist in that directory.
