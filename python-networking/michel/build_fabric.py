# Copyright (c) 2019 TNND
# version beta 0,01 only underlay so far
# Python script to generate IP fabric  (leave & spine) config
# With ospf routing for the underlay
# Script takes a config file as first argument
# Second argument can be outout directory where config files for all spine en leaves are written to
# If Second argument is ommited current working directory will be used outputfile

# Config file can contain:
# section  general
# In this section you specify setting every router (Spine and Leaves get)
# As well as some global paramaters.
#
# organisation    : The name of the organisation to display in login message
# hostname-prefix : A hostname gets this and then spines S1..XX Leaves L1..Y
# p2p-range       : Network rang to set point-to-point in. from x.x.0.1 to x.x.4.254
#                 : with /30 ranges
# loopback-range  : Class C range for /32 IP's on loop loopback
#                   Spines go first first spine gets 1 etc. First leave gets 1+max-Spines
# nameserver      : Dns server, multiple allowed. Optional.
# ntpserver       : ntp server name or address, multiple allowed. Optional
# snmp-community  : Community getting read-only permision. Optional
# snmp-trap-server: Trapserver, optional
# syslog          : specify <IP> <facility> <level>
# leaves          : Number of leave switches in the fabric
# spines          : Number of present spine switches in the fabric
# max-spines      : Number of maximum spines the fabric can grow to
#                   max-spines must be greater or equal to number of Spines
#                   max-spine is used as offset in IP address calculation
#                   should typically be four or six
# max-Leaves      : Maximum number of leaves to support within ip numbering schema
#                 : In principle an ip-fabric always can scale more, but then the IP numbering gets disorganized.
#                 : A practical limit is also the number of interfaces on the spines ....
# spine-start-int : First interface to use on spine for leave connection
# leave-start-int : Guess
# mtu			  : mtu size on Spine-leave connections
#
# set             : all lines in inputfile beginning wit "set" will be copied to all configfiles
# vlan			  : Start of vlan argumen vlannumber, vlane-anme. if van is ommiteted is will be vlan{number}
# member       	  : Include an interface in a vlans
#					Arguments router (typically l1.. L{leaves}, but spines are allowed)<access|trunk>
#					Use pair <router> <interface> to define a redundant connection, sharing an esi
# Vlan-ip		  : L3 to configure for vlan

import sys
import re
import os

if len(sys.argv) != 3 and  len(sys.argv) != 2:
	print ("Usage: ", sys.argv[0], "<inputfile> [output directory]" )
	exit(1)

inputfile=open(sys.argv[1])

if (len(sys.argv) == 3):
	os.chdir(sys.argv[2])

