#!/usr/bin/env python
import os
import struct
import time
from panda.lib.panda import Panda

if __name__ == "__main__":
  if os.getenv("WIFI") is not None:
    p = Panda("WIFI")
  else:
    p = Panda()
  print p.health()
  print p.get_serial()

  t1 = time.time()
  for i in range(100):
    p.get_serial()
  t2 = time.time()
  print "100 requests took %.2f ms" % ((t2-t1)*1000)

  p.set_controls_allowed(True)

  a = 0
  while 1:
    # flood
    msg = "\xaa"*4 + struct.pack("I", a)
    p.can_send(0xaa, msg, 0)
    p.can_send(0xaa, msg, 1)
    p.can_send(0xaa, msg, 4)
    time.sleep(0.01)

    dat = p.can_recv()
    if len(dat) > 0:
      print dat
    a += 1

