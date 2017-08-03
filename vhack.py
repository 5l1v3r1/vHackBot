USERNAME="xxxxxxxxx"
PASSWORD="xxxxxxxxxx"
PROXY=None
TESSERACT_EXE_LOCATION="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

#Do not edit below this line

import wx
import wx.xrc

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,336 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Rank", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		bSizer1.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.m_textCtrl231 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl231.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_textCtrl231.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer1.Add( self.m_textCtrl231, 0, wx.ALL|wx.EXPAND, 2 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Score", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		bSizer12.Add( self.m_staticText22, 1, wx.ALL, 5 )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Reputation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		bSizer12.Add( self.m_staticText23, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer12, 0, wx.EXPAND, 5 )
		
		bSizer212 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrl24 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl24.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_textCtrl24.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer212.Add( self.m_textCtrl24, 1, wx.ALL, 2 )
		
		self.m_textCtrl212 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl212.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_textCtrl212.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer212.Add( self.m_textCtrl212, 1, wx.ALL, 2 )
		
		
		bSizer1.Add( bSizer212, 0, wx.EXPAND, 5 )
		
		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Money", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		bSizer1.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		self.m_textCtrl2121 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl2121.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_textCtrl2121.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer1.Add( self.m_textCtrl2121, 0, wx.ALL|wx.EXPAND, 2 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Firewall Level", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer2.Add( self.m_staticText5, 1, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"SDK Level", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer2.Add( self.m_staticText6, 1, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Scan Level", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer2.Add( self.m_staticText7, 1, wx.ALL, 5 )

		self.m_staticText700 = wx.StaticText( self, wx.ID_ANY, u"Spam Level", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText700.Wrap( -1 )
		bSizer2.Add( self.m_staticText700, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_textCtrl2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer21.Add( self.m_textCtrl2, 1, wx.ALL, 2 )
		
		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl21.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_textCtrl21.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer21.Add( self.m_textCtrl21, 1, wx.ALL, 2 )
		
		self.m_textCtrl22 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl22.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_textCtrl22.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer21.Add( self.m_textCtrl22, 1, wx.ALL, 2 )

		self.m_textCtrl2200 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl2200.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_textCtrl2200.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer21.Add( self.m_textCtrl2200, 1, wx.ALL, 2 )
		
		
		bSizer1.Add( bSizer21, 0, wx.EXPAND, 5 )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Antivirus Level", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		bSizer22.Add( self.m_staticText51, 1, wx.ALL, 5 )
		
		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"Spyware Level", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		bSizer22.Add( self.m_staticText61, 1, wx.ALL, 5 )
		
		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, u"IP Spoof Level", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		bSizer22.Add( self.m_staticText71, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer22, 0, wx.EXPAND, 5 )
		
		bSizer211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrl23 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl23.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_textCtrl23.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer211.Add( self.m_textCtrl23, 1, wx.ALL, 2 )
		
		self.m_textCtrl211 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl211.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_textCtrl211.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer211.Add( self.m_textCtrl211, 1, wx.ALL, 2 )
		
		self.m_textCtrl221 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl221.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_textCtrl221.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer211.Add( self.m_textCtrl221, 1, wx.ALL, 2 )
		
		
		bSizer1.Add( bSizer211, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass

app=wx.App(False)
MAINFRAME=MyFrame1(None)
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
import locale
locale.setlocale(locale.LC_ALL,"US")
GLOBAL_LOCK=Lock()
TIME_QUEUE=TimedQueue()
IP_QUEUE=TimedQueue()
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
SPAM_LEVEL=0
RAM_LEVEL=0
def saveip(x):
	t=time.time()+3660
	IP_QUEUE.put(t,3660)
	try:
		v=json.loads(open("ips.json",'r').read())
	except:
		v={}
	v[x]=t
	w=open("ips.json",'w')
	json.dump(v,w)
	w.close()
def loadips():
	try:
		v=json.loads(open("ips.json",'r').read())
	except:
		v={}
	for p in v:
		y=v[p]-time.time()
		if y>0:
			IP_QUEUE.put(p,y)
		else:
			IP_QUEUE.put(p)
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
	kwargs["proxies"]={"http":PROXY,"https":PROXY}
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
	global RAM_LEVEL
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
	if totaltasks<RAM_LEVEL:
		toup=gettoupdate()
		d=dorequest(buildurl("vh_addUpdate.php",[("utype",toup)]))
		print d.text
		d=dorequest(buildurl("vh_fillTasks.php",[("utype",toup)]))
		print d.text
def gettoupdate():
	v=[(FW_LEVEL,"fw"),(ADW_LEVEL,"adw"),(SDK_LEVEL/6,"sdk"),(SCAN_LEVEL,"scan"),(IP_LEVEL,"ipsp"),(AV_LEVEL,"av"),(SPAM_LEVEL/2,"spam")]
	return min(v)[1]
def update():
	global UHASH,FW_LEVEL,ADW_LEVEL,SDK_LEVEL,SCAN_LEVEL,IP_LEVEL,AV_LEVEL,SPAM_LEVEL,RAM_LEVEL
	d=dorequest(buildurl("vh_update.php"))
	v=d.json()
	print v
	UHASH=v["uhash"]
	FW_LEVEL=int(v["fw"])
	wx.CallAfter(MAINFRAME.m_textCtrl2.SetValue,v["fw"])
	ADW_LEVEL=int(v["adw"])
	wx.CallAfter(MAINFRAME.m_textCtrl211.SetValue,v["adw"])
	SDK_LEVEL=int(v["sdk"])
	wx.CallAfter(MAINFRAME.m_textCtrl21.SetValue,v["sdk"])
	SCAN_LEVEL=int(v["scan"])
	wx.CallAfter(MAINFRAME.m_textCtrl22.SetValue,v["scan"])
	IP_LEVEL=int(v["ipsp"])
	wx.CallAfter(MAINFRAME.m_textCtrl221.SetValue,v["ipsp"])
	AV_LEVEL=int(v["av"])
	wx.CallAfter(MAINFRAME.m_textCtrl2200.SetValue,v["spam"])
	SPAM_LEVEL=int(v["spam"])
	RAM_LEVEL=int(v["ram"])
	wx.CallAfter(MAINFRAME.m_textCtrl23.SetValue,v["av"])
	wx.CallAfter(MAINFRAME.m_textCtrl2121.SetValue,locale.format("%d",int(v["money"])/1000,grouping=True))
	wx.CallAfter(MAINFRAME.m_textCtrl24.SetValue,v["score"])
	wx.CallAfter(MAINFRAME.m_textCtrl212.SetValue,v["elo"])
	wx.CallAfter(MAINFRAME.m_textCtrl231.SetValue,str(v["rank"]))
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
def hackplayer(p,isip=False):
	if isip:
		target=p
		print "Hacking {0}".format(p)
	else:
		print "Hacking {0}".format(p)
		v=dorequest(buildurl("vh_scanHost.php",[("hostname",p)]))
		print v.text
		target=v.json()["ipaddress"]
	d=dorequest(buildurl("vh_loadRemoteData.php",[("target",target)]))
	d=d.json()
	chance=d["winchance"]
	if chance>=60:
		print "Sending trojan to {0}".format(target)
		d=dorequest(buildurl("vh_trTransfer.php",[("port","0"),("target",target)]))
		print d.text
		d=d.json()
		if d["result"]=="0":
			wx.CallAfter(MAINFRAME.m_textCtrl2121.SetValue,locale.format("%d",d["newmoney"]/1000,grouping=True))
			wx.CallAfter(MAINFRAME.m_textCtrl212.SetValue,str(d["elo"]))
			if d["amount"]>=20000000:
				saveip(target)
			print "Won {0}, total {1}".format(d["amount"]/1000,d["newmoney"]/1000)
def getip():
	v=IP_QUEUE.get_nowait()
	try:
		w=json.loads(open("ips.json",'r').read())
		w.pop(v,None)
		m=open("ips.json",'w')
		json.dump(w,m)
		m.close()
	except:
		pass
	return v
def hackplayers():
	while True:
		while True:
			try:
				p=getip()
				hackplayer(p,True)
			except:
				break
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
	loadips()
	update()
	Thread(target=_update).start()
	Thread(target=hackplayers).start()
	MAINFRAME.Show()
	app.MainLoop()
