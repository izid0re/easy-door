#! /usr/bin/env python3
import base64
import bz2
import hashlib
import getpass
import inspect
import bz2
from Crypto import Random
from Crypto.Cipher import AES
import sys
import os
class Cipher(object):
	def __init__(self, key): 
		self.bs = 32
		self.key = hashlib.sha256(key.encode()).digest()

	def encrypt(self, raw):
		raw = self._pad(raw)
		iv = Random.new().read(AES.block_size)
		cipher = AES.new(self.key, AES.MODE_CBC, iv)
		return base64.b64encode(iv + cipher.encrypt(raw))

	def decrypt(self, enc):
		enc = base64.b64decode(enc)
		iv = enc[:AES.block_size]
		cipher = AES.new(self.key, AES.MODE_CBC, iv)
		return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

	def _pad(self, s):
		return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)
	@staticmethod
	def from_ask_pass(prompt="passwd > "):
		pw = getpass.getpass(prompt)
		if pw != getpass.getpass("confirm > "):
			print ("password do not matchi")
			return None
		return Cipher(pw)
	@staticmethod
	def from_pass(prompt="passwd > "):
		return Cipher(getpass.getpass(prompt))
	@staticmethod
	def from_raw_ask_pass(fin=None, fout=None, prompt="passwd > "):
		fin = fin or sys.stdin
		fout = fout or sys.stdout
		fout.write(prompt)
		fout.flush()
		pw = fin.readline()
		fout.write("confirm > ")
		fout.flush()
		if pw != fin.readline():
			fout.write("password do not match!\n")
			fout.flush()
			return None
		return Cipher(pw[:-1])
	@staticmethod
	def from_raw_pass(fin=None, fout=None, prompt="passwd > "):
		fin = fin or sys.stdin
		fout = fout or sys.stdout
		fout.write(prompt)
		fout.flush()
		pw = fin.readline()		
		return Cipher(pw[:-1])
	@staticmethod
	def _unpad(s):
		return s[:-ord(s[len(s)-1:])]
def lineno():
	return inspect.currentframe().f_back.f_lineno
HEAD=[0,lineno()]
def isPackSource(data):
	return data.endswith("# PyPack.v0\n")
def get_head():
	try:
		p = __file__
	except:
		return
	p = os.path.abspath(p)
	d = ""
	with open(p, "r") as r:
		d = r.read()
	if isPackSource(d):
		d = d.split('\n')[HEAD[0]:HEAD[1]]
		return "\n".join(d)
	return

def tob(bos):
	if isinstance(bos,bytes):
		return bos
	return bos.encode('utf-8')
def tos(bos):
	if isinstance(bos,str):
		return bos
	return bos.decode('utf-8')

def build_seq(cipher, crypt=True, compress=True, reverse=False):
	seq = []
	if crypt:
		seq.append(cipher.encrypt if not reverse else cipher.decrypt)
	if compress:
		seq.append(bz2.compress if not reverse else bz2.decompress)
	if reverse:
		seq = seq[::-1]
	return seq

def crypt(data, cipher,crypt=True,compress=True,reverse=False):
	seq = build_sequence(cipher, crypt=crypt, compress=compress, reverse=reverse)
	for s in seq:
		data = s(data)
	return data
def pack(data="print('packed!',dir(),__file__)", raw=False):
	cipher=Cipher.from_ask_pass()
	head = get_head()
	if not head:
		return
	data = '__source__=base64.b64decode("' + tos(base64.b64encode(tob(data))) + '")\n' + data
	if not raw:
		data = head + "\ntry:\n\t" + 'cipher=Cipher.from_pass("pack.pw> ");\nexcept KeyboardInterrupt:sys.exit()\nexcept:sys.exit(1);\nexec(cipher.decrypt(base64.b64decode("' + tos(base64.b64encode( cipher.encrypt(data))) + '")))'
	else:
		data = head + "\ntry:\n\t" + 'cipher=Cipher.from_raw_pass(prompt="pack.pw> ");\nexcept KeyboardInterrupt:sys.exit()\nexcept:sys.exit(1);\nexec(cipher.decrypt(base64.b64decode("' + tos(base64.b64encode( cipher.encrypt(data))) + '")))'
	data = '#! /usr/bin/python3.6\nimport base64\nimport bz2\nexec(bz2.decompress(base64.b64decode("' + tos(base64.b64encode(bz2.compress(tob(data)))) + '")).decode("utf-8"))'
	return data
def depack(data):
	data = data.replace("exec","out=")
	d={}
	exec(data,d)
	data = d["out"]
	data = data.replace("exec","out=")
	exec(data,d)
	return d['out']
if __name__ == "__main__" :
	import argparse
	ap = argparse.ArgumentParser()
	ap.add_argument("-s", "--src")
	ap.add_argument("-r","--reverse", action="store_true")
	ap.add_argument("-R","--raw", action="store_true")

	ns = ap.parse_args()
	data = ""
	if ns.src:
		with open(ns.src, 'r') as r:
			data = r.read()
	else:
		data = sys.stdin.read()
	if ns.reverse:
		print(depack(data))
	else:
		print(pack(data, ns.raw))
	#print(depack(p))
# PyPack.v0
