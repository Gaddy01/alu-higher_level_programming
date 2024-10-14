#!/usr/bin/env python3


import os

pyfile=os.getenv("PYFILE")

file=open("pyfile","r")
exec(file.read())

file close
