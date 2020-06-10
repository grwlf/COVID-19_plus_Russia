#!/usr/bin/env python

from os import walk
from os.path import abspath, join
from covid19ru.defs import REGIONS, COVID19RU_ROOT



def rename(root:str=COVID19RU_ROOT, force:bool=False)->None:
  for root, dirs, filenames in walk(abspath(root), topdown=True):
    for filename in sorted(filenames):
      if filename.endswith('csv'):
        with open(join(root,filename), 'r') as f:
          s=f.read()
        for en,_,en2 in REGIONS:
          s=s.replace(en,en2)
        with open(join(root,filename), 'w') as f:
          f.write(s)
  return
