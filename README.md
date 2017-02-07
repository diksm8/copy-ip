# copy-ip
Python script to copy current IP.

Install the required modules using ``pip install -r requirements.txt``
Compile using ``pyinstaller -F --noconsole copy-ip.py``
Put the ``copy-ip.exe`` somewhere in your path, i.e your scirpts folder
Make an AutoHotkey script containing ``#i:: Run, copy-ip`` and run the script on startup
The AutoHotkey is set to run the script when you press "super" (windows key) and "i" key