# -*- coding: utf-8 -*-
# Module: default
# Author: jurialmunkey
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html
import sys
import time
import xbmc
import xbmcgui
import xbmcplugin
from urllib.parse import unquote_plus


TEST_ITEM = {
    'label': 'Item_{x}_Label',
    'label2': 'Item_{x}_Label2',
    'path': 'plugin://plugin.video.testcase/?info=winprops&x={x}',
    'isFolder': False
}


def parse_paramstring(paramstring):
    """ helper to assist to standardise urllib parsing """
    params = dict()
    paramstring = paramstring.replace('&amp;', '&')  # Just in case xml string
    for param in paramstring.split('&'):
        if '=' not in param:
            continue
        k, v = param.split('=')
        params[unquote_plus(k)] = unquote_plus(v)
    return params


class Plugin(object):
    def __init__(self):
        self.handle = int(sys.argv[1])
        self.paramstring = sys.argv[2][1:]
        self.params = parse_paramstring(self.paramstring)
        self.update_listing = False
        self.container_content = 'tvshows'
        self.sort_methods = [{'sortMethod': xbmcplugin.SORT_METHOD_UNSORTED}]
        self.plugin_category = 'Test Case'

    def set_winprops(self):
        window = xbmcgui.Window(10000)
        xbmc.executebuiltin('Container.Refresh')
        window.setProperty('reload', f'{int(time.time())}')

    def make_listing(self):
        for x in range(20):
            it = {k: v.format(x=x) if isinstance(v, str) else v for k, v in TEST_ITEM.items()}
            li = xbmcgui.ListItem(label=it['label'], label2=it['label2'], path=it['path'])
            xbmcplugin.addDirectoryItem(
                handle=self.handle,
                url=it['path'],
                listitem=li,
                isFolder=it['isFolder'])

        xbmcplugin.setPluginCategory(self.handle, self.plugin_category)  # Container.PluginCategory
        xbmcplugin.setContent(self.handle, self.container_content)  # Container.Content
        for i in self.sort_methods:
            xbmcplugin.addSortMethod(self.handle, **i)
        xbmcplugin.endOfDirectory(self.handle, updateListing=self.update_listing)

    def run(self):
        info = self.params.get('info')
        if info == 'winprops':
            return self.set_winprops()
        return self.make_listing()
