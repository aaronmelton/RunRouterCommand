# RunRouterCommand.py #
----------

Assuming Python is in your path environment variable, you can execute the
script directly from the command-line:


    python RunRouterCommand.py

Personally, I use the Pyinstaller module, [http://www.pyinstaller.org/](http://www.pyinstaller.org/)
to compile everything into a single binary to execute from the Windows
command-line:

    python C:\path\to\pyinstaller.py RunRouterCommand.py --onefile