def general_settings( outputfile ):
	global nameservers
	global ntpservers
	global snmpcommunity
	global syslogservers
	global organisation
	global hostname
	for str in nameservers:
		buf="set system name-server " + str + '\n'
		outputfile.write(buf)
	for str in ntpservers:
		buf="set system ntp server %s" % (str) + '\n'
		outputfile.write(buf)
	for str in syslogservers:
		buf="set system syslog host " + str + '\n'
		outputfile.write(buf)
	if snmpcommunity != "":
		buf="set snmp community %s authorization read-only\n" % (snmpcommunity)
		outputfile.write(buf)
	if snmptrapserver != "":
		buf="set snmp trap-group group1 targets %s\n" % (snmptrapserver)
		outputfile.write(buf)
	buf="set firewall family inet filter ECMP term final then load-balance per-packet\n"
	outputfile.write(buf)
	buf="set routing-options forwarding-table export ECMP\n"
	outputfile.write(buf)
	outputfile.write("set routing-options autonomous-system 64512\n")
	outputfile.write("set system services ssh protocol-version v2\n")
	outputfile.write("set system services ssh ciphers aes256-ctr\n")
	outputfile.write("set system services ssh ciphers \"aes256-gcm@openssh.com\"\n")
	outputfile.write("set system services ssh ciphers \"chacha20-poly1305@openssh.com\"\n")
	outputfile.write("set system services ssh macs hmac-sha2-256\n")
	outputfile.write("set system services ssh macs \"hmac-sha2-256-etm@openssh.com\"\n")
	outputfile.write("set system services ssh macs hmac-sha2-512 \n")
	outputfile.write("set system services ssh macs \"hmac-sha2-512-etm@openssh.com\"\n")
	outputfile.write("set system services ssh key-exchange curve25519-sha256\n")
	outputfile.write("set system services ssh key-exchange ecdh-sha2-nistp256\n")
	outputfile.write("set system services ssh key-exchange ecdh-sha2-nistp384\n")
	outputfile.write("set system services ssh key-exchange ecdh-sha2-nistp521\n")
	outputfile.write("set system services ssh key-exchange group-exchange-sha2\n")
	outputfile.write("set system services ssh connection-limit 5\n")
	outputfile.write("set system services ssh rate-limit 3\n")
	outputfile.write("set system login message \"\\n* [WARNING]" + hostname + ": Unauthorized access prohibited. *\\n")
	outputfile.write("* This system is owned by " + organisation + "If you are not *\\n")
	outputfile.write("* authorized to access this system, exit immediately. *\\n")
	outputfile.write("* Unauthorized access to this system is forbidden by *\\n")
	outputfile.write("* company policies, national, and international laws. *\\n")
	outputfile.write("* Unauthorized users are subject to criminal and civil *\\n")
	outputfile.write("* penalties as well as company initiated disciplinary *\\n")
	outputfile.write("* proceedings. *\\n*\\n");
	outputfile.write("* By entry into this system you acknowledge that you *\\n")
	outputfile.write("* are authorized access and the level of privilege you *\\n")
	outputfile.write("* subsequently execute on this system. You further *\\n")
	outputfile.write("* acknowledge that by entry into this system you *\\n")
	outputfile.write("* expect no privacy from monitoring. *\\n\\n\"\n");
	outputfile.write("set system login retry-options tries-before-disconnect 3\n")
	outputfile.write("set system login retry-options backoff-threshold 3\n")
	outputfile.write("set system login retry-options backoff-factor 6\n")
	outputfile.write("set system login retry-options minimum-time 30\n")
	outputfile.write("set system login retry-options maximum-time 30\n")

organisation=""
hostname_prefix=""
oobrange=""
mtu=""
nameservers=[ "" ]
nameservers.clear()
ntpservers=[ "" ]
ntpservers.clear()
syslogservers=[ "" ]
syslogservers.clear()
copy_set=[ "" ]
copy_set.clear()

for line in inputfile:
	if re.search("^#.*$", line.strip()):
		continue
	if line == "":
		continue
	s=re.split("\s", line.strip())
	for i in range(len(s)-1,0,-1):
		if s[i] == '':
			del(s[i])
	if s[0].lower() == "hostname-prefix":
		hostname_prefix=s[1]
	if s[0].lower() == "nameserver":
		nameservers.append(s[1])
	if s[0].lower() == "ntp-server":
		ntpservers.append(s[1])
	if s[0].lower() == "p2p-range":
		p2prange=s[1]
	if s[0].lower() == "loopback-range":
		loopbackrange=s[1]
	if s[0].lower() == "oob-range":
		oobrange=s[1]
	if s[0].lower() == "snmp-community":
		snmpcommunity=s[1]
	if s[0].lower() == "snmp-trap-server":
		snmptrapserver=s[1]
	if s[0].lower() == "spines":
		spines=int(s[1])
	if s[0].lower() == "leaves":
		leaves=int(s[1])
	if s[0].lower() == "max-spines":
		maxspines=int(s[1])
	if s[0].lower() == "max-leaves":
		maxleaves=int(s[1])
	if s[0].lower() == "spine-start-int":
		spinestartint=s[1]
	if s[0].lower() == "leave-start-int":
		leavestartint=s[1]
	if s[0].lower() == "syslog":
		if len(s) != 4:
			print ("Wrong number of arguments for syslog server " + s[1])
			continue
		syslogservers.append("%s %s %s" % (s[1], s[2], s[3]))
	if s[0].lower() == "organisation":
		for i in range (1,len(s)):
			organisation=organisation + s[i] + " "
	if s[0].lower() == "mtu":
		mtu=s[1]
	if s[0].lower() == "set":
		temp_line=""
		for i in range (len(s)):
			temp_line=temp_line + s[i] + " "
		temp_line = temp_line + '\n'
		copy_set.append(temp_line)

