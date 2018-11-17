#### pyranoïd

Require python3 for the Crypto library

Pyranoïd is a python3 script that encrypt a standalone python script with a password.
The cipher is AES in cbc mode. why? ... why not.

The program use getpass unless you use --raw option. It use bz2 to compress the code.


The crypted script has his own source in the \_\_source\_\_ variable, 
and there is the cipher object avaible if you want to reuse the same password to encrypt/decrypt what you want.

The function 'depack' is a dumb function to retreive the source, but you steel need the password to execute it.

If you enter a wrong password normally nothing happend.
