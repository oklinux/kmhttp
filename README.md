# 酷猫HTML UI框架脚本 0.1
# 特性：
支持PyQt4/5及Chrome作为窗口输出支撑。
可利用Python、Shell、PHP等等作为 主程序开发语言。
使用HTML、JS、CSS等作为界面设计语言。
本脚本是基于Python3开发的。
# 使用方法：
1、Python3
需要在程序目录下写一个包含start(url,data)方法的main.py
其中，url是HTML界面发送的链接，由< a href=main***** >产生。链接开天务必是main。data是HTML提交的所有数据，不大于128KB。
该start方法必须返回新产生的HTML界面代码。
2、其它语言
在程序目录下必须有例如main.sh/main.php/main等主执行程序，url将以参数的形式传递给他们，所以连接数据被保存到link.dat文件中，供他们使用处理。
他们必须产生main.html文件作为主界面。
# 关于：
作者：陈欧侃
授权协议：GPLv2
