questions = { "Verifying the EIGRP K values": {
        "answer":"show ip protocols",
        "notes": "..."
    },
    "Verifying network statements and EIGRP process ASN": {
        "answer":"show run | section router eigrp",
        "notes": "..."
    },
    "Verifying the EIGRP ASN":  {
        "answer":"show ip protocols",
        "notes": "..."
    },
    "Verifying EIGPR passive interfaces": {
        "answer":"show ip protocols",
        "notes": "..."
    },
    "Verifying enabled interfaces of EIGRP": {
        "answer":"show ip eigrp interfaces",
        "notes": "Output sections of enabled interfaces, number of peers of each interface, process-ID or named process and the local ASN."
    },
    "(Y/N): Passive interface for EIGRP turns off the sending and receiving of EIGRP packets on an interfaces?": {
        "answer":"Y",
        "notes": "This is true. The interface's network ID is injected into the EIGRP process. This gives an improvement of security and reduces EIGRP control traffic."
    },
    "(Y/N): To form an EIGRP neighbor adjacency, the router interfaces must be on the same subnet?": {
        "answer":"Y",
        "notes": "In case of an failure. Use 'spot-the-differnence' with commands like: 'show run interface GigabitEthernet0/1' or 'show ip interface GigabitEthernet0/1'."
    },    
    
}