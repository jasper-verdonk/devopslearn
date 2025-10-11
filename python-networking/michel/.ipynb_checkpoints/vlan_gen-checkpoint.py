# vlan_gen v1.0
# speed up configuring vlans on ELS switches

LINES_RESULTS=32

from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
import re
import socket



def clicked_save_results():
    window.filename =  filedialog.asksaveasfilename(initialdir = ".",title = "Save results to file",defaultextension = 'txt', filetypes = (("txt files","*.txt"),("all files","*.*")))
    if window.filename != "":
        show_in_results("Saving output to file " + window.filename + '\n')
        f=open(window.filename, "w")
        f.write(results.get(1.0, END))
        f.close()

def clicked_exit():
    sys.exit(0)

def is_int(int):
    if re.search("[a-z]{1,2}-[0-9]{1,2}.*",int) == None:
        return False
    return True

def clicked_go():
    global do_ints
    if start_int.get().strip() == "":
        messagebox.showinfo("Error", "Please enter start interface")
        start_int.focus_set()
        return()

    if end_int.get().strip() == "":
        messagebox.showinfo("Error", "Please enter end interface")
        end_int.focus_set()
        return()

    if vlan.get().strip() == "":
        messagebox.showinfo("Error", "Please enter a vlan name")
        vlan.focus_set()
        return()

    if is_int(start_int.get().strip()) == False:
        messagebox.showinfo("Error", "Please enter a valid start interface")
        start_int.focus_set()
        return()

    if is_int(end_int.get().strip()) == False:
        messagebox.showinfo("Error", "Please enter a valid end interface")
        end_int.focus_set()
        return()

    if do_vlan.get() == True:
        if vlan_id.get().strip()=="":
            messagebox.showinfo("Error", "Please enter a vlan-id when checking vlan")
            vlan_id.focus_set()
            return()
        if int(vlan_id.get()) < 1 or int(vlan_id.get()) > 4096:
            messagebox.showinfo("Error", "Please enter a valid vlan-id ....")
            vlan_id.focus_set()
            return()
        if (vlan_ip.get().strip() != ""):
            s=re.split("/",vlan_ip.get().strip())
            if int(s[1]) <0 or int(s[1]) > 32:
                messagebox.showinfo("Error", "Please enter a valid IP address or leave the address fiels empty.\n")
                return()
            try:
                socket.inet_aton(s[0])
                show_results("set vlans %s l3-interface irb.%s\n" % (vlan.get().strip(), vlan_id.get().strip() ))
                show_results("set interfaces irb unit %s family inet address %s\n" % (vlan_id.get().strip(), vlan_ip.get().strip() ))
            except OSError:
                messagebox.showinfo("Error", "Please enter a valid IP address or leave the address fiels empty.\n")
                return()
        show_results ("set vlans %s vlan-id %s\n" % (vlan.get().strip(), vlan_id.get().strip() ))
    start=re.split("/", start_int.get().strip())
    end=re.split("/", end_int.get().strip())

    if do_ints.get() == True:
        for i in range (int(start[2]),int(end[2])+1):
            show_results("set interfaces %s/%s/%d unit 0 family ethernet-switching vlan members %s\n" % (start[0],start[1],i,vlan.get()))
    else:
        show_results("set interfaces interface-range %s unit 0 family ethernet-switching vlan member %s\n" % (range_name.get().strip(), vlan.get().strip()))
        for i in range (int(start[2]),int(end[2])+1):
            show_results("set interfaces interface-range %s member %s/%s/%d\n" % (range_name.get().strip(), start[0],start[1],i))

def clicked_int():
    global do_range
    global do_ints
    gen_range.toggle()
    if do_ints.get() == True:
        range_name.config(state=DISABLED)
    else:
        range_name.config(state=NORMAL)

def clicked_vlan():
    if do_vlan.get() == True:
        vlan_id.config(state=NORMAL)
        vlan_ip.config(state=NORMAL)
    else:
        vlan_id.config(state=DISABLED)
        vlan_ip.config(state=DISABLED)


def clicked_range():
    global do_range
    global do_ints
    gen_ints.toggle()
    if do_range.get() == True:
        range_name.config(state=NORMAL)
    else:
        range_name.config(state=DISABLED)

def clicked_clear_results():
    results.config(state=NORMAL)
    results.delete('1.0', END)
    results.config(state=DISABLED)


def show_results(text):
    results.config(state=NORMAL)
    results.yview( END )
    results.insert(END,text)
    results.config(state=DISABLED)

window = Tk()
window.title("Generate interface/vlan config")
window.geometry('665x600')

do_range=BooleanVar()
do_ints=BooleanVar()
do_vlan=BooleanVar()
#do_range=False
#do_ints=True
lbl_vlan = Label(window,   text="Vlan:")
lbl_vlan.grid(column=0, row=0, sticky=W)
vlan=Entry(window,width=15)
vlan.grid(column=1, row=0, sticky=W)
gen_ints = Checkbutton(window, text='Interfaces', command=clicked_int, variable=do_ints)
gen_ints.grid(column=2, row=0, sticky=W)
gen_ints.select()
gen_range = Checkbutton(window, text='Range', command=clicked_range, variable=do_range)
gen_range.grid(column=3, row=0, sticky=W)
lbl_range_name = Label(window,   text="Range name")
lbl_range_name.grid(column=4, row=0, sticky=W)
range_name=Entry(window,width=15)
range_name.grid(column=5, row=0, sticky=W)
btn_exit = Button(window, text="exit", command=clicked_exit)
btn_exit.grid(column=7, row=0, sticky=E)

lbl_start_int = Label(window, text="start int")
lbl_start_int.grid(column=0,row=1, sticky=W)
start_int = Entry(window, width=10)
start_int.grid(column=1, row=1, sticky=W)
lbl_end_int = Label(window, text="end int")
lbl_end_int.grid(column=2,row=1, sticky=W)
end_int = Entry(window, width=10)
end_int.grid(column=3, row=1, sticky=W)
go=Button(window, text="go", command=clicked_go)
go.grid(column=4, row=1, sticky=W)


gen_vlan = Checkbutton(window, text='include vlan',  variable=do_vlan, command=clicked_vlan)
gen_vlan.grid(column=0, row=2, sticky=W)
lbl_id = Label(window, text="id")
lbl_id.grid(column=1, row=2, sticky=W)
vlan_id = Entry(window, width=4)
vlan_id.grid(column=2, row=2, sticky=W)
lbl_vlan_ip = Label(window, text="IP")
lbl_vlan_ip.grid(column=3, row=2, sticky=W)
vlan_ip = Entry(window, width=16)
vlan_ip.grid(column=4, row=2, sticky=W)


lbl_results = Label(window, text="Results:")
lbl_results.grid(column=0,row=3, sticky="NSEW")
btn_clear= Button(window, text="clear", command=clicked_clear_results)
btn_clear.grid(column=1, row=3, sticky="NSW")
btn_save = Button(window, text="save", command=clicked_save_results)
btn_save.grid(column=2, row=3, sticky="NSW")

results = scrolledtext.ScrolledText(window,width=80,height=LINES_RESULTS)
results.grid(column=0,row=4,columnspan=8,sticky="NSEW")
results.config(state=DISABLED)
range_name.config(state=DISABLED)
vlan_id.config(state=DISABLED)
vlan_ip.config(state=DISABLED)

window.rowconfigure(4, weight=1)
window.columnconfigure(5, weight=1)

window.mainloop()
