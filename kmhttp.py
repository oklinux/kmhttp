#!.usr/bin/python3
#encoding='utf-8'

import os
import sys
import time
import socket
from http.server import *
from multiprocessing import *
#声明一个将要绑定的IP和端口，这里是用本地地址
def duankou(cs):
  dk=35460
  dkjilu='/run/shm/dkjilu.log'
  if os.path.isfile(dkjilu):
    dk1=open(dkjilu,'r')
    dk=dk1.read()
    dk1.close()
    dk=int(dk)+cs
  dk2=open(dkjilu,'w')
  dk2.write(str(dk))
  dk2.close()
  return dk

def fuwuuqi():
  return('localhost', duankou(1))

def dizhi():
  return 'http://localhost:'+str(duankou(0))+'/main'

def mulu(chanshu):
  fankui=os.path.dirname(sys.argv[0])
  if fankui=='':
    fankui='./'
  if chanshu=='daodongqian':
    os.chdir(fankui)
  bianliang=os.environ
  if chanshu=='home':
    fankui=bianliang.get('HOME')
  if chanshu=='daohome':
    os.chdir(bianliang.get('HOME'))
  if chanshu=='linshi':
    fankui=bianliang.get('TEMP')
    if os.path.isdir('/tmp'):
      fankui='/tmp'
      
  return fankui

#得到要发送的数据信息
def HuoquHTML(data):
  fankui="" 
  QingqiuLX = data.decode('utf-8')
  QingqiuLX = QingqiuLX[0:QingqiuLX.find("/")].rstrip()
  
  #判断是GET请求还是POST请求
  if QingqiuLX=="GET":
    URL = PanduanLX(data,'GET /',' HTTP/1.1')
  if QingqiuLX=="POST":
    URL = PanduanLX(data,'POST /',' HTTP/1.1')
    fankui=' '
  URL=URL.decode('utf-8')
  fankui=ShujuFH(URL,fankui,data)
  return fankui
#

#筛选出请求的一个方法
def PanduanLX(data,startStr,endStr):
  dataIndex = data.decode("utf-8")
  startIndex = dataIndex.index(startStr)
  if startIndex>=0:
    startIndex += len(startStr)
    endIndex = dataIndex.index(endStr)
    return data[startIndex:endIndex]

#请求返回数据
def ShujuFH(lujing,fankui,data):
  fankui=ShezhiBMLX(data,fankui,"text/html",lujing,"r")
  if os.path.exists(lujing) and os.path.isfile(lujing):
    if ".html" in lujing:
      fankui=ShezhiBMLX(data,fankui,"text/html",lujing,"r")
    if ".css" in lujing:
      fankui=ShezhiBMLX(data,fankui,"text/css",lujing,"r")
    if ".js" in lujing:
      fankui=ShezhiBMLX(data,fankui,"application/x-javascript",lujing,"r")
    if ".gif" in lujing:
      fankui=ShezhiBMLX(data,fankui,"image/gif",lujing,"rb")
    if ".doc" in lujing:
      fankui=ShezhiBMLX(data,fankui,"application/msword",lujing,"rb")
    if ".mp4" in lujing:
      fankui=ShezhiBMLX(data,fankui,"video/mpeg4",lujing,"rb")
    else:
      fankui=ShezhiBMLX(data,fankui,"application/data",lujing,"rb")
      
  return fankui

#设置编码格式和文件类型
def ShezhiBMLX(data,fankui,type,file,openFileType):
  fankui='HTTP/1.1 200 OK \n'
  fankui+="Content-Type: "+type+";charset=utf-8"
  fankui+="Content-Length: "+str(WenjianDX(file))+"\n"+"\n"
  fankui = fankui.encode(encoding = 'utf-8')
    
  if os.path.isfile(file):
    WenjianNR=open(file,openFileType)
    fankui+=HuoquWJ(fankui,WenjianNR)
  else:
    fankui+=jiaoben(data,file)

  return fankui

#调用主程序生成HTML界面
def jiaoben(data,URL):
  fankui=''
  mulu('daodongqian')
  mingling=''
  if os.path.isfile('main.py'):
    import main
    fankui=main.start(URL,data)
  else:
    fankui=shouming()
    JBWenjian=open('link.dat','wb')
    JBWenjian.write(data)
    JBWenjian.close()
    if os.path.isfile('main.sh'):
      mingling=print('sh ./main.sh '+URL)
    if os.path.isfile('main'):
      mingling=print('./main '+URL)
    if os.path.isfile('main.php'):
      mingling=print('php main.php '+URL)
  if mingling != '':
    os.system(mingling)
  
  fankui = fankui.encode(encoding = 'utf-8')
  if os.path.isfile('main.heml'):
    WenjianNR=open('main.html','r')
    fankui=HuoquWJ(fankui,WenjianNR)
  return fankui