# /* done with scanning inputfile */
# /* done a seek to "rewind" the input file to the first line */
inputfile.seek(0,0)

spine_int_split=re.split("/", spinestartint)
spine_int_prefix=""
for i in range (len(spine_int_split)-1):
	spine_int_prefix=spine_int_prefix + spine_int_split[i] + "/"
spine_int_number=int(spine_int_split[i+1])

leave_int_split=re.split("/", leavestartint)
leave_int_prefix=""
for i in range (len(leave_int_split)-1):
	leave_int_prefix=leave_int_prefix + leave_int_split[i] + "/"
leave_int_number=int(leave_int_split[i+1])


# Start handling Spine underlay config
for filenumber in range (1,spines+1):
	outputfile=hostname_prefix+"S"+str(filenumber)+".conf"
	f=open(outputfile, "wt")
	hostname=" %sS%d" % (hostname_prefix, filenumber)
	general_settings(f)
	buf="set interfaces lo0 unit 0 family inet address %s.%d/32\n" % (loopbackrange,filenumber)
	f.write(buf)
	if oobrange != "":
		buf="set interfaces me0 unit 0 family inet address %s.%d/24\n" % (oobrange,filenumber)
	else:
		buf="set chassis alarm management-ethernet link-down ignore\n"
	f.write(buf)
	buf="set routing-options router-id %s.%d\n" % (loopbackrange,filenumber)
	f.write(buf)
	buf="set protocols ospf area 0 interface lo0.0 passive\n"
	f.write(buf)
	buf="set system host-name %s\n" % (hostname)
	f.write(buf)
	f.write("set routing-options resolution rib bgp.rtarget.0 resolution-rib inet.0\n")
	for leave_number in range (0,leaves):
		byte3=(1 + (leave_number *4) + (maxleaves*maxspines*4*(filenumber-1)) ) // 256
		byte4=(1 + (leave_number *4) + (maxleaves*maxspines*4*(filenumber-1)) ) % 256
		spine_int="%s%d" % (spine_int_prefix,spine_int_number + leave_number)
		buf="set interfaces %s unit 0 family inet address %s.%d.%d/30\n" % (spine_int,p2prange,byte3,byte4)
		f.write(buf)
		buf="set protocols ospf area 0 interface %s.0 interface-type p2p bfd-liveness-detection minimum-interval 300 multiplier 3\n" % (spine_int)
		f.write(buf)
		buf="set interfaces %s description \"link to  %sL%d int %s%d\"\n" % (spine_int, hostname_prefix, leave_number+1, leave_int_prefix,filenumber-1)
		f.write(buf)
		buf="set interfaces %s mtu %s\n" % (spine_int, mtu)
		f.write(buf)
	for buf in copy_set:
		f.write(buf)
	f.close()
# Done with spine underlay

# Start handling Leave underlay
for leave_number in range (0,leaves):
	outputfile=hostname_prefix+"L"+str(leave_number+1)+".conf"
	f=open(outputfile, "wt")
	hostname="%sL%d" % (hostname_prefix, leave_number+1)
	buf="set interfaces lo0 unit 0 family inet address %s.%d/32\n" % (loopbackrange,leave_number+maxspines+1)
	f.write(buf)
	if oobrange != "":
		buf="set interfaces me0 unit 0 family inet address %s.%d/24\n" % (oobrange,leave_number+maxspines+1)
	else:
		buf="set chassis alarm management-ethernet link-down ignore\n"
	f.write(buf)
	buf="set routing-options router-id %s.%d\n" % (loopbackrange,leave_number+maxspines+1)
	f.write(buf)
	buf="set protocols ospf area 0 interface lo0.0 passive\n"
	f.write(buf)
	buf="set system host-name %s\n" % (hostname)
	f.write(buf)

	for spine_number in range (0,spines):
		byte3=(2 + ((leave_number) *4) + (maxleaves*maxspines*4*spine_number) ) // 256
		byte4=(2 + ((leave_number) *4) + (maxleaves*maxspines*4*spine_number) ) % 256
		leave_int="%s%d" % (leave_int_prefix,spine_number + leave_int_number)
		buf="set interfaces %s unit 0 family inet address %s.%d.%d/30\n" % (leave_int,p2prange,byte3,byte4)
		f.write(buf)
		buf="set protocols ospf area 0 interface %s.0 interface-type p2p bfd-liveness-detection minimum-interval 300 multiplier 3\n" % (leave_int)
		f.write(buf)
		buf="set interfaces %s description \"link to spine %sS%d int %s%d\"\n" % (leave_int, hostname_prefix, spine_number+1, spine_int_prefix,leave_number)
		f.write(buf)
		buf="set interfaces %s mtu %s\n" % (leave_int, mtu)
		f.write(buf)
	for buf in copy_set:
		f.write(buf)
	f.close()
