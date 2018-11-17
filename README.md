#### pyranoïd

Require python3 for the Crypto library

Pyranoïd is a python3 script that encrypt a standalone python script with a password.
The cipher is AES in cbc mode. why? ... why not.

The program use getpass unless you use --raw option. It use bz2 to compress the code.


The crypted script has his own source in the __source__ variable, 
and there is the cipher object avaible if you want to reuse the same password to encrypt/decrypt what you want.

The function 'depack' is a dumb function to retreive the source, but you steel need the password to execute it.

exemple:

> echo print\(dir\(\)\) > test.py
> ./pyranoïd -s test.py > tst.cry
password >
confirm >
> cat tst.cry
#! /usr/bin/python3.6
import base64
import bz2
exec(bz2.decompress(base64.b64decode("QlpoOTFBWSZTWW+TyzsAAKDfgAAwev//e397//6////wUAQe7QQNoNAASkTQJ6Rqam9T0nkTDSY1NI9MiehqHtKbUyHqB5TaHDTTBDIaaZGTCAaaAMJo0yYAEDQSmiEalP01NTI8po0xM1NPSHqADEM0mgxHqMmhw00wQyGmmRkwgGmgDCaNMmABA0EihAmk9TxpU8SbRqJ5Jsp7VP0oeTQABGRgmnqNFjSgwbE2AxibQxiGhJtEOAa8jt+SA0iGhtFFECtyOxBXQhA8N0abvFJW9Phv2fq7CeFaLgZESuVri4OCi1SveM+6pxpWFeqpC0DKBo+1TUJuKXOzvDm7inUrZCZnHCkCV/fitGylkiZMdpkjUeSVq3ClQ3No6afqLUNvA4I70GeMuNJSRVJrhzItUjuLXeUWmKM7uQDtOeJnH6E8ru0YcwsD2ECldBjNvDPVjfehNnto9bKUkO0qpqKZZPZlnrLC0zwXntHcR6Jl+UksnjIMzOzsalO6K5+2RpmDGI8mKAefnTqfCEIWWN32e3bJaY8P+cP5n4i4MEce35qkpRO6OmbVQD6WasydAhfUlwH8l4Ye4Q+KhSkxsDBKLKnROvUhs5GJRHlcOs10bDtNbyGlRh8ybFjowbtsAHp+pzhM39tXoclfIvPs0/mtPZ7l9Nle6aXlquHq3N9ZJOppfC6RcYOzm/u96X5XnoiDFNn+AFjfbx3OXK2wRVb7a3KbbXPEkcx9HHTPX4TRe/I2cpw955SCvHt1Fs7zS0lxN17XlZ3WO1C0UjGZcz0N/w5GDXXs/Y+FIWF5XwNAXlqLBfxz851zUqc0/Qz73+uttd3YmZsaMHZZu3zPcULdBeO+cvb56zF5gS5xx0mr6UcYaSwG8MbJe/l6rEfG1swwQYWyma/LeuOwyKRj624DqhAibohtCHqeQcNQs1zgIqEuRYa7h4Tcbln7248CFj25IaVKRUtKzHQj498R+RiFrEUmJejEtJBIkMBlNpCTVbgmVXzC+2FB3EKiJmFDHuc3VtrzFaLyq0vAgbktrKhdFJq3z4CUilPF0tOhzVyAkSv0qsNNrotOd9RD5P6LuiCA9LwibbpvrTT9c4eHUHRpGsPLBFZ0F6M/gEUAMKwGNduCiEmTPTJBYUFCYNalAhJWnWRXpkbOW4gQy18i4ETRVMbQo9gpFwdh8uYRHeLDuiXf7JbG8BpjGoi/TlNCF49wjLn0BvjNXkRSHDGARKClU8TI5VLiBo7rC57NGawsyLFszhxVJG9whkYpGdKQELswivTrRtJY5YbFFA5jcXIkmH8ylMGEBmMBwLgnQZJmslBIMO1FIZxZvQMKjCyBPJpYkSBXoKEFRQBATNvFRx1I9+zEiFAb1jxRppRnIpfu0jP1fLq1E+NIywDx6AD6zWLOnpxRPFODGmYaBaw706keqyCJ7oQSrSt5Dp5rtLwWH/i7kinChIN8nlnY")).decode("utf-8"))
> python3.6 tst.cry
pack.pw>
['AES', 'Cipher', 'HEAD', 'Random', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__source__', '__spec__', 'base64', 'bz2', 'cipher', 'getpass', 'hashlib', 'inspect', 'lineno', 'os', 'sys']

If you enter a wrong password normally nothing happend.

