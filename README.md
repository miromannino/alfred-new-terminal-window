alfred-new-terminal-window
==========================

Alfred workflow to open a new Terminal/iTerm window in the current space. Holding the alt key, the new window will be opened in the current frontmost Finder folder.

How to use
----------

Install the workflow and type one of the following keyword on Alfred:

### iTerm

 - `tw`: open a new iTerm window
 - `tw` pressing `enter` together with the `alt` key: open the current Finder folder in a new iTerm window

The workflow will also suggest all the available profiles for iTerm.

[TODO screenshot]

One can also open iTerm directly with a profile in this way:

    tw myprofilename

[TODO screenshot con "tw myprofilena" per far vedere che nel frattempo suggerisce]

### Terminal 

 - `ttw`: open a new Terminal window
 - `ttw` pressing `enter` together with the `alt` key: open the current Finder folder in a new Terminal window


General notes
-------------

- All the new window is placed in the current desktop
- If a terminal window is open, it doesn't focus that window, but a new one will be created. If you want
  to focus an existing Terminal, you can just write "iTerm" or "Terminal" using Alfred.
- Once the workflow has been imported, feel free to change the default keywords if you don't like them.
- For speed improvement, the default iTerm profile will appear instantaneously, while the other will appear 
  after some milliseconds (because that requires reading the available iTerm profiles from a file). 
  Other workflow for iTerm doesn't have that feature, and may appear slow.