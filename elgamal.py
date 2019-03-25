import random
import pickle
import array
import re
from base.general import is_prime

class ElGamal(object):

  def __init__(self):
    pass
  
  def read_file(self, filename):
    data = None
    with open(filename, 'rb') as file:
      data = file.read()
    return data
  
  def read_file_list(self, filename):
    itemlist = None
    with open(filename, 'rb') as file:
      itemlist = pickle.load(file)
    return itemlist

  def write_file(self, filename, data):
    with open(filename, 'wb') as file:
      file.write(data)
      
  def write_file_list(self, filename, data):
    with open(filename, 'wb') as file:
      pickle.dump(data, file)

  def key_gen(self, p):
    if (is_prime(p) == False):
      return "P is not prime" 
    g = random.randrange(p)
    x = random.randrange(1,p - 2)
    y = (g**x)%p
    key_public = [y,g,p]
    key_private = [x,p]
    
    self.write_file_list("key.pub", key_public)
    self.write_file_list("key.pri", key_private)
  
  def encrypt(self, filename, key_public, key_private):
    plaintext = self.read_file(filename)
    list_plaintext = list(plaintext)
    list_plain_int = list(map(int, plaintext))
    key_pub = self.read_file_list(key_public)
    key_pri = self.read_file_list(key_private)
    
    y = key_pub[0]
    g = key_pub[1]
    p = key_pub[2]
    x = key_pri[0]

    k = random.randrange(1,p-2)

    list_cipher_int = []
    for inc in range(len(list_plain_int)):
      a = (g**k)%p
      b = ((y**k)*list_plain_int[inc])%p
      list_cipher_int.append(a)
      list_cipher_int.append(b)
    print(list_plain_int)
    regex = re.compile('.\w+').findall(filename)
    print(regex)
    self.write_file_list("cipher" + regex[-1], list_cipher_int)
    print(list_cipher_int)
  
  def decrypt(self, filename, key_public, key_private):
    list_cipher_int = self.read_file_list(filename)
    key_pub = self.read_file_list(key_public)
    key_pri = self.read_file_list(key_private)

    y = key_pub[0]
    g = key_pub[1]
    p = key_pub[2]
    x = key_pri[0]
    
    list_plain_int = []
    inc = 0
    while inc < len(list_cipher_int):
      pangkat = p-1-x
      axinf = (list_cipher_int[inc]**pangkat)%p
      message = (axinf*list_cipher_int[inc+1])%p
      list_plain_int.append(message)
      inc+=2

    regex = re.compile('.\w+').findall(filename)
    self.write_file("out"+ regex[-1], array.array('B', list_plain_int).tobytes())
    print(list_plain_int)

if __name__ == '__main__':
  elgamal = ElGamal()
  elgamal.key_gen(233)
  a = elgamal.read_file_list("key.pub")
  b = elgamal.read_file_list("key.pri")
  elgamal.encrypt("plain.txt", "key.pub", "key.pri")
  elgamal.decrypt("cipher.txt", "key.pub", "key.pri")
  # list_a = int.from_bytes(a, byteorder='big')
  # print(a)
  # print(a[0])
  # print(b)
  

