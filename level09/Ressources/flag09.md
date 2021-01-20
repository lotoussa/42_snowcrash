### Comment obtenir le flag
scp -P 4242 level09@192.168.1.44:token Ressources  
xxd -p Ressources/token | sed 's/.\{2\}/& /g'  
66 34 6b 6d 6d 36 70 7c 3d 82 7f 70 82 6e 83 82 44 42 83 44 75 7b 7f 8c 89 0a  
python3 Ressources/decrypt.py  
f3iji1ju5yuevaus41q1afiuq  
level09@SnowCrash:~$ su flag09  
Password:  
Don't forget to launch getflag !  
flag09@SnowCrash:~$ getflag  
Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z  
