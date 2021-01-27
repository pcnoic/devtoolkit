#!/usr/bin/env python3

import sys 
import base64 

msg = sys.argv[1] 
msg_bytes = msg.encode('ascii') 
base64_bytes = base64.b64encode(msg_bytes) 
base64_msg = base64_bytes.decode('ascii') 
print(base64_msg) 

 
