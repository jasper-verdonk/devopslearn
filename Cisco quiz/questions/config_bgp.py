questions = {
    "Initialize the BGP process for ASN 65000": {
        "answer": "router bgp 65000",
        "notes": "..."
    },    
    "Under BGP process ASN 65000 hierarchy, define EBGP neighbor 10.12.1.2 ASN 65100": {
        "answer": "neighbor 10.12.1.2 remote-as 65100",
        "notes": "..."
    }, 
    "Under BGP process ASN 65000 hierarchy, define EBGP neighbor 10.12.1.2 MD5 authentication 'CISCOBGP'": {
        "answer": "neighbor 10.12.1.2 password CISCOBGP",
        "notes": "..."
    }, 
    "Cange the local-preference value from 100 to 150 for all routes received from a specific neighbor": {
        "answer":"bgp default local-preference 150",
        "notes": "..."
    },
    "": {
        "answer":"",
        "notes": "..."
    },
}