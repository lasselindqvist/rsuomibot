# http://inamidst.com/saxo/
# Created by Sean B. Palmer

import re
import saxo
import urllib2
from BeautifulSoup import BeatifulSoup

regex_link = re.compile(r"(http[s]?://[^<> \"\x01]+)[,.]?")

def everything_between(text,begin,end):
    idx1=content.find(begin)
    idx2=content.find(end,idx1)
    return content[idx1+len(begin):idx2].strip()

@saxo.event("PRIVMSG")
def link(irc):
    search = regex_link.search(irc.text)
    if search:
        if irc.sender.startswith("#"):
            irc.client("link", irc.sender, search.group(1))
            URLObject = urllib2.urlopen(search.group(1))
            html = BeautifulSoup(URLObject.read())
            title = html.find('title')
            irc.say(title)