#done with leave underlay

#overlay spines
for spine_number in range (1,spines+1):
	outputfile=hostname_prefix+"S"+str(spine_number)+".conf"
	f=open(outputfile, "at")
	f.write("set forwarding-options vxlan-routing  next-hop 16384\n")
	f.write("set forwarding-options vxlan-routing  interface-num 8192\n")
	f.write("set forwarding-options vxlan-routing  overlay-ecmp\n")
	f.write("set protocols bgp group overlay type internal\n")
	f.write("set protocols bgp group overlay family evpn signaling\n")
	f.write("set protocols bgp group overlay multipath\n")
	f.write("set protocols bgp group overlay cluster %s.%d\n" % (loopbackrange, spine_number))
	f.write("set protocols bgp group overlay local-address %s.%d\n" % (loopbackrange, spine_number))
	f.write("set routing-options forwarding-table chained-composite-next-hop ingress evpn\n")

#	/* Spines are Route Refelectors: must peer with other spines */
	for i in range (1,spines +1):
		if ( i != spine_number):
			f.write("set protocols bgp group overlay neighbor %s.%d\n" % (loopbackrange, i))
#	/* Every spine must peer with every leave */
	for leave_number in range (maxspines+1, leaves+maxspines+1):
		f.write("set protocols bgp group overlay neighbor %s.%d\n" % (loopbackrange, leave_number))
	f.write("set protocols evpn extended-vni-list all\n")
	f.write("set protocols evpn encapsulation vxlan\n")
	f.write("set protocols evpn multicast-mode ingress-replication\n")
	f.write("set switch-options vtp-source-interface lo0.0\n")
	f.write("set switch-options route-distinguisher %s.%d:1\n" % (loopbackrange, spine_number))
	f.write("set switch-options vrf-target auto\n")
	f.close()

#overlay Leaves
for leave_number in range (1, leaves +1):
	outputfile=hostname_prefix+"L"+str(leave_number)+".conf"
	f=open(outputfile, "at")
	f.write("set forwarding-options vxlan-routing  next-hop 16384\n")
	f.write("set forwarding-options vxlan-routing  interface-num 8192\n")
	f.write("set forwarding-options vxlan-routing  overlay-ecmp\n")
	f.write("set protocols bgp group overlay type internal\n")
	f.write("set protocols bgp group overlay family evpn signaling\n")
	f.write("set protocols bgp group overlay multipath\n")
	f.write("set protocols bgp group overlay local-address %s.%d\n" % (loopbackrange, leave_number + maxspines))
	f.write("set routing-options forwarding-table chained-composite-next-hop ingress evpn\n")
	f.write("set protocols evpn default-gateway no-gateway-community\n")
	for spine_number in range (1, spines+1):
		f.write("set protocols bgp group overlay neighbor %s.%d\n" % (loopbackrange, spine_number))
	f.write("set protocols evpn extended-vni-list all\n")
	f.write("set protocols evpn encapsulation vxlan\n")
	f.write("set protocols evpn multicast-mode ingress-replication\n")
	f.write("set switch-options vtp-source-interface lo0.0\n")
	f.write("set switch-options route-distinguisher %s.%d:1\n" % (loopbackrange, leave_number + maxspines))
	f.write("set switch-options vrf-target auto\n")
	f.close()

