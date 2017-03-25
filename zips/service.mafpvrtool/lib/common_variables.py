#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import xbmc,xbmcgui,xbmcaddon,os,shutil,requests,time
import xbmcvfs
import re

addon_id = 'service.AnonymousPVRTools'

selfAddon = xbmcaddon.Addon(id=addon_id)
datapath = xbmc.translatePath(selfAddon.getAddonInfo('profile')).decode('utf-8')
addonfolder = xbmc.translatePath(selfAddon.getAddonInfo('path')).decode('utf-8')
artfolder = os.path.join(addonfolder,'resources','img')
msgok = xbmcgui.Dialog().ok
mensagemprogresso = xbmcgui.DialogProgress()

def copy_file(path):
	print "Copy file to addon_data... " + str(path)
	shutil.copy(path, os.path.join(datapath,'special://home'))
	print "File has been copied..."

def download_and_extract(name):
	print "starting download... " + str(name)
	start_time = time.time()
	r = requests.get(name, stream=True)
	if r.status_code == 200:
		with open(os.path.join(datapath,'special://home',name.split('/')[-1]), 'wb') as f:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f) 
		print "download finished..." + name
		print "elapsed time:" + str(time.time() - start_time)
	else:
		print "download failed (error status != 200)..." + name
		
		
# def replacemalicious():		
        # target = xbmc.translatePath('special://home/addons/plugin.video.MaverickTV/default.py')
        # home = xbmc.translatePath('special://home/addons/plugin.video.anonymous/resources/')
        # if os.path.exists(target):
            # file = open(os.path.join(home, 'mavdefault.py'))
            # data = file.read()
            # file.close()
            # file = open(target,"w")
            # file.write(data)
            # file.close()
            # xbmcgui.Dialog().notification('[COLOR green]Malicious Code Removed From[/COLOR] ','Maverick TV')
# targetfolder = xbmc.translatePath('special://home/addons/plugin.video.MaverickTV/')
# targetfile = open(os.path.join(targetfolder, 'default.py'))
# targetread = targetfile.read()
# targetfile.close()
# if 'anonymous' in targetread:
	# replacemalicious()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
if xbmcvfs.exists(xbmc.translatePath('special://home/userdata/sources.xml')):
        with open(xbmc.translatePath('special://home/userdata/sources.xml'), 'r+') as f:
                my_file = f.read()
                if re.search(r'http://kisakul.com/anonymous', my_file):
                        xbmc.log('===Anonymous===Source===Found===in===sources.xml===Not Deleting.===')
                else:
                        line1 = "you have Installed The Anonymous From An"
                        line2 = "Unofficial Source And Will Now Delete Please"
                        line3 = "Install From [COLOR red]http://kisakul.com/anonymous[/COLOR]"
                        line4 = "Removed Repo And Addon"
                        line5 = "successfully"
                        xbmcgui.Dialog().ok(addon_name, line1, line2, line3)
                        delete_addon = xbmc.translatePath('special://home/addons/'+addon_id)
                        delete_repo = xbmc.translatePath('special://home/addons/repository.anonymousgroup')
                        shutil.rmtree(delete_addon, ignore_errors=True)
                        shutil.rmtree(delete_repo, ignore_errors=True)
                        dialog = xbmcgui.Dialog()
                        xbmc.log('===DELETING===ADDON===+===REPO===')
                        xbmcgui.Dialog().ok(addon_name, line4, line5)
