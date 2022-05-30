def mask_calculator(str):
    mass = str.split('.')
    ret = 0
    for i in mass:
        ret += bin(int(i)).count("1")
    return ret

def write_bytes(byte_number,data, path):
    f = open(path, 'rb')
    d = list(f.read())
    counter = 0
    try:
        for i in byte_number:
            print(i)
            d[i] = int(data[counter])
            counter+=1
    except TypeError:
        d[byte_number] = int(data)
    f.close()

    f = open(path, 'wb')
    f.write(bytes(d))
    f.close()

def read_bytes(path='/kepm/settings.kprm61850'):
    f = open(path, 'rb')
    d = list(f.read())
    f.close()
    return d

def setting_write(ip, mask, gate,path='/kepm/settings.kprm61850'):
    ip_adr = [16, 17, 18, 19]
    mask_adr = 20
    gate_adr = [21, 22, 23, 24]
    ip = ip.split('.')
    mask = mask_calculator(mask)
    gate = gate.split('.')

    write_bytes(ip_adr,ip, path)
    write_bytes(mask_adr, mask, path)
    write_bytes(gate_adr, gate, path)