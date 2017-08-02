USERNAME="xxxxxxxxx"
PASSWORD="xxxxxxxxxx"
TESSERACT_EXE_LOCATION="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

#Do not edit below this line

import hashlib
import time
import json
import base64
from collections import OrderedDict
import requests
from requests.structures import CaseInsensitiveDict
from PIL import Image
import pytesseract
from StringIO import StringIO
import traceback
from threading import Thread,Lock
from timedqueue import TimedQueue
GLOBAL_LOCK=Lock()
TIME_QUEUE=TimedQueue()
TIME_QUEUE.put(1)
pytesseract.pytesseract.tesseract_cmd=TESSERACT_EXE_LOCATION
sess=requests.session()
UHASH=""
FW_LEVEL=0
SDK_LEVEL=0
SCAN_LEVEL=0
AV_LEVEL=0
IP_LEVEL=0
ADW_LEVEL=0
def md5(s):
	return hashlib.md5(s).hexdigest()
def bcod(s):
	x=base64.b64encode(s)
	return x.replace("=","")
def new_default_headers():
	return CaseInsensitiveDict({"User-Agent":"Dalvik/2.1.0 (Linux; U; Android 7.1.1; ONEPLUS A3003 Build/NMF26F)","Accept-Encoding":"gzip","Connection":"keep-alive"})
requests.sessions.default_headers=new_default_headers
def dorequest(*args,**kwargs):
	TIME_QUEUE.get()
	TIME_QUEUE.put(1,1)
	with GLOBAL_LOCK:
		return sess.get(*args,**kwargs)
def buildurl(php,options=[]):
	global UHASH,USERNAME,PASSWORD
	paramstring1=USERNAME
	paramstring2=PASSWORD
	currenttime="{0:.0f}".format(time.time())
	paramcontext=OrderedDict()
	if options==[]:
		paramcontext[""]=""
	for (p,q) in options:
		paramcontext[p]=q
	paramcontext["time"]=currenttime
	paramcontext["user"]=USERNAME
	paramcontext["pass"]=PASSWORD
	paramcontext["uhash"]=UHASH
	localobject1=json.dumps(paramcontext,separators=(",",":"))
	paramcontext=bcod(localobject1)
	localobject2=md5(str(len(localobject1))+md5(currenttime))
	paramstring1=paramstring1+md5(md5(paramstring2))
	paramstring2=localobject2
	localobject1=md5(currenttime+localobject1)
	paramstring2 = md5("aeffI" + md5(md5(bcod(paramstring2))))
	paramstring1 = bcod(paramstring1)
	localobject1 = bcod(localobject1)
	paramstring1=md5(md5(paramstring2+md5(md5(paramstring1)+localobject1)))
	return "https://api.vhack.cc/v/8/"+php+"?user="+paramcontext+"&pass="+paramstring1
def updatesdk():
	d=dorequest(buildurl("vh_updateInfo.php",[("utype","sdk")]))
	v=d.json()
	print v
	try:
		x=dorequest(buildurl("vh_tasks.php"))
		print x.text
		x=x.json()
		totaltasks=len(x["data"])
	except:
		totaltasks=0
	print "Total tasks running {0}".format(totaltasks)
	if totaltasks<14:
		toup=gettoupdate()
		d=dorequest(buildurl("vh_addUpdate.php",[("utype",toup)]))
		print d.text
		d=dorequest(buildurl("vh_fillTasks.php",[("utype",toup)]))
		print d.text
def gettoupdate():
	v=[(FW_LEVEL,"fw"),(ADW_LEVEL,"adw"),(SDK_LEVEL,"sdk"),(SCAN_LEVEL,"scan"),(IP_LEVEL,"ipsp"),(AV_LEVEL,"av")]
	return min(v)[1]
def update():
	global UHASH,FW_LEVEL,ADW_LEVEL,SDK_LEVEL,SCAN_LEVEL,IP_LEVEL,AV_LEVEL
	d=dorequest(buildurl("vh_update.php"))
	v=d.json()
	print v
	UHASH=v["uhash"]
	FW_LEVEL=int(v["fw"])
	ADW_LEVEL=int(v["adw"])
	SDK_LEVEL=int(v["sdk"])
	SCAN_LEVEL=int(v["scan"])
	IP_LEVEL=int(v["ipsp"])
	AV_LEVEL=int(v["av"])
	updatesdk()
def _update():
	time.sleep(20)
	while True:
		try:
			update()
		except:
			traceback.print_exc()
		time.sleep(20)
def gettext(d):
	d=base64.b64decode(d)
	d=StringIO(d)
	d=Image.open(d)
	return pytesseract.image_to_string(d,config="--oem 0")
def getplayerlist():
	players=[]
	d=dorequest(buildurl("vh_getImg.php",[("by","0")]))
	d=d.json()
	for p in d["data"]:
		q=gettext(p["img"]).lower()
		print q.encode("utf-8")
		if ("firewall" in q)&("fbi" not in q):
			players.append(p["hostname"])
	return players
def hackplayer(p):
	print "Hacking {0}".format(p)
	v=dorequest(buildurl("vh_scanHost.php",[("hostname",p)]))
	print v.text
	target=v.json()["ipaddress"]
	d=dorequest(buildurl("vh_loadRemoteData.php",[("target",target)]))
	d=d.json()
	chance=d["winchance"]
	if chance>=80:
		print "Sending trojan to {0}".format(target)
		d=dorequest(buildurl("vh_trTransfer.php",[("port","0"),("target",target)]))
		print d.text
		d=d.json()
		if d["result"]=="0":
			print "Won {0}, total {1}".format(d["amount"]/1000,d["newmoney"]/1000)
def hackplayers():
	while True:
		try:
			v=getplayerlist()
			for p in v:
				try:
					hackplayer(p)
				except Exception as e:
					print e
		except Exception as e:
			print e
if __name__=="__main__":
	update()
	Thread(target=_update).start()
	hackplayers()
