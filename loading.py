from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep
from animations import animations as ani

class Loader:
  def __init__(self, desc="Loading", end="Done!", animation="simpleDotsScrolling", timeout=0.1):
    self.desc = desc
    self.end = end
    self.timeout = timeout

    self.thr = Thread(target=self.animate, daemon=True)
    self.steps = ani[animation]["frames"]
    self.done = False

  def start(self):
    self.thr.start()
    return self

  def animate(self):
    for c in cycle(self.steps):
      if self.done:
        break
      print(f"\r{self.desc} {c}", flush=True, end="")
      sleep(self.timeout)

  def stop(self):
    self.done = True
    cols = get_terminal_size((80, 20)).columns
    print("\r" + " " * cols, end="", flush=True)
    print(f"\r{self.end}", flush=True)
