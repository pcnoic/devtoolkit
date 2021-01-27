#!/usr/bin/env python3

import sys 
import base64

enc_msg = sys.argv[1]
base64_bytes = enc_msg.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')
print(message)
