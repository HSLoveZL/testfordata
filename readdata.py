# coding=utf-8
import xml.dom.minidom


dom=xml.dom.minidom.parse('/home/hongsh/testfordata/login.xml')
root=dom.documentElement

logins=root.getElementsByTagName('null')
username=logins[0].getAttribute('username')
password=logins[0].getAttribute('passwd')
prompt_info=logins[0].firstChild.data

print username
print prompt_info

