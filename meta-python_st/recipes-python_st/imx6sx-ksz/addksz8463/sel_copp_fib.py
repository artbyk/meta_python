from ksz8463 import Ksz

ksz = Ksz()

if Ksz.spitest_silence() == '0X8443':
    Ksz.sel_copp_fib()
else:
    print("Spi doesn't work right. Ksz mode not selected")  
