import base64,hashlib,os,random,re,requests,shutil,string,sys,urllib,urllib2,json,urlresolver,ssl
import xbmc,xbmcaddon,xbmcgui,xbmcplugin,xbmcvfs
from addon.common.addon import Addon
from addon.common.net import Net
from resources import control

addon_id   = 'script.module.kratos'
selfAddon  = xbmcaddon.Addon(id=addon_id)
addon      = Addon(addon_id, sys.argv)
addon_name = selfAddon.getAddonInfo('name')
icon       = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
fanart     = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
User_Agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
putlockerhd      = 'http://putlockerhd.co'
ccurl      = 'http://cartooncrazy.me'
s          = requests.session()
net        = Net()
ccurl      = 'http://cartooncrazy.me'
xxxurl     ='http://www.xvideos.com'
kidsurl    = base64.b64decode ('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3NDbGFya2VJc0JhY2svU3RyZWFtSHViL21hc3Rlci9MaW5rcy9LaWRzL2tpZHNjb3JuZXIueG1s')
docurl     = 'http://documentaryheaven.com'
mov2       = 'http://zmovies.to'
wwe        = 'http://watchwrestling.in'
tv         = base64.b64decode ('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3NDbGFya2VJc0JhY2svU3RyZWFtSHViL21hc3Rlci9MaW5rcy8yNDcvMjQ3dHYueG1s')
proxy      = 'http://www.justproxy.co.uk/index.php?q='



def regex_from_to(text, from_string, to_string, excluding=True):
	if excluding:
		try: r = re.search("(?i)" + from_string + "([\S\s]+?)" + to_string, text).group(1)
		except: r = ''
	else:
		try: r = re.search("(?i)(" + from_string + "[\S\s]+?" + to_string + ")", text).group(1)
		except: r = ''
	return r


def regex_get_all(text, start_with, end_with):
	r = re.findall("(?i)(" + start_with + "[\S\s]+?" + end_with + ")", text)
	return r


def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
		params=sys.argv[2]
		cleanedparams=params.replace('?','')
		if (params[len(params)-1]=='/'):
			params=params[0:len(params)-2]
		pairsofparams=cleanedparams.split('&')
		param={}
		for i in range(len(pairsofparams)):
			splitparams={}
			splitparams=pairsofparams[i].split('=')
			if (len(splitparams))==2:
				param[splitparams[0]]=splitparams[1]
	return param


def addDir(name,url,mode,iconimage,fanart,description):
	u=sys.argv[0]+"?url="+url+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={"Title": name,"Plot":description})
	liz.setProperty('fanart_image', fanart)
	if mode==3 or mode==7 or mode==17 or mode==15 or mode==23 or mode==30 or mode==27 or mode ==36 or mode==39 or mode==50:
		liz.setProperty("IsPlayable","true")
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	else:
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok
	xbmcplugin.endOfDirectory
	
def addDirPlay(name,url,mode,iconimage,fanart,description):
	u=sys.argv[0]+"?url="+url+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	if mode==44:
		liz.setProperty("IsPlayable","true")
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	else:
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok
	xbmcplugin.endOfDirectory

def OPEN_URL(url):
	headers = {}
	headers['User-Agent'] = User_Agent
	link = s.get(url, headers=headers, verify=False).text
	link = link.encode('ascii', 'ignore')
	return link
	
def Open_Url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
		
def xxx(url):
        link = OPEN_URL(url)
        all_videos = regex_get_all(link, 'class="thumb-block ">', '</a></p>')
        for a in all_videos:
			name = regex_from_to(a, 'title="', '"')
			name = str(name).replace("&amp;","&").replace('&#39;',"'").replace('&quot;','"').replace('&#39;',"'").replace('&#039;',"'")
			url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
			thumb = regex_from_to(a, '<img src="', '"')
			addDir(name,'http://www.xvideos.com'+url,27,thumb,'','')
        xxxadd_next_button(link)
			

def xxxadd_next_button(link):
			try:
				if '/tags/' in link:
					link = str(link).replace('\n','').replace('\r','').replace('\t','').replace(' ','').replace('  ','')
					nextp=regex_from_to(link,'<aclass="active"href="">.+?</a></li><li><ahref="','"')
					addDir('[B][COLOR ghostwhite]Next Page>>> [COLOR dodgerblue] Keep going and you will go blind[/COLOR][/B]',xxxurl+nextp,24,'','','')
			except: pass
			
			try:
				if '/tags/' not in link:
					link = str(link).replace('\n','').replace('\r','').replace('\t','').replace(' ','').replace('  ','')
					nextp = regex_from_to(link,'<aclass="active"href="">.+?</a></li><li><ahref="','"')
					xbmc.log(str(nextp))
					addDir('[B][COLOR ghostwhite]Next Page[/COLOR][/B]',xxxurl+nextp,24,'','','')
			except: pass
			return
			
def xxxgenre(url):
        link = passpopup(url)
        link = OPEN_URL(link)
        main = regex_from_to(link,'<strong>All tags</strong>','mobile-hide')
        all_videos = regex_get_all(main, '<li>', '</li>')
        for a in all_videos:
			name = regex_from_to(a, '"><b>', '</b><span').replace("&amp;","&")
			url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
			url = url+'/'
			thumb = regex_from_to(a, 'navbadge default">', '<')
			addDir('%s     [B][COLOR red](%s Videos)[/COLOR][/B]' %(name,thumb),xxxurl+url,24,'','','')
		
