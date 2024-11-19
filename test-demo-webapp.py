#!/usr/bin/python

import requests
import sys
from threading import Thread
import queue

class testdemowebapp:

  def __init__(self):
    self.url =  "http://localhost:8000/demo-1.0/demo"
    self.counter = 0
    self.JSESSIONID = None

  # Return False if sticky True otherwise
  def request_response(self):
    headers = {'user-agent': 'test-demo-webapp'}
    if self.JSESSIONID is not None:
      cookies = {'JSESSIONID': self.JSESSIONID}
      r = requests.get(self.url, headers=headers, cookies=cookies)
    else:
      r = requests.get(self.url, headers=headers)
    for c in r.cookies:
      if c.name == "JSESSIONID":
        if self.JSESSIONID is None:
          self.JSESSIONID = c.value
        elif self.JSESSIONID != c.value:
          return False
    return True

  # Return False if sticky True otherwise
  def request_response_loop(self, n):
    i = 0
    while self.request_response():
      i = i + 1
      if i == n:
        return True
    return False

  def start(result_queue, n, tid):
    mydemo = testdemowebapp()
    result_queue.put((tid, 'done' if mydemo.request_response_loop(n) else 'failed'))

if __name__ == "__main__":
  args = sys.argv[1:]
  count = 1
  loop = 1000
  if len(args) >= 1:
    count = int(args[0])
  if len(args) == 2:
    loop = int(args[1])

  q = queue.Queue()
  tarr = [] 
  for i in range(count):
    t = Thread(target=testdemowebapp.start, args=(q, loop, i), daemon=True)
    tarr.append(t)
  for i in range(count):
    tarr[i].start()

  for i in range(count):
    r = q.get()
    if r[1] != 'done':
      print("Failed")
      break
