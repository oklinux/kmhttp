#!.usr/bin/python3
#encoding='utf-8'
import os
import sys

anzhuang_sh='''#!nin/bash
mkdir -p /usr/share/okaywx
cp %s /usr/share/okaywx
echo "#!/bin/bash
python3 /usr/share/okaywx/okaywx.py RUN >/dev/null &
">/usr/bin/okaywx
chmod -R 777 /usr/share/okaywx /usr/bin/okaywx
tee<<desktop>/usr/share/applications/okaywx.desktop
[Desktop Entry]
Name=Okay Wenxin
Name[zh_CN]=Okay微信
Exec=okaywx
Icon=
Type=Application;Network;Internet
desktop
rm -rf $0
''' % sys.argv[0]

def anzhuang():
  if sys.argv[1]:
    if sys.argv[1] == 'setup':
      az=open('setup.sh','w')
      az.write(anzhuang_sh)
      az.close()
      os.system('sudo bash ./setup.sh')


def ming():
  return 'Okay微信Linux版'
def dizhi():
  return 'http://wx.qq.com/'

#检查pynput依赖，如过未安装，就使用pip安装。
def jianchaYL(yilai1,yilai):
  test='''from %s import *
import os,sys
''' % yilai1

  if zhixingJB(test) != 0:
    if not os.path.isfile('/usr/bin/apt'):
        os.system('sudo apt update')
    elif not os.path.isfile('/usr/bin/apt-get'):
        os.system('sudo apt-get update')
    
    if os.path.isfile('/usr/bin/yum'):
      os.system('sudo yum install python3-'+str(yilai))
    if os.path.isfile('/usr/bin/apt-get'):
      os.system('sudo apt-get install -y python3-'+str(yilai))
    if os.path.isfile('/usr/bin/yum'):
      os.system('sudo dmf install pyhon3-'+str(yilai))



def zhixingJB(JMJB):
  JBWenjian=open('browser.py','w')
  JBWenjian.write(JMJB)
  JBWenjian.close()
  zhixingJG=os.system('python3 browser.py')
  return zhixingJG


def jiemian():
  JBQt4='''
import sys
import okaywx
mc=[okaywx.ming(),'ok']
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
app = QApplication(mc)
browser = QWebView()
browser.load(QUrl(okaywx.dizhi()))
browser.show()
app.exec_()
'''
  JBQt5='''
import sys
import okaywx
mc=[okaywx.ming(),'ok']
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import *
app = QApplication(mc)
browser = QWebView()
browser.load(QUrl(okaywx.dizhi()))
browser.show()
app.exec_()
'''
  JBQt51='''
import sys
import okaywx
mc=[okaywx.ming(),'ok']
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
app = QApplication(mc)
browser = QWebEngineView()
browser.load(QUrl(okaywx.dizhi()))
browser.show()
app.exec_()
'''
  if zhixingJB(JBQt51) != 0:
    if zhixingJB(JBQt5) != 0:
      if zhixingJB(JBQt4) != 0:
        jianchaYL('PyQt5.QtWebEngineWidgets','pyqy5.qtwebengine')
        if zhixingJB(JBQt51) != 0:
          jianchaYL('PyQt5.QtWebKitWidgets','pyqy5.qtwebkit')
          if zhixingJB(JBQt5) != 0:
            os.system('/usr/bin/chrome --app='+dizhi())


if __name__ == '__main__':
  anzhuang()
  jiemian()
