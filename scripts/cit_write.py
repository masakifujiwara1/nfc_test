import nfc
import time
import datetime
import csv

service_code = 0x100b
gakuban = "未検出"
dt_now = datetime.datetime.now()
dt_create_file = dt_now.strftime('%Y-%m-%d %H:%M:%S')

with open('csv/' + str(dt_create_file) + '.csv', 'w') as f:
  writer = csv.writer(f, lineterminator='\n')
  writer.writerow(['date', 'gakuban'])

def connected(tag):
  # 内容を16進数で出力する
  # print("dump felica.")
  # print('  ' + '\n  '.join(tag.dump()))
  #システムコード指定
  idm, pmm = tag.polling(system_code=0x81E1)
  tag.idm, tag.pmm, tag.sys = idm, pmm, 0x81E1
  global gakuban

  if isinstance(tag, nfc.tag.tt3.Type3Tag):
    try:
      
      # 学籍番号出力
      sc = nfc.tag.tt3.ServiceCode(service_code >> 6, service_code & 0x3f)
      # print("sc: "+ str(sc))
      bc = nfc.tag.tt3.BlockCode(2,service=0)
      # print("bc: "+str(bc))
      feli_data = tag.read_without_encryption([sc],[bc])
      # print(feli_data[0:8])
    #   print(feli_data)
      gakuban = feli_data[0:7].decode()
      # def側学番出力
      # print("gakuban:" + gakuban)
      # write()
    except Exception as e:
      print("error: %s" % e)
  else:
    print("error: tag isn't Type3Tag")
  
def write():

  if not gakuban == "未検出":
    date_now = datetime.datetime.now()
    now = date_now.strftime('%H:%M:%S')
    line = [str(now), str(gakuban)]
    with open('csv/' + str(dt_create_file) + '.csv', 'a') as f:
      writer = csv.writer(f, lineterminator='\n')
      writer.writerow(line)
  
  return now

while True:
  with nfc.ContactlessFrontend('usb') as m:
    try:
      tag = m.connect(rdwr={'on-connect': connected})
      now = write()
    except:
      print("status: error")
      print("more slowly\n")
    # ループ側学番出力
    if not gakuban == "未検出":
      print("status: ok")
      print("time: " + now)
      print("gakuban: "+ gakuban + "\n")
    gakuban = "未検出"
    time.sleep(2)