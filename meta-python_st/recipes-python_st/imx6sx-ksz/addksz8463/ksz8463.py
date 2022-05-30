import spidev
import logging
import time
import sys
import os
import subprocess

class Ksz:

    def switch_enable():
        Ksz.spi2(adress = 0x000,data = [0x01,0x00],rw = 1,max_speed = 5000000)
        
    
    def switch_disable():
        Ksz.spi2(adress = 0x000,data = [0x00,0x00],rw = 1,max_speed = 5000000)

    def switch_power_off(): #broken
        # result_tx, result_rx = Ksz.spi2(adress=0X032,data=[0x1000,0x00],rw=1)
        # print(result_tx,result_rx)
        Ksz.spitest(adress=0X032,data=[0x02,0x00],rw=1)
        Ksz.spitest(adress=0X032,data=[0x00,0x00],rw=0)
    def switch_power_on(): #broken
        Ksz.spitest(adress=0X032,data=[0x00,0x00],rw=1)
        Ksz.spitest(adress=0X032,data=[0x00,0x00],rw=0)
        

    def global_reset():#broken
        # Ksz.spi2(adress = 0x126,data = [0x1,0x1],rw = 1,max_speed = 5000000)
        Ksz.spitest(adress=0x126,data=[0x1,0x00],rw=1)
        print("read")
        Ksz.spitest(adress=0x126,data=[0x01,0x00],rw=0)
        # time.sleep(1)
        # Ksz.spi2(adress = 0x126,data = [0x00,0x00],rw = 1,max_speed = 5000000)
        Ksz.spitest(adress=0x126,data=[0x00,0x00],rw=1)
        print("read")
        Ksz.spitest(adress=0x126,data=[0x00,0x00],rw=0)

    def blink():
        for i in range(0,10):
            Ksz.spi2(adress = 0x06C,data = [0x00,0x40],rw = 1,max_speed = 5000000)
            Ksz.spi2(adress = 0x084,data = [0x00,0x00],rw = 1,max_speed = 5000000)
            time.sleep(1)
            Ksz.spi2(adress = 0x06C,data = [0x00,0x00],rw = 1,max_speed = 5000000)
            Ksz.spi2(adress = 0x084,data = [0x00,0x40],rw = 1,max_speed = 5000000)
            time.sleep(1)
        Ksz.spi2(adress = 0x084,data = [0x00,0x00],rw = 1,max_speed = 5000000)
        Ksz.spi2(adress = 0x06C,data = [0x00,0x00],rw = 1,max_speed = 5000000)

    def spi2(adress,data = [0x00,0x00],rw = 0,bus = 0,dev = 0,max_speed = 12000000,mode = 0b00,bits_word = 8):
        spi = spidev.SpiDev()
        spi.open(bus, dev)
        spi.max_speed_hz = max_speed
        spi.lsbfirst = False
        spi.cshigh = False
        spi.mode = mode
        spi.bits_per_word = bits_word
        adress = int(Ksz.convert_base(adress))
        # print(adress)
        if rw == 0:
            mask1 = 0b00000000
        elif rw == 1:
            mask1 = 0b10000000 
        mask2 = 0b00001100
        result_tx = []
        save = adress
        adress = adress >> 4
        adress = adress + mask1
        # print(adress)
        result_tx.append(adress)

        adress = save
        adress = adress << 4
        # print(adress)
        for i in range(8, 15):
            adress = adress & ~(1 << i)
        adress = adress + mask2
        # print(adress)
        result_tx.append(adress)
        for i in range(0,len(data)):
            result_tx.append(data[i])
        result_rx = spi.xfer(result_tx)
        spi.close()
        return result_tx, result_rx

    def convert_base(num, to_base=10, from_base=16):
        # first convert to decimal number
        if isinstance(num, str):
            n = int(num, from_base)
        else:
            n = int(num)
        # now convert decimal to 'to_base' base
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < to_base:
            return alphabet[n]
        else:
            return Ksz.convert_base(n // to_base, to_base) + alphabet[n % to_base]

    def spitest(adress = 0x00,data = [0x00,0x00],rw = 0):
        txData, rxData = Ksz.spi2(adress,data,rw)

        print(" ")
        print("TX_DATA:")
        print(txData)
        for i in range(len(rxData)):
            print (format(txData[i],'#b')) 
        print(" ")
        print("RX_DATA:")
        print(rxData)
        for i in range(len(rxData)):
            print (format(rxData[i],'#b')) 
        print(" ")
        print (format(rxData[3],'#X')+format(rxData[2],'X'))
        return str(format(rxData[3],'#X')+format(rxData[2],'X'))

    def spitest_silence():
        txData, rxData = Ksz.spi2(adress = 0x00,data = [0x00,0x00])
        return str(format(rxData[3],'#X')+format(rxData[2],'X'))
    def spi_read_copp():
        txData, rxData = Ksz.spi2(adress = 0x0D8,data = [0xFE,0x00],rw = 0,max_speed = 5000000)

        print(" ")
        print("TX_DATA:")
        print(txData)
        for i in range(len(rxData)):
            print (format(txData[i],'#b')) 
        print(" ")
        print("RX_DATA:")
        print(rxData)
        for i in range(len(rxData)):
            print (format(rxData[i],'#b')) 
        print(" ")
        print (format(rxData[3],'#X')+format(rxData[2],'X')) 

    def iterate_over_values(start = 0X0D8, stop = 0X0D9):
        logging.basicConfig(level=logging.DEBUG, filename=r'iteratelog.log', filemode='w',
                            format='%(name)s - %(levelname)s - %(message)s')
        adress = start
        while(adress < stop):
            print(hex(adress))
            logging.info(" ")
            logging.info(hex(adress))
            txData, rxData = Ksz.spi2(adress = adress,data = [0x00,0x00],rw = 0)
            TX = format(txData[0],'#X')+format(txData[1],'X')
            RX = format(rxData[3],'#X')+format(rxData[2],'X')
            logging.info("TX:" + TX)
            logging.info("RX:" + RX)
            logging.info(" ")
            adress = adress + 2
        print("\033[32m {}".format("Done"))
        print("\033[37m {}".format(" "))

    def port_1_power_off():
        Ksz.spi2(adress = 0x04C,data = [0x20,0x39],rw = 1,max_speed = 5000000)

    def port_1_power_on():
        Ksz.spi2(adress = 0x04C,data = [0x20,0x31],rw = 1,max_speed = 5000000)

    def port_2_power_off():
        Ksz.spi2(adress = 0x058,data = [0x20,0x39],rw = 1,max_speed = 5000000)

    def port_2_power_on():
        Ksz.spi2(adress = 0x058,data = [0x20,0x31],rw = 1,max_speed = 5000000)

    def select_fiber_mode():
        Ksz.spi2(adress = 0x0D8,data = [0x3E,0x00],rw = 1,max_speed = 5000000)

    def select_copper_mode():
        Ksz.spi2(adress = 0x0D8,data = [0xFE,0x00],rw = 1,max_speed = 5000000)

    def gpio_check_status(pin = 125):
        print("pin = " + str(pin))
        command = 'echo ' + str(pin)+' > /sys/class/gpio/export'
        result = os.system(command)
        if result != 0:
            sys.exit("Something went wrong")
        command = 'echo "in" > /sys/class/gpio/gpio' + str(pin)+'/direction'
        result = os.system(command)
        if result != 0:
            sys.exit("Something went wrong")
        command = 'cat /sys/class/gpio/gpio' + str(pin)+'/value'
        result = os.popen(command).read()
        logging.info("GPIO " + str(pin) +" status = "+ str(result))
        status = result
        print("GPIO " + str(pin) +" status = "+ str(result))
        command = 'echo ' + str(pin)+' > /sys/class/gpio/unexport'
        result = os.system(command)
        if result != 0:
            sys.exit("Something went wrong")
        print(status)
        return status

    def gpio_check_status_silence(pin = 125):
        # print("pin = " + str(pin))
        command = 'echo ' + str(pin)+' > /sys/class/gpio/export'
        result = os.system(command)
        if result != 0:
            sys.exit("Something went wrong")
        command = 'echo "in" > /sys/class/gpio/gpio' + str(pin)+'/direction'
        result = os.system(command)
        if result != 0:
            sys.exit("Something went wrong")
        command = 'cat /sys/class/gpio/gpio' + str(pin)+'/value'
        result = os.popen(command).read()
        logging.info("GPIO " + str(pin) +" status = "+ str(result))
        status = result
        # print("GPIO " + str(pin) +" status = "+ str(result))
        command = 'echo ' + str(pin)+' > /sys/class/gpio/unexport'
        result = os.system(command)
        if result != 0:
            sys.exit("Something went wrong")
        # print(status)
        return int(status)

    def iterate_over_pins(start = 0, stop = 127):
        logging.basicConfig(level=logging.DEBUG, filename=r'GPIOlog2.log', filemode='w',
                            format='%(name)s - %(levelname)s - %(message)s')
        adress = start
        while(adress < stop):
            try:
                Ksz.gpio_check_status_silence(pin = adress)
                adress = adress + 1
            except:
                logging.info("GPIO " + str(adress) +" status = busy")
                print("GPIO " + str(adress) +" status = busy")
                adress = adress + 1
        print("\033[32m {}".format("Done"))
        print("\033[37m {}".format(" "))

    def sel_copp_fib():
        if Ksz.gpio_check_status_silence(pin = 125) == 0:
            Ksz.select_copper_mode()
            print("Copper mode selected")
        if Ksz.gpio_check_status_silence(pin = 125) == 1:
            Ksz.select_fiber_mode()
            print("Fiber mode selected")

    def read_status_port1():
        result_tx, result_rx = Ksz.spi2(adress = 0x04E)
        if result_rx[3] == 8:
            print("Port 1 is down")
        if result_rx[3] == 44:
            print("Port 1 is up")


    def read_status_port2():
        result_tx, result_rx = Ksz.spi2(adress = 0x05A)
        if result_rx[3] == 8:
            print("Port 2 is down")
        if result_rx[3] == 44:
            print("Port 2 is up")
    def test():
        print("test")

if __name__ == "__main__":
    method_name =  sys.argv[1]
    parametr_count = len(sys.argv)-2
    args = []
    
    for i in range(2,len(sys.argv)):
        args.append(sys.argv[i])
    try: 
        getattr(Ksz, method_name)(*args)

    except:
        print("There is no parameter")
        getattr(Ksz, method_name)()