def resolvexxx(url):
	base = 'http://www.xvideos.com'
	page  = OPEN_URL(url)
	page=urllib.unquote(page.encode("utf8"))
	page=str(page).replace('\t','').replace('\n','').replace('\r','').replace('                                            	','')
	play = regex_from_to(page,"setVideoUrlHigh.+?'","'")
	url = str(play).replace('[','').replace("'","").replace(']','')
        liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=icon)
        liz.setInfo(type='Video', infoLabels={'Title':description})
        liz.setProperty("IsPlayable","true")
        liz.setPath(str(url))
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
	
		
def passpopup(url):
 kb =xbmc.Keyboard ('', 'heading', True)
 kb.setHeading('Enter Password') # optional
 kb.setHiddenInput(True) # optional
 kb.doModal()
 if (kb.isConfirmed()):
    text = kb.getText()
    if 'zzz' in text:
       text = str(text).replace('zzz','/tags')
       return (str(xxxurl+text)).replace('%3a','').replace('%2f','')
    else:
        Msg="Incorrect Password\n\nPassword is available from\n[COLOR ghostwhite]https://www.facebook.com/groups/anonymouskodi/[/COLOR]"
        dialog = xbmcgui.Dialog()
        ok = dialog.ok('Oops... Incorrect Password', Msg)
        return False


def documentary(url):
#	addDir('DOCUMENTARY MOVIES',putlockerhd+'/documentary_movies',19,icon,fanart,'')
	OPEN = OPEN_URL(url)
	regex = regex_get_all(OPEN,'<h2><a href','alt="')
	for a in regex:
		url = regex_from_to(a,'="','"')
		title = regex_from_to(a,'">','<').replace("&amp;","&").replace('&#39;',"'").replace('&quot;','"').replace('&#39;',"'").replace('&#8211;',' - ').replace('&#8217;',"'").replace('&#8216;',"'").replace('&#038;','&').replace('&acirc;','')
		thumb = regex_from_to(a,'img src="','"')
		vids = regex_from_to(a,'</a> (',')</h2>').replace('(','').replace(')','')
		if vids == "":
			addDir(title,url,36,thumb,fanart,'')
		else:
			addDir(title,docurl+url,35,thumb,fanart,'')
	try:
		link = re.compile('<li class="next-btn"><a href="(.+?)"').findall(OPEN)
		link = str(link).replace('[','').replace(']','').replace("'","")
		xbmc.log(str(link))
		if link == "":
			return False
		else:
			addDir('[B][COLOR dodgerblue]NEXT PAGE[/COLOR][/B]',link,35,thumb,fanart,'')
	except:pass
def resolvedoc(url):
	open = OPEN_URL(url)
	xbmc.log(str(open))
	url = regex_from_to(open,'height=".*?" src="','"')
	link = urlresolver.HostedMediaFile(url).resolve()
	liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
	liz.setInfo(type='Video', infoLabels={'Title': name, 'Plot': description})
	liz.setProperty('IsPlayable','true')
	liz.setPath(str(link))
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
	

def home():
	home = xbmc.executebuiltin('XBMC.RunAddon(plugin://plugin.video.kratos/?action=)')
	return home
	


params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None
query=None
type=None
# OpenELEQ: query & type-parameter (added 2 lines above)

try:
	url=urllib.unquote_plus(params["url"])
except:
	pass
try:
	name=urllib.unquote_plus(params["name"])
except:
	pass
try:
	iconimage=urllib.unquote_plus(params["iconimage"])
except:
	pass
try:
	mode=int(params["mode"])
except:
	pass
try:
	description=urllib.unquote_plus(params["description"])
except:
	pass
try:
	query=urllib.unquote_plus(params["query"])
except:
	pass
try:
	type=urllib.unquote_plus(params["type"])
except:
	pass
# OpenELEQ: query & type-parameter (added 8 lines above)

if mode==None or url==None or len(url)<1:
	CAT()

elif mode==2:
	INDEX2(url)

elif mode==3:
	LINKS(url)

elif mode==4:
	TV()

elif mode==6:
	EPIS(url)

elif mode==7:
	LINKS2(url,description)

elif mode==8:
	SEARCH(query,type)
# OpenELEQ: query & type-parameter (added to line above)

elif mode==9:
	GENRE(url)

elif mode==10:
	COUNTRY(url)

elif mode==11:
	YEAR(url)
	
elif mode==12:
	INDEX3(url)
	
elif mode==13:
	resolve(name,url,iconimage,description)
	
elif mode==19:
	putlockerhdread(url)
	
elif mode==15:
	putlockerhdplay(url)
	
elif mode==16:
	toonlist(url)
	
elif mode==17:
	resolvetoons(name,url,iconimage,description)
	
elif mode==18:
	toon_get(url)
	
elif mode==24:
	xxx(url)
	
elif mode==25:
	LiveTV()
	
elif mode==26:
	opencartooncrazy(url)
	
elif mode==27:
	resolvexxx(url)
	
elif mode==99:
	xxxgenre(url)
	
elif mode==30:
	resolvecartooncrazy(url,icon)
	
elif mode==31:
	xxxCAT()
	
elif mode==32:
	CartooncrazyList()
	
elif mode==33:
	listgenre(url)
	
elif mode==34:
	CartooncrazysubList(url)
	
elif mode==35:
	documentary(url)
	
elif mode==36:
	resolvedoc(url)
	
elif mode==43:
	wweopen(url)
	
elif mode==44:
	playwwe(url,description)
	
elif mode==45:
	wwepages(url)
	
elif mode==46:
	resolvetwentyfourseven(url,icon)
	
elif mode==47:
	opentwentyfourseven(url)

elif mode==48:
	tvlist(url)

elif mode==49:
	TVREQUESTCAT()
	
elif mode==50:
	TVREQUESTCATPLAY(name,url,icon)
	
elif mode==98:
	xxxstars(url)
	
elif mode==100:
	MovieCAT()
	
elif mode==999:
	home()





xbmcplugin.endOfDirectory(int(sys.argv[1]))