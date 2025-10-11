
# run show or config commands on multiple junos Hosts
# needs pyez installed. Developed on python 3.7
# Gui handled by tkinker libary

LINES_HOSTS=5
LINES_INPUT=5
LINES_RESULTS=20
VERSION="1.0 beta"
MAX_THREADS=20
HOSTFILE_NAME="myhosts.txt"

from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import ttk
import re
import pprint
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from jnpr.junos.exception import ConfigLoadError
from jnpr.junos.exception import CommitError
from lxml import etree
from jnpr.junos.utils.config import Config
from io import StringIO
import threading

import sys
import socket
import time

def load_hosts():
    try:
        f=open(HOSTFILE_NAME)
        for line in f.read():
            hosts.insert(END,line)
        f.close()
    except OSError as err:
        return

def is_valid_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

def clicked_dns_lookup():
    ip_address=""
    content = hosts.get(1.0, END)
    s=re.split('\s',content)
    for i in range(len(s)-1,-1,-1):
        if s[i] == '' or s[i]== '\s':
            del s[i]
    for i in range(len(s)):
        if (i < len(s) -1) and (s[i+1][0:1] == '('):
            continue
        if s[i] == "\s" or s[i][0:1]=="(":
            continue
        if is_valid_ip(s[i]) == False:
            try:
                ip_address=socket.gethostbyname(str(s[i]))
                content=content.replace(s[i],s[i]+ ' ('+ip_address+')')
                hosts.delete("1.0",END)
                hosts.insert('insert',content)
            except:
                show_in_results("dns lookup failed for " + s[i] + '\n')

def clicked_show():
    for ip in get_my_hosts():
        process = threading.Thread(target=run_show, args=[ ip ])
        process.start()
        DevReq(1)

def run_show(ip):
    sema.acquire()
    content = commands.get(1.0,END)
    content = content + '\n'
    cmds=re.split('\n',content)
    string=""
    string="Result on host %s:\n" % (ip)
    dev = Device(host=ip, user=user.get(), passwd=passwd.get(), gather_facts=False)
    try:
        dev.open()
    except ConnectError as err:
        string=string+"Error: %s\n" % (err)
    else:
        for j in range (len(cmds)):
            if cmds[j] == "":
                continue
            tring=string+"Sending: "+cmds[j]+'\n'
            string=string+dev.cli(cmds[j], warning=False)
            string=string+"\n=============================================\n"
    show_in_results(string)
    string=""
    dev.close()
    DevReq(-1)
    sema.release()

def clicked_save_results():
    window.filename =  filedialog.asksaveasfilename(initialdir = ".",title = "Save results to file",defaultextension = 'txt', filetypes = (("txt files","*.txt"),("all files","*.*")))
    if window.filename != "":
        show_in_results("Saving output to file " + window.filename + '\n')
        f=open(window.filename, "w")
        f.write(results.get(1.0, END))
        f.close()

def clicked_exit():
    sys.exit(0)

def clicked_configure():
    for ip in get_my_hosts():
        process = threading.Thread(target=run_configure, args=[ ip ])
        process.start()

def run_configure(ip):
    sema.acquire()
    DevReq(1)
    global do_chk_compare
    changes = commands.get(1.0,END) + '\n'
    string=""
    string=string+"Result on host %s:\nSending:\n%s\n" % (ip,changes)
    dev = Device(host=ip, user=user.get(), passwd=passwd.get(), gather_facts=False)
    try:
        dev.open()
    except ConnectError as err:
        string=string+"Error: %s\n" % (err)
    else:
        with Config(dev, mode='exclusive') as cu:
            try:
                string=string+str(cu.load(changes, format='set'))
            except ConfigLoadError as err:
                string=string+"Error on loading config: %s\n" % (pprint.pformat(err))
            else:
                if do_chk_compare.get() == True:
                    old_stdout = sys.stdout
                    sys.stdout = mystdout = StringIO()
                    cu.pdiff()
                    sys.stdout = old_stdout
                    string=string+mystdout.getvalue()
                    string=string+"\ncommit : "
                try:
                    cu.commit( timeout=180, confirm=2, comment='Commit done using mja.py' )
                    string=string+"Commit issued\n"
                    show_in_results(string)
                    string=""
                except CommitError as err:
                    string=string+"Failed:\n %s" % (pprint.pformat(err))
                    show_in_results(string)
                    string=""
                else:
                    try:
                        string=string+("Confirming the commit\n")
                        show_in_results(string)
                        string=""
                        cu.commit_check()
                    except CommitError as err:
                        string=string+"Confirming the config failed. Device will rollback.\n"
                        string=string+"Reason:\n %s" % (pprint.pformat(err))
            string=string+"\n=============================================\n"
    show_in_results(string)
    string=""
    dev.close()
    DevReq(-1)
    sema.release()

def clicked_clear_results():
    results.config(state=NORMAL)
    results.delete('1.0', END)
    results.config(state=DISABLED)

def clicked_check():
    for ip in get_my_hosts():
        process = threading.Thread(target=run_check, args=[ ip ])
        process.start()


