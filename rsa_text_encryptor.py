

def main():
    args = get_args()
    try:
        text = args[0]
        public_key = args[1]
        out_file_name = args[2]
    except:
        return
    try:
        encrypt_text(text, public_key, out_file_name)
    except:
        pass


def encrypt_text(text, public_key, out_file_name):
    byte_list = text_to_byte_array(text)
    encrypted = []
    for item in byte_list:
        encrypted_item = encrypt(item, public_key)
        encrypted.append(encrypted_item)
    encrypted = text_to_byte_array(str(encrypted))
    encrypted = bytearray(encrypted)
    out_file_name = out_file_name + '_text.rsa-enc'
    f = open(out_file_name, 'wb')
    f.write(encrypted)
    f.close()


def encrypt(message, public_key):
    n = public_key[0]
    e = public_key[1]
    output = (message ** e) % n
    return output


def get_args():
    text = input('enter/paste text to encrypt:')
    public_key = input('enter encrypton key:')
    try:
        public_key = public_key.split('-')
        public_key = [int(x) for x in public_key]
        out_file_name = input('enter the output file name (no extension):')
    except:
        print('ERROR! INVALID KEY!')
        input('press the enter key to exit the program . . .')
        return False
    return [text, public_key, out_file_name]

    
def text_to_byte_array(text_in):
    f = open('temp', 'w')
    f.write(text_in)
    f.close()
    f = open('temp', 'rb')
    data = f.read()
    data = list(data)
    f.close()
    import os
    os.remove('temp')
    return data

if __name__ == '__main__':
    main()
