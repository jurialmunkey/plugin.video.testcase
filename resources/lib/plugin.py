# -*- coding: utf-8 -*-
# Module: default
# Author: jurialmunkey
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html
import sys
import xbmcgui
import xbmcplugin


TEST_ITEM = {
    'label': 'Item_{x}_Label',
    'label2': 'Item_{x}_Label2',
    'path': 'plugin://plugin.video.testcase/?item={x}'
}


class Plugin(object):
    def __init__(self):
        self.handle = int(sys.argv[1])
        self.paramstring = sys.argv[2][1:]
        self.update_listing = False
        self.container_content = 'videos'
        self.sort_methods = [{'sortMethod': xbmcplugin.SORT_METHOD_UNSORTED}]
        self.plugin_category = 'Test Case'

    def make_listing(self):
        items = []
        for x in range(20):
            it = {k: v.format(x=x) if isinstance(v, str) else v for k, v in TEST_ITEM.items()}
            label = it['label']
            label2 = it['label2']
            path = it['path']
            li = xbmcgui.ListItem(label=label, label2=label2, path=path, offscreen=True)
            li.getVideoInfoTag()
            items.append((path, li, False, ))

        xbmcplugin.addDirectoryItems(handle=self.handle, items=items)
        xbmcplugin.setPluginCategory(self.handle, self.plugin_category)  # Container.PluginCategory
        xbmcplugin.setContent(self.handle, self.container_content)  # Container.Content
        # for i in self.sort_methods:
        #     xbmcplugin.addSortMethod(self.handle, **i)
        xbmcplugin.endOfDirectory(self.handle, updateListing=self.update_listing)

    def run(self):
        return self.make_listing()
