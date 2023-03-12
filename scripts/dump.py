import nfc
import time

def connected(tag):
  # 内容を16進数で出力する
  print("dump felica.")
  print('  ' + '\n  '.join(tag.dump()))

while True:
  with nfc.ContactlessFrontend('usb') as m: #felicaリーダーusb扱い
    tag = m.connect(rdwr={'on-connect': connected}) #felicaカード情報読み込み
    print(tag) #情報出力
    time.sleep(1) #インターバル