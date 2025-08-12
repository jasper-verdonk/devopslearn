questions = {
    "What does BGP stand for?": {
        "answer": "Border Gateway Protocol", 
        "notes": "BGP is a Path vector routing protocol."
         },
    "What is the default administrative distance for eBGP?": {
        "answer": "20", 
        "notes": "The default administrative distance for iBGP is 200."
         },
    "What is the TCP port of BGP?": {
        "answer": "179", 
        "notes": "This is the default BGP port."
         },
    "Which BGP attribute class must be recogonized by all BGP implementations and advertised to other autonomous systems?": {
        "answer": "Well-known mandatory", 
        "notes": "The other BGP attribute classes are: Well-know discretionary, Optional Transitive, Optional Non-transitive."
         }, 
    "How are the BGP Path Attributes (PAs) classified?": {
        "answer": "Well-known mandatory, Well-known discretionary, Optional transitive, Optional non-transitive", 
        "notes": "..."
         }, 
    "Well-known mandatory PAs must be included with every prefix advertisement (Y/N)": {
        "answer": "Y", 
        "notes":"Examples of well-know mandatory attributes: AS-path and Origin." 
         },
    "Well-known discretionary PAs must be included with the prefix advertisement (Y/N)": {
        "answer": "N", 
        "notes":"An example: Local-Preference" },
    "The IPv6 address family must be initialized to establish a BGP session with a peer using IPv6 addressing (Y/N)": {
        "answer": "Y", 
        "notes": "The IPv6 address family does not exits by default on IOS-based devices"
         },
    "What is the default value of the local-preference BGP attribute?": {
        "answer":"100",
        "notes": "Local Preference can be set for specific routes by using a route-map or for all routes received from a specific neighbor."
    },    
    
}