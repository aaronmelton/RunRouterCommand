# RunRouterCommand.py #
---

## RunRouterCommand.py v1.2.1 (2014-06-09) ##
* Added error correction for commandFile: Application did not previously check
  to determine if this file existed.  Will create an example file containing
  command "show version" if file does not exist.

## RunRouterCommand.py v1.2.0 (2014-03-17) ##
* Replaced tab with four spaces.
* Application failed to fully execute because routerFile and commandFile were
  not defined.  Originally intended to update this code such that it would read
  these values from a config file but never finished that task.  Now complete.
* Added error-checking around output file handling.
* Replaced ' with " to be consistent throughout the file.
* Updated `README.md` to match newest application design.
* Corrected problem where application would fail if logFileDirectory or 
  resultsFileDirectory in settings.cfg was blank.
* Added error-checking for resultsFileDirectory variable.


## RunRouterCommand.py v1.1.12 (2013-08-29) ##
* Suppressed error SPAM from stdout by adding stderr=(open(os.devnull, 'w'))
  to the Queue() function. (Errors are still written to the log.)

## RunRouterCommand.py v1.1.11 (2013-08-15) ##
* Cleaned up module importing

## RunRouterCommand.py v1.1.10 (2013-08-15) ##
* Alphabetized functions

## RunRouterCommand.py v1.1.10 (2013-07-20) ##
* Updating project to use Semantic Versioning: http://semver.org/
  Previous project versions were described using a MAJOR.PATCH increment
  instead of MAJOR.MINOR.PATCH increment.  In other words, adjusting the
  previous version 1.10 -- it's correct Semantic Version would be 1.1.10.

## RunRouterCommand.py 1.10 (2013-07-20) ##
* Making application a bit more extendible through the use of functions and
  variables.
* Improved file error handling.

## RunRouterCommand.py 1.09 (2013-07-18) ##
* Changed application to search for 'routers.txt' file instead of 'routers.lst'
  because some users were complaining about '.lst' not being a registered file
  extension in Windows. (Their user permissions did not allow them to associate
  this extension with Notepad, etc.)
  
## RunRouterCommand.py 1.08 (2013-07-10) ##
* Updated error checking to include validating `commands.lst` file exists.

## RunRouterCommand.py 1.07 (2013-06-26) ##
* Initial "release" of application built on Exscript. This application
  is as old as my `DownloadRouterConfig.py` application, but I'm just now 
  getting around to putting it on GitHub.


----------

(specific details of what changed prior to v1.07 not captured)
