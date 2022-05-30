#! /bin/sh
(kill -TSTP $$; kill -CONT $$)
sleep 1
ip="$(grep -v 'Gate' /kepm/wired.network | grep -oE "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}")"
# netmask="$(grep -v "Gate" /kepm/wired.network | grep -oE "\/[0-9]{1,2}"| grep -oE "\w+")"
netmask=$1
sleep 7; ifconfig prp1 $ip netmask $netmask  &
# cd /kepm/prp  #/sw_stack_prp1-master/prp_pcap_tap_userspace/
echo 1 > prp_conf.txt
ret="$(cat prp_conf.txt)"


com="./prp_stack eth0 eth1"


if [ $ret != '0' ]; then
  $com
  
  
else
  echo "Change prp_conf.txt value"  
fi