# Scanning input file again for vlans
vlan=""
vlan_created=[ "" ]
vlan_created.clear()
ae_count_leaves=[ 0 ]
ae_count_spines=[ 0 ]
ae_tracking=[ "" ]
did_mtu=[ "" ]

for i in range (leaves+1):
	ae_count_leaves.append(0)
	ae_count_spines.append(0)

def search_ae(router,interface):
	global ae_tracking
	print (ae_tracking)
	to=len(ae_tracking)
	print("to is %d" % (to))
	for i in range (1, to):
		print ("i : %d" % (i))
		print ("looking for %s%sae[0-9]* in %s" % (router, interface, ae_tracking[i]))
		if re.search("%s%sae[0-9]*" % (router, interface), ae_tracking[i]):
			string=re.search("^.*ae[0-9]+",ae_tracking[i]).group()
			print ("String : %s" % (string))
			return string
		return ("")

def lowest(a,b):
	if a<b: return a
	else: return b

for line in inputfile:
	if re.search("^#.*$", line.strip()):
		continue
	if line == "":
		continue
	s=re.split("\s", line.strip())
	for i in range(len(s)-1,0,-1):
		if s[i] == '':
			del(s[i])
# Start handling "vlan" in inputfile
	if (s[0].lower() == "vlan"):
		vlan_id=int(s[1])
		if ( (vlan_id <1) or (vlan_id >4094)):
			print("Vlan error: id should be between 1 and 4094, found %d\n" % (vlan_id))
			exit(1)
		if len(s) == 3:
			vlan_name=s[2]
		else:
			vlan_name="vlan%d" % (vlan_id)
		vlan_created.clear()
		continue
#start handling vlan-ip in input file
	if s[0].lower() == "vlan-ip":
		if vlan_name == "":
			print("vlan-ip found without vlan: ignoring")
			continue
		for spine_number in range (1,spines+1):
			outputfile=hostname_prefix+"S"+str(spine_number)+".conf"
			f=open(outputfile, "at")
			f.write("set vlans %s l3-interface irb.%d\n" % (vlan_name, vlan_id))
			f.write("set vlans %s vlan-id %d\n" % (vlan_name, vlan_id))
			f.write("set interfaces irb.%d family inet address %s\n" % (vlan_id, s[1]))
			f.write("set vlans %s vxlan vni %d\n" % (vlan_name, vlan_id))
			f.close()
			if vlan_created.count("s%d" % spine_number) == 0:
				vlan_created.append("s%d" % (spine_number))
# Start handling member in input file
	if s[0].lower() == "member":
		if vlan_name == "":
			print ("Found member without vlan first. This can't be good!")
			exit(1)
		if re.match("[sl][0-9]+", s[1].lower()) == None:
			print("Wrong router %s in vlan %d * * ignoring this line * *\n" % (s[1], vlan_id))
			continue
		member_router_sl=s[1][0:1].lower()
		member_router_number=int(s[1][1:])
		if member_router_sl == "s" and member_router_number > spines:
			print ("ingnoring line %s: ** spine number greather then configured number of spines **" % (line))
			continue
		if member_router_sl == "l" and member_router_number > leaves:
			print ("ingnoring line %s: ** leave number greather then configured number of leaves **" % (line))
			continue
		outputfile=hostname_prefix+member_router_sl.upper()+str(member_router_number)+".conf"
		f=open(outputfile, "at")
		if vlan_created.count("%s%d" % (member_router_sl, member_router_number)) == 0:
			f.write("set vlans %s vlan-id %d\n" % (vlan_name, vlan_id))
			f.write("set vlans %s vxlan vni %d\n" % (vlan_name, vlan_id))
			vlan_created.append("%s%d" % (member_router_sl, member_router_number))
		vlan_mode="empty"
		if s[3].lower() == "access": vlan_mode="access"
		if s[3].lower() == "trunk":	vlan_mode="trunk"
		if vlan_mode=="empty":
			print ("Unknown interface-mode " + s[3])
			f.close()
			continue
		if len(s) >=5 and s[4] == "pair":
			pair_router_sl=s[5][0:1].lower()
			pair_router_number=int(s[5][1:])
			if re.match("[sl][0-9]+", s[5].lower()) == None:
				print("Wrong pair router %s in vlan %d * * ignoring this line * *\n" % (s[1], vlan_id))
				continue
			if pair_router_sl == "s" and pair_router_number > spines:
				print ("ingnoring line %s: ** pair-spine number greather then configured number of spines **" % (line))
				continue
			if pair_router_sl == "l" and pair_router_number > leaves:
				print ("ingnoring line %s: ** pair-leave number greather then configured number of leaves **" % (line))
				continue
			print ("s[2] : %s s6: %s" % (s[2], s[6]))
			ae_int=search_ae(member_router_sl+str(member_router_number),s[2])
			pair_ae_int=search_ae(pair_router_sl+str(pair_router_number),s[6])
			print ("Gevonden ae int   : " + str(ae_int))
			print ("Gevonden pair ae int: " + str(pair_ae_int))
			outputfile=hostname_prefix+pair_router_sl.upper()+str(pair_router_number)+".conf"
			f2=open(outputfile, "at")
			if ae_int=="":
				if member_router_sl == "s":
					ae=ae_count_spines[member_router_number]
					ae_count_spines[member_router_number]+=1
				if member_router_sl == "l":
					ae=ae_count_leaves[member_router_number]
					ae_count_leaves[member_router_number]+=1
				ae_tracking.append("%s%sae%d" % (member_router_sl+str(member_router_number),s[2],ae))
			else:
				ae=int(ae_int[2:])
