import sys
import re
if len(sys.argv) != 3:
    print ("Usage: %s <loopbackIP> <interface number>" % (sys.argv[0]))
    exit(1)
bytes=re.split("\.",sys.argv[1])
print("ESI becomes 01:01:01:%02x:%02x:%02x:%02x:%02x:01:01" % (int(bytes[0]), int(bytes[1]), int(bytes[2]), int(bytes[3]), int(sys.argv[2])))
