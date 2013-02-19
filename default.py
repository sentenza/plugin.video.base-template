# * Copyright (C) 2013 sentenza @ github.com
# *
# * This Program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2, or (at your option)
# * any later version.
# *
# * This Program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; see the file LICENSE. If not, write to
# * the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# * http://www.gnu.org/copyleft/gpl.html

""" Video plugin base template for XBMC """
    
import sys
import urllib
import urlparse
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
from resources.lib.plugincore import PluginCore

### Plugin constants ###
__plugin__ = "plugin.video.base-template"
__author__ = "sentenza"

Addon = xbmcaddon.Addon(id=__plugin__)

# plugin handle
handle = int(sys.argv[1])

core = PluginCore()


### User Interface construction ###
def show_folder(url=None):
    ''' List the categories from the root to the leafs '''

    list_mode = "folder" if url is None else "list"

    categories = core.get_categories()
    ### EXAMPLE listing of 5 items
    for category in categories:
        title = category["title"]
        item_url = category["url"]
        list_item_style = xbmcgui.ListItem(title)
        add_item({"mode": list_mode, "url": item_url}, list_item_style)
    xbmcplugin.endOfDirectory(handle=handle, succeeded=True)


def show_video_files(url):
    # TODO
    xbmcplugin.endOfDirectory(handle=handle, succeeded=True)


def play_video(url):
    # TODO
    # Routine for parsing url
    video_url = url
    xbmc.Player().play(video_url)


### xbmcplugin based UI methods ###
def add_item(parameters, li, folder=True):
    ''' 
    Adds an item to a listing directory. If folder==False a single item instead of a folder.
    '''
    url = sys.argv[0] + '?' + urllib.urlencode(parameters)
    return xbmcplugin.addDirectoryItem(handle=handle, url=url, listitem=li, isFolder=folder)

### Common utilities ####
def parameters_string_to_dict(parameters):
    ''' Convert parameters encoded in a URL to a dict. '''
    return dict(urlparse.parse_qsl(parameters[1:]))


# parameter values
params = parameters_string_to_dict(sys.argv[2])
mode = str(params.get("mode", ""))
url = str(params.get("url", ""))

if mode == "":
    show_folder()
elif mode == "folder":
    show_folder(url)
# elif mode == "list":
#    show_video_files(url)
# elif mode == "video":
#    play_video(url)
