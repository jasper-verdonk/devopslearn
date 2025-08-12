questions = { "Initialize the OSFP process 100": {
        "answer":"router ospf 100",
        "notes": "..."
    }, 
    "Under OSFP process 100 hierarchy, define RID 192.168.1.1": {
        "answer":"router-id 192.168.1.1",
        "notes": "This is at hierarchy R(config)# router ospf 100"
    }, 
    "Under OSFP process 100 hierarchy, enable OSFP on all interfaces with one statement for area 1234": {
        "answer":"network 0.0.0.0 255.255.255.255 area 1234",
        "notes": "This is at hierarchy R(config)#router ospf 100. Very specific has the format (i.e): 192.168.1.1 0.0.0.0 area 1234."
    }, 
    "Under OSFP process 100 hierarchy, enable OSFP on interface with IP 192.168.10.10 very specific for area 1234": {
        "answer":"network 192.168.10.10 0.0.0.0 area 1234",
        "notes": "Enable all interface for OSFP for area 1234: network 0.0.0.0 255.255.255.255 area 1234"
    }, 
    "Which command enables OSFP area 0 on the interface that is configured with the IPv4 address 172.16.10.1 and the subnet mask 255.255.255.252": {
        "answer":"network 172.16.10.0 0.0.0.3 area 0",
        "notes":"This is the correct network address and the wildcard."
        
    },
}    
    