#			print( ">>>>  ae_int=%s,  ae = %d" % (ae_int, ae))
			f.write("set interfaces ae%d unit 0 family ethernet-switching interface-mode %s vlan members %s\n"% (ae, s[3], vlan_name))
			f.write("set interfaces %s ether-options 802.3ad ae%d\n" % (s[2], ae))
			if did_mtu.count("%s%dae%d" % (member_router_sl, member_router_number, ae)) == 0:
				f.write("set interfaces ae%d mtu %s\n" % (ae, mtu))
				f.write("set esi ok\n")
				f.write("set system id\n")
				did_mtu.append("%s%dae%d" % (member_router_sl, member_router_number, ae))
#				print (did_mtu)
			remember_ae=ae
			if pair_ae_int=="":
				if pair_router_sl == "s":
					ae=ae_count_spines[pair_router_number]
					ae_count_spines[pair_router_sl_router_number]+=1
				if pair_router_sl == "l":
					ae=ae_count_leaves[pair_router_number]
					ae_count_leaves[pair_router_number]+=1
				ae_tracking.append("%s%sae%d" % (pair_router_sl+str(pair_router_number),s[6],ae))
			else:
				ae=int(pair_ae_int[2:])
	#		print(" >>>>  pair ae:  %d" % (ae))
			f2.write("set interfaces ae%d unit 0 family ethernet-switching interface-mode %s vlan members %s\n"% (ae, s[3], vlan_name))
			f2.write("set interfaces %s ether-options 802.3ad ae%d\n" % (s[6], ae))
			f.write("set interfaces %s description member of ae%d, paired with %s%s%d %s\n" % (s[2], ae, hostname_prefix, pair_router_sl, pair_router_number, s[6]))
			if did_mtu.count("%s%dae%d" % (pair_router_sl, pair_router_number, ae)) == 0:
				f2.write("set interfaces ae%d mtu %s\n" % (ae, mtu))
				f2.write("set esi ok\n")
				f2.write("set system id\n")
				did_mtu.append("%s%dae%d" % (member_router_sl, member_router_number, ae))
			f2.close()
		else:	# single interface
#		print(ae_tracking)
			f.write("set interfaces %s unit 0 family ethernet-switching interface-mode %s vlan member %s\n" % (s[2], s[3], vlan_name))
			if did_mtu.count("%s%d%s" % (member_router_sl, member_router_number,s[2])) == 0:
				f.write("set interfaces %s mtu %s\n" % (s[2], mtu))
				did_mtu.append("%s%d%s" % (member_router_sl, member_router_number,s[2]))
			f.close()
print (ae_count_leaves)
