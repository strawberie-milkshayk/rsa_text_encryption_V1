

def main():
    args = get_args()
    try:
        file_path = args[0]
        private_key = args[1]
        decrypted = decrypt_text(file_path, private_key)
        print('\nDECRYPTED TEXT:')
        print('-' * 20)
        print(decrypted)
        print('-' * 20)
    except:
        print('\nDECRYPTED TEXT:')
        print('-' * 20)
        print('you entered the wrong decryption key! it sure would be unfortunate if i just...')
        print('-' * 20)
        import time
        import webbrowser
        time.sleep(5)
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        time.sleep(5)
        webbrowser.open('https://cdn.discordapp.com/attachments/843374277382373394/863313501396271134/secret_message.gif')

def get_args():
    input('press enter to select file to decrypt . . .')
    file_path = get_file()
    private_key = input('enter key:')
    try:
        private_key = private_key.split('-')
        private_key = [int(x) for x in private_key]
    except:
        return False
    return [file_path, private_key]
    


def decrypt_text(file_loc, private_key):
    f = open(file_loc, 'r')
    file_data = f.read()
    file_data = str(file_data)
    file_data = file_data[1:len(file_data) - 1]
    file_data = file_data.split(', ')
    file_data = [int(x) for x in file_data]
    f.close()
    decrypted_bytes = []
    for item in file_data:
        decrypted_byte = decrypt(item, private_key)
        decrypted_bytes.append(decrypted_byte)
    f = open('temp', 'wb')
    f.write(bytearray(decrypted_bytes))
    f.close()
    f = open('temp', 'r')
    text = f.read()
    f.close()
    import os
    os.remove('temp')
    return text


def decrypt(message, private_key):
    n = private_key[0]
    d = private_key[1]
    output = (message ** d) % n
    return output




def get_file():
    from tkinter import Tk     # from tkinter import Tk for Python 3.x
    from tkinter.filedialog import askopenfilename

    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)
    return filename


if __name__ == '__main__':
    main()
