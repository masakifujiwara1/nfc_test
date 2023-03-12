#!/usr/bin/env python3
import nfc
import time
# import os
# import sys
# sys.path.insert(1, os.path.split(sys.path[0])[0])

while True:
  with nfc.ContactlessFrontend('usb') as m: #felicaリーダーusb扱い
    tag = m.connect(rdwr={'on-connect': lambda tag: False}) #felicaカード情報読み込み
    print(tag) #情報出力
    time.sleep(1) #インターバル