import sys
import os
# sys.path.insert(1, os.path.split(sys.path[0])[0])
sys.path.append('/home/fmasa/.local/lib/python3.8/site-packages')
import nfc

clf = nfc.ContactlessFrontend("usb")
print(clf)