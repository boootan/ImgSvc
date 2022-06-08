import hashlib

def main():
    file = open('testhash.txt', 'w')
    correctKey = input("Compute this hash using the correct shared key or baloney? Input Y or N")
    if correctKey == 'Y':
        sharedKey = 'foobar'
    elif correctKey == 'N':
        sharedKey = '123456781234567812345678'
    else:
        return

    IdNumber = '123456789'
    hash = hashlib.sha1(IdNumber.encode() + sharedKey.encode())
    file.writelines(hash.hexdigest())
    file.close()

if __name__ == '__main__':
    main()
