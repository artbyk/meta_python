import os
import threading

def calculator(num):
        degree = int(num / 8)
        ret = ""
        mask = 0b11111111
        for i in range(0,degree):
            ret += str(mask)+"."
        mask = int('{:08b}'.format(mask >> 8 - num%8)[::-1], 2)
        ret += str(mask)
        for i in range(0, 4-degree-1):
            ret +=".0"
        return ret

class MyThread(threading.Thread):
    def run(self):
        os.system("/kepm/prp/prpstart.sh "+netmask)
        pass

netmask = str(calculator(int(os.popen('grep -v "Gate" /kepm/wired.network | grep -oE "\/[0-9]{1,2}"| grep -oE "\w+"').read()))) # Take the netmask from eth0
thread = MyThread()
thread.daemon = True
thread.start()