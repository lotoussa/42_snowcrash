### Comment obtenir le flag
level02@SnowCrash:~$ tcpdump -r level02.pcap -A "tcp[tcpflags] & (tcp-push) != 0"  
ft\_waNDReL0L  
level02@SnowCrash:~$ su flag02  
Password:  
Don't forget to launch getflag !  
flag02@SnowCrash:~$ getflag  
Check flag.Here is your token : kooda2puivaav1idi4f57q8iq  
