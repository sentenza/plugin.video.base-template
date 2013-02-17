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

# plugin handle
handle = int(sys.argv[1])


### User Interface construction ###
def show_folder(url=None):
    ''' List the categories in the root folder of the plugin '''

    list_mode = "folder" if url else "list"

    ### EXAMPLE listing of 5 items
    for i in range(1,6):
        title = "Category item " + str(i)
        item_url = "http://example.com/" + str(i)
        list_item_style = xbmcgui.ListItem(title)
        add_item({"mode": list_mode, "url": item_url}, list_item_style)
    xbmcplugin.endOfDirectory(handle=handle, succeeded=True)

def show_video_files(url):
    # TODO
    pass

def play_video(url):
    # TODO
    pass


### xbmcplugin based UI methods ###
def add_item(parameters, li, folder=True):
    ''' Adds an item to a listing directory. '''
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
