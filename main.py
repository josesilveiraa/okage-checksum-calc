from calculate_crc import CRC

if __name__ ==  "__main__":
    crc = CRC()
    
    with open('./bkmo0.dat', 'rb') as f:
        data = f.read()
        crc.initialize()
        checksum = crc.calculate(data)
        print('[+] Checksum: {0}'.format(checksum))
        print('[+] HEX checksum: {0}'.format(hex(checksum)))