#获#打开文件，这里不直接写，二是去取要发送的文件再写
def HuoquWJ(fankui,file):
    for yihang in file:
      fankui+=yihang
    return fankui

#取要发送数据的大小，根据HTTP协议规范，要提前指定发送的实体内容的大小
def WenjianDX(Wenjianming):
  size=1048676
  if os.path.isfile(Wenjianming):
    fileobject=open(Wenjianming)
    fileobject.seek(0,2)
    size = fileobject.tell()
    
  return size
 
def shouming():
  fankui='''<html><head>
  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
  <meta http-equiv="CONTENT-TYPE" content="text/html; charset=UTF-8">
  <title>酷猫UI说明</title>
</MATA></head>
<!--WZBT--><h1><CONTER>酷猫HTML UI框架脚本 0.1
</vonter></h1><P><!--WZNR--><h2>特性：</h2></p>
<P>支持PyQt4/5及Chrome作为窗口输出支撑。</p>
<P>可利用Python、Shell、PHP等等作为 主程序开发语言。</p>
<P>使用HTML、JS、CSS等作为界面设计语言。</p>
<P>本脚本是基于Python3开发的。</p>
<P><h2>使用方法：</h2></p>
<P>1、Python3</p>
<P>需要在程序目录下写一个包含start(url,data)方法的main.py。</p>
<P>其中，url是HTML界面发送的链接，由< a href=main***** >产生。链接开天务必是main。data是HTML提交的所有数据，不大于128KB。</p>
<P>该start方法必须返回新产生的HTML界面代码。</p>
<P>2、其它语言</p>
<P>在程序目录下必须有例如main.sh/main.php/main等主执行程序，url将以参数的形式传递给他们，所以连接数据被保存到link.dat文件中，供他们使用处理。</p>
<P>他们必须产生main.html文件作为主界面。</p>
<P><h2>关于：</h2></p>
<P>作者：陈欧侃</p>
<P>授权协议：GPLv2</p>
'''

  return fankui

class WebServer():
  def run(self):
    #实例化一个Socket
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定IP和端口
    sock.bind(fuwuuqi())
    print ('starting up on '+dizhi())
    #设置监听
    sock.listen(1)
    #这里首先给个死循环，其实这里是需要多线程的，再后续版本将会实现
    while True:
      #接受客户端的请求并得到请求信息和请求*的端口信息
      connection, client_address = sock.accept()
      print ('waiting for a connection') 
      try:
        #获取请求信息
        data = connection.recv(131024)
        if data:
           #发送请求信息
           XinxiFH = HuoquHTML(data) 
           connection.sendall(XinxiFH)
      finally:
        connection.close()


def zhixingJB(JMJB):
  JBWenjian=open('browser.py','w')
  JBWenjian.write(JMJB)
  JBWenjian.close()
  zhixingJG=os.system('python3 browser.py')
  return zhixingJG
  
def jiemian():
  JBQt4='''
import sys
import kmhttp
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
app = QApplication(sys.argv)
browser = QWebView()
browser.load(QUrl(kmhttp.dizhi()))
browser.show()
app.exec_()
'''
  JBQt5='''
import sys
import kmhttp
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import *
app = QApplication(sys.argv)
browser = QWebView()
browser.load(QUrl(kmhttp.dizhi()))
browser.show()
app.exec_()
'''
  JBQt51='''
import sys
import kmhttp
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
app = QApplication(sys.argv)
browser = QWebEngineView()
browser.load(QUrl(kmhttp.dizhi()))`
browser.show()
app.exec_()
'''
  os.chdir(mulu('dongqian'))
  time.sleep(2)
  if zhixingJB(JBQt5) != 0:
    if zhixingJB(JBQt51) != 0:
      if zhixingJB(JBQt4) != 0:
        os.system('/usr/bin/chrome --app='+dizhi())
	
	

if __name__ == '__main__':
  server = WebServer()
  p = Process(target = server.run)
  p.start()
  
  jiemian()
  
  