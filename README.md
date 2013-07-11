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
3. A `routers.lst` file in the same directory as the script which contains
   a list, one per line, of hostnames or IP addresses the application will
   then connect to download the running-config.
4. A `commands.lst` file in the same directory as the script which contains
   a list of valid commands, one per line, to execute on the router.

## Assumptions ##
1. This application was written for use on Cisco IOS devices and cannot be
   guaranteed to work on other makes/model routers.
2. This application assumes that you have enable privileges on each router
   in order to execute privileged command.  If you do not have sufficient 
   user privileges, this application will not work as designed.

## Limitations ##
1. This application uses the same username/password to access ALL routers. If
   your routers use unique usernames/passwords, then this script will not work.
2. This application is hard-coded to connect to FOUR routers simultaneously.
   I wrote this application in an environment where Cisco routers authenticate
   against a Cisco ACS and found FOUR simultaneous requests to be the maximum
   number of requests before regular authentication failures began happening.
   If you use static usernames/passwords in your environment, or your ACS is
   more robust, feel free to increase the `max_threads` variable in the
   `Queue` function.

## Functionality ##
1. Upon execution, the application will prompt the user for a username and
   password.  This username/password will be used to login to all routers
   specified in the `routers.lst` file.
2. The application will open an SSH v2 connection to each router in the
   `routers.lst` file and use the credentials provided by the user to
   authenticate.
3. The application will pass a `terminal length 0` command to the router to
   avoid any page breaks which will interrupt router output.  It has been my
   experience in testing that the `autoinit()` function provided by Exscript
   fails to accomplish this, so I perform this task manually.
4. The application will read the contents of the `commands.lst` file line by
   line and pass them to the router as if they were being entered directly at
   terminal.  Be advised that if the router requires extra time to process
   a command or you attempt to pass too large a command list to the router, it
   may overwhelm the copy-paste buffer.
5. The application will write the the results of the commands as if you were
   seeing the output in the terminal.  These results will be written to 
   a file using the format, `HOSTNAME_results_YYYYMMDD.txt`, where HOSTNAME is
   the hostname (or IP address) specified in the `routers.lst` file and
   YYYYMMDD is the numerical Year-Month-Day of the box executing the
   application.
6. The application will write a `status_YYYYMMDD.log` file that identifies the
   connectivity results from each router.
