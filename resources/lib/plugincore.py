# * Copyright (C) 2013 sentenza @ github.com
# *
# * This Program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 3, or (at your option)
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

import urllib2
from BeautifulSoup import BeautifulSoup

class PluginCore:
    
    ''' The core class of the video plugin '''
    
    # TODO (sentenza) configuration file
    _USERAGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0"

    def __init__(self):
        # Set the opener for scaping webpages
        opener = urllib2.build_opener()
        opener.addheaders = [('User-Agent', self._USERAGENT)]
        urllib2.install_opener(opener)
        # CHANGE the site to read
        self.root_page_url = "http://example.com"

    ### TODO (sentenza)
    def get_categories(self, page_url=self.root_page_url):
        ''' Returns a list of categories of the scraped site '''
        data = urllib2.urlopen(page_url)
        tree = BeautifulSoup(data, convertEntities=BeautifulSoup.HTML_ENTITIES)

        # CHANGE the parse tree structure
        links = tree.find("div", "CLASS").findAll('a')

        categories = []
        avoid_categories = ["Avoid1", "Avoid2"]
        
        for link in links:
            category = {}
            category["title"] = link.contents[0].strip()
            if category["title"] in avoid_categories:
                continue
            category["url"] = link["href"]
            categories.append(category)
        # categories[{title: "", url: ""}, ... ]
        return categories