def run_check (ip):
    sema.acquire()
    DevReq(1)
    global chk_facts
    string="Testing %s: " % (ip)
    dev = Device(host=ip, user=user.get(), passwd=passwd.get(), gather_facts=do_facts.get())
    try:
        dev.open()
    except ConnectError as err:
        string=string+"Error: %s\n" % (err)
    else:
        string=string+"ok\n"
        if do_facts.get()==True:
            string=string+"%s\n=============================================\n" % (pprint.pformat(dev.facts))
    show_in_results(string)
    string=""
    dev.close()
    DevReq(-1)
    sema.release()

def show_in_results(text):
    results.config(state=NORMAL)
    results.yview( END )
    results.insert(END,text)
    results.config(state=DISABLED)

def get_my_hosts():
    global TotalHosts
    global DevQueue
    content = hosts.get(1.0, END)
    s=re.split('\s',content)
    for i in range(len(s)-1,-1,-1):
        if s[i]=='' or s[i][0:1]=="(":
            del s[i]
    for i in range (len(s)):
        if i>=len(s):
            break
        if is_valid_ip(s[i]):
            continue
        try:
            ip_address=socket.gethostbyname(str(s[i]))
        except:
            show_in_results("Invalid host entry: %s\n" % (s[i]))
            del s[i]
            continue
    TotalHosts=len(s)
    DevQueue=TotalHosts
    return s

def DevReq(i):
    global OutstandingReq
    global TotalHosts
    global DevQueue
    OutstandingReq += i
    if i<0:
        DevQueue+=i
    if OutstandingReq > 0:
        lbl_count.config (fg="red")
    else:
        lbl_count.config (fg="black")
    lbl_count.config(text="device requests pending/queue/total:  %d/%d/%d" % (OutstandingReq, DevQueue, TotalHosts))

OutstandingReq=int(0)
TotalHosts=int(0)
DevQueue=int(0)
sema=threading.Semaphore(value=MAX_THREADS)

window = Tk()

window.title("Multiple Junos Access             "+ "version " + VERSION)
window.geometry('695x600')
do_facts = BooleanVar()
do_chk_compare = BooleanVar()
do_facts.set(False)
do_chk_compare.set(False)

lbl_user = Label(window,   text="User:")
lbl_user.grid(column=0, row=0, sticky=("NW"))
user=Entry(window,width=10)
user.grid(column=1, row=0, sticky="NW")
lbl_passwd = Label(window, text="Passwd")
lbl_passwd.grid(column=2, row=0, sticky="NW")
passwd = Entry(window,width=10, show="*")
passwd.grid(column=3, row=0, sticky="NW")
user.insert(10,"mteppercd")
#passwd.insert(10,"root123")
lbl_count = Label(window, text="device requests pending/queue/total:  %d/%d/%d" % (0,0,0))
lbl_count.grid(column=4, row=0,columnspan=4,sticky="NE")

lbl_hosts = Label(window, text="Hosts:")
lbl_hosts.grid(column=0,row=1, sticky="NW")
btn_check = Button(window, text="Check connections", command=clicked_check)
btn_check.grid(column=1, row=1, sticky="NEW")
chk_facts = Checkbutton(window, text='include facts', var=do_facts)
chk_facts.grid(column=2, row=1, sticky="NEW")
btn_dns_lookup = Button(window, text="dns lookup", command=clicked_dns_lookup)
btn_dns_lookup.grid(column=3, row=1, sticky="NW")
btn_exit = Button(window, text="exit", command=clicked_exit)
btn_exit.grid(column=7, row=1, sticky="NE")

hosts = scrolledtext.ScrolledText(window,width=80,height=LINES_HOSTS)
hosts.grid(column=0,row=2,columnspan=8, sticky="NSEW")

lbl_commands = Label(window, text="Input:")
lbl_commands.grid(column=0,row=3, sticky="NW")
btn_run = Button(window, text="show", command=clicked_show)
btn_run.grid(column=1, row=3, sticky=W)
btn_configure = Button(window, text="configure", command=clicked_configure)
btn_configure.grid(column=2, row=3, sticky="NSEW")
chk_compare = Checkbutton(window, text='include show compare in output', var=do_chk_compare)
chk_compare.grid(column=3, row=3, sticky="NW")

commands = scrolledtext.ScrolledText(window,width=80,height=LINES_INPUT)
commands.grid(column=0,row=4,columnspan=8,sticky="NSEW")

lbl_results = Label(window, text="Results: ")
lbl_results.grid(column=0,row=5, sticky="NW")
btn_clear= Button(window, text="clear", command=clicked_clear_results)
btn_clear.grid(column=1, row=5, sticky="NSW")
btn_save = Button(window, text="save", command=clicked_save_results)
btn_save.grid(column=2, row=5, sticky="NSEW")

results = scrolledtext.ScrolledText(window,height=LINES_RESULTS)
results.grid(column=0,row=6,columnspan=8,sticky="NSEW")
results.config(state=DISABLED)

window.rowconfigure(2, weight=1)
window.rowconfigure(4, weight=2)
window.rowconfigure(6, weight=4)
window.columnconfigure(5, weight=1)

load_hosts()

window.mainloop()
