# 7zpasscrack
Brute force password cracking for 7zip archives written in Python3. 

The program cycles through a list of passwords and checks them against 
the archive.

Requires 7zip to be installed and a list of passwords such as `rockyou` 
or `crackstation`.

# To Do
There are still work to do to make this a finished program. For example,
the threads aren't stopped when the right password is found so the 
program doesn't stop and continues. 

# Disclaimer
This is a tool for use in cracking one's own files for which you forgot
the password, not to illegally access other's files.
