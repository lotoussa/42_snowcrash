### Comment obtenir le flag
level00@SnowCrash:~$ find / -user flag00 2\>/dev/null  
/usr/sbin/john  
/rofs/usr/sbin/john  
level00@SnowCrash:~$ cat /usr/sbin/john /rofs/usr/sbin/john  
cdiiddwpgswtgt  
cdiiddwpgswtgt  
dcode.fr -> bruteforce rot\*(cdiiddwpgswtgt)(rot15) = nottoohardhere  
level00@SnowCrash:~$ su flag00  
Password:  
Don't forget to launch getflag !  
flag00@SnowCrash:~$ getflag  
Check flag.Here is your token : x24ti5gi3x0ol2eh4esiuxias  
