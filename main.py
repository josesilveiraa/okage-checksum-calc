from calculate_crc import CRC

if __name__ ==  "__main__":
    crc = CRC()
    
    with open('./bkmo0.dat', 'rb') as f:
        data = f.read()
        crc.initialize()
        checksum = crc.calculate(data[12:])
        print('[*] Checksum: {0}'.format(checksum))