#!/usr/bin/python3

import concurrent.futures
import subprocess
import sys

def try_password(aPassword, aFile, aExecutor):
  myRet = subprocess.call(["7z", "t", "-p\"" + aPassword + "\"", aFile], stdout=subprocess.DEVNULL)
  if myRet == 0:
    print ("The password is: " + aPassword)

myFilename = sys.argv[2]
myPasswordFile = sys.argv[1]

print ("File to crack: " + myFilename)
print ("Password list: " + myPasswordFile)

myFile = open(myPasswordFile, "rt")
myExecutor = concurrent.futures.ThreadPoolExecutor(max_workers=3)
for myLine in iter(myFile):
  myPassword = myLine.strip('\n')
  myExecutor.submit(try_password, myPassword, myFilename, myExecutor)
