#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import vk
import time
import re
###########################
########HELLO THERE########
###########################

# try:
# 	tokenfile=open('git/parser/input.data','r')
# except FileNotFoundError:
# 	print('ERR000[FileNotFoundError]')
# 	quit()
# try:
# 	tokenstate=tokenfile.readlines()
# 	token=tokenstate[0][:-1]####################### 1st line-token
# 	group=tokenstate[1]############################ 2nd line-group id
# except:
# 	print('ERR320[DataParseFromFileError]')
# 	quit()

token=input('VK token:')
group=int(input('Group ID:'))
f=open(input('File name:'),'w')

# token=''
# group=
# f=open('','w')

countof=int(input('Count of users for check [[mod 1000 or 100=0]]:'))
sortof=input('id_asc/id_desc/\'\' ,def='': ')
to=input('Timeout(experimental)[75 for slow ,def=75]:')
if to=='':
	to=75
else:
	to=int(to)
session = vk.Session(access_token=token)
api = vk.API(session, v='5.8', lang='en', timeout=to)
print('Successful start...')
outer=''
off=0
step=100
div=r'<div class="m"><a href="#link"><img src="#avatar" class="i"></a><div class="s"><div class="t"><text  clickabil albums="#albcount" onclick="k(this)">FriendC: @##1    AlbumC: @##2 AM17PC: @##3 SavedPC: @##4</text> ........................................................................<a href="@link">GO</a></div></div><diva hidden="true">Anime;Saved</diva></div>'
while api.groups.getMembers(group_id=group,sort=sortof,fields='',count=step,offset=off)['users']!=[] and off<countof:
	time.sleep(1)
	m=api.groups.getMembers(group_id=group,sort=sortof,fields='',count=step,offset=off)['users']
	off+=step
	time.sleep(1)
	avatars=api.users.get(user_ids=",".join(str(x) for x in m),fields='photo_50')
	time.sleep(1)
	for x in range(len(m)):
		albums=''
		try:
			tmp=api.photos.getAlbums(owner_id=m[x],need_system=1)['items']
		except vk.exceptions.VkAPIError:
			continue
		for p in range(len(tmp)):
			albums+=tmp[p]['title']+':'+str(tmp[p]['size'])+';'
		temp=re.findall(r'[^0-9]*\'s saved photos\:[0-9]*',albums)
		if temp!=[]:
			try:
				outer+=div.replace('#link','https://vk.com/id'+str(m[x])).replace('#albcount',albums).replace('@##4','____'[:-len(str(temp[0].split(':')[1]))]+temp[0].split(':')[1]).replace('@link','https://vk.com/album'+str(m[x])+'_000').replace('#avatar',avatars[x]['photo_50']).replace('@##2','_____'[:-len(str(len(tmp)))]+str(len(tmp)-2))+'\n'
			except IndexError:
				continue
	m.clear()
	avatars.clear()
	time.sleep(2)
s=r'<!DOCTYPE html><html><head>	<title>Page of users</title></head><body>'
s2='<script type=\"text/javascript\">	function k(item) {		if (item.getAttribute(\'clickabil\')!=undefined) {		var temp=item.getAttribute(\'albums\');		var templist=temp.split(\';\');		var temps=\'\';		for (var i =0; i<templist.length-1;i++) {			var templ=templist[i].split(\':\');			temps+=templ[0]+\' [\'+templ[1]+\'] \'+\';\';}		alert(temps);}}</script><style type="text/css">.m {height: 34;width: 840px;border: 1px solid #2a5885;border-radius: 0px;}.i {position: relative;height:30px;width:30px;margin:4px 0px 0px 4px;border:1px solid  red;border-radius: 1px }.s {height:14px;float:right;margin:11px 0px 0px 0px;}.t {font-size:14px;}</style></body></html>'
f.write(s+'\n'+outer+'\n'+s2)
f.close()