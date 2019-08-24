# http://inamidst.com/saxo/
# Created by Sean B. Palmer

import re
import saxo

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
            content = open(search.group(1)).read()
            title = everything_between(content,'<title>','</title>')
            irc.say(title)
