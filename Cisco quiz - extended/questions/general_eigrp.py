questions = { "What does EIGRP stand for?": {
        "answer":"Enhanced Interior Gateway Routing Protocol",
        "notes": "..."
    },
    "Which algorithm does EIGRP use?": {
        "answer":"DUAL",
        "notes": "Diffusing Update Algorithm."
    },
    "What is the EIGRP metric based on by default?": {
        "answer":"Bandwidth and delay",
        "notes": "All the EIGRP metrics are: Bandwidth, delay, load, reliablility. "
    },
    "Which EIGRP K values are set to 1 by default (e.g: K1 = 0, K4=0)": {
        "answer":"K1, K3",
        "notes": "K1 = 1, K2 = 0, K3 = 1, K4 = 0, K5 = 0. The value TOS = 0 and cannot be changed. K6 is used for named mode configurations."
    },
    "Which command displays the K values?": {
        "answer":"show ip protocols",
        "notes": "..."
    },
    "What is the IP protocol number of EIGRP? Is it 88 or 89?": {
        "answer":"88",
        "notes": "The EIGRP IP Protocol number is: 88 (no TCP or UDP header)"
    },
    "How many packet types does EIGRP use for inter-router communication?": {
        "answer":"5",
        "notes": "Hello, Request, Update, Query and reply. EIGRP uses RTP (Reliable Transport Protocol)."
    },
    "What is the default EIGRP administative distance (non-redistributed or summary)?": {
        "answer":"90",
        "notes": "Routes that are being redistributed into EIGRP have an administrative distance of 170."
    },
    "What is the administrative distance of an EIGRP summary route": {
        "answer":"5",
        "notes": "Redistributed EIGRP routes have an administrative distance 170. Non-redistributed EIGRP routes have an administrative distance 90."
    },
    "(Y/N) The Autonomous system number (ASN) must match for neighborship formation": {
        "answer":"Y",
        "notes": "Forming a neighborship with a peer the following must match: Metric K values, primary subnet matches, ASN matches and authentication parameters."
    },
    "How do we call a route with the lowest path metric to reach a destination?": {
        "answer":"Successor route",
        "notes": "The route with the lowest path metric to reach a destination."
    },
    "How do we call the first-hop router for the successor route?": {
        "answer":"Successor",
        "notes": "This is applicable to the successor route."
    },
    "How do we call the metric value for the lowest-metric path to reach a destination": {
        "answer":"Feasible distance",
        "notes": "The metric value for the lowest-metric path. The FD is calculated locally. It uses the RD as an input vector."
    },
    "How do we call the distance reported by a router to reach a prefix?": {
        "answer":"Reported distance",
        "notes": "The reported distance value is the feasible distance calculated by the advertising router."
    },
    "How do we call the condition for a route to be conciderate a backup route?": {
        "answer":"Feasible condition",
        "notes": "The RD must be less then the FD."
    },
        
}