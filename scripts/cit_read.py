import nfc
import time

service_code = 0x100b

def connected(tag):
  # 内容を16進数で出力する
  print("dump felica.")
  print('  ' + '\n  '.join(tag.dump()))
  #システムコード指定
  idm, pmm = tag.polling(system_code=0x81E1)
  tag.idm, tag.pmm, tag.sys = idm, pmm, 0x81E1
  global gakuban

  if isinstance(tag, nfc.tag.tt3.Type3Tag):
    try:
      
      # 学籍番号出力
      sc = nfc.tag.tt3.ServiceCode(service_code >> 6, service_code & 0x3f)
      print("sc: "+ str(sc))
      bc = nfc.tag.tt3.BlockCode(2,service=0)
      print("bc: "+str(bc))
      feli_data = tag.read_without_encryption([sc],[bc])
      print(feli_data[0:8])
    #   print(feli_data)
      gakuban = feli_data[0:8].decode()
      # def側学番出力
      print("gakuban:" + gakuban)
    except Exception as e:
      print("error: %s" % e)
  else:
    print("error: tag isn't Type3Tag")


while True:
  with nfc.ContactlessFrontend('usb') as m:
    tag = m.connect(rdwr={'on-connect': connected})
    # ループ側学番出力
    print("main gakunow: "+ gakuban)
    time.sleep(1)