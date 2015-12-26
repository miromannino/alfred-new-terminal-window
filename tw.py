import xml.etree.ElementTree as ET
import biplist
import os
import sys

# Config
iTerm_CONFIG_PATH = os.path.join(os.environ["HOME"], "Library", "Preferences", "com.googlecode.iterm2.plist")

def readITermConfig(query):
  rE = ET.Element('items')
  if os.path.isfile(iTerm_CONFIG_PATH):
    try:
      config = biplist.readPlist(iTerm_CONFIG_PATH)
      defaultBookmarkGUID = config.get('Default Bookmark Guid')
      for item in config['New Bookmarks']:
        profileName = item.get('Name')
        if (item.get('Guid') == defaultBookmarkGUID): continue
        if len(query) > 0 and profileName.lower().find(query.lower()) == -1: continue
        iE = ET.SubElement(rE, 'item', valid = 'yes', arg = profileName, autocomplete = profileName)
        tE = ET.SubElement(iE, 'title')
        tE.text = 'New iTerm window'
        stE = ET.SubElement(iE, 'subtitle')
        stE.text = profileName
    except:
      return None
    return rE
  else:
    return None

res = readITermConfig(sys.argv[1] if len(sys.argv) > 1 else '')
if res is not None: 
  print '<?xml version="1.0"?>'
  print ET.tostring(res)
