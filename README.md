# pybin
Pybin is an open-source, online pastebin that keeps the server entirely blind to the content you share.

The data is stored encrypted with 256-bit AES encryption in GCM. Server **does not** store decryption keys, they are part of a url
![image](https://github.com/user-attachments/assets/ac9ace1d-9bb9-4022-b71b-44ddca0a1675)

## How it works
Common url: ```V5i0G9acTt1DDFAW3N4P-2aW29gBMhQ6nEct3vz2oSwqjZdOAYwo=```
consists of two parts:
  1) first 9 chars - id of the paste
  2) rest of the string is a decryption key for your paste

Pybin stores only encrypted paste and corresponding id.
