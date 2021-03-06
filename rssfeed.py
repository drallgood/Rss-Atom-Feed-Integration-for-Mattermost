#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'elpatron@mailbox.org'

import sys
import urllib
try:
    import html2text
except ImportError as exc:
    print('Error: failed to import module. ({}). \nInstall missing modules using '
                '"sudo pip install -r requirements.txt"'.format(exc))
    sys.exit(0)


class RssFeed:
    def __init__(self, name, url, iconurl, user, channel, showname, showtitle, showdescription, showurl):
        self.Name = name
        self.Url = url
        self.Iconurl = iconurl
        self.User = user
        self.Channel = channel
        self.ShowName = showname
        self.ShowTitle = showtitle
        self.ShowDescription = showdescription
        self.ShowUrl = showurl
        self.LastTitle = ''
        self.NewTitle = ''
        self.ArticleUrl = ''
        self.Description = ''

    def jointext(self):
        text = ''
        h = html2text.HTML2Text()
        h.ignore_links = True
        self.Description = h.handle(self.Description)
        if self.ShowName == True:
            text += "_" + self.Name + '_\n'
        if self.ShowTitle == True:
            text += '### [' + self.NewTitle + '](' + urllib.quote(self.ArticleUrl, safe=';/?:@&=+$,') + ')\n'
        if self.ShowDescription == True:
            text += self.Description + '\n'
        if self.ShowUrl == True:
            text += self.ArticleUrl
        return text

    def env_definition(self):
        text = '\nRSS_FEED_' + self.Name
        text += '=\'' + self.Url
        text += ';' + self.Iconurl
        text += ';' + self.Channel
        text += ';' + str(self.ShowName)
        text += ';' + str(self.ShowTitle)
        text += ';' + str(self.ShowDescription)
        text += ';' + str(self.ShowUrl)
        text += '\''
        return text

