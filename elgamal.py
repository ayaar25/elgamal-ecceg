import random
import elgamal-ecceg.general as g

class ElGamal(object):

  def __init__(self):
    pass

  def gcd(a, b): 
    if a < b: 
        return gcd(b, a) 
    elif a % b == 0: 
        return b; 
    else: 
        return gcd(b, a % b)
  
  def read_file(self, filename):
    data = None
    with open(filename, 'rb') as file:
      data = file.read()
    return data

  def write_file(self, filename, data):
    with open(filename, 'wb') as file:
      file.write(data)

  def key_gen(self, p):
    if (g.is_prime(p) == False):
      return "P is not prime" 
    g = random.randrange(p)
    x = random.randrange(1,p - 2)
    y = (g**x)%p
    key_public = ''+str(y)+','+str(g)+','+str(p)
    key_public = bytes(key_public, "utf-8")
    key_private = ''+str(x)+','+str(p)
    key_private = bytes(key_private, "utf-8")

    self.write_file("key.pub", key_public)
    self.write_file("key.pri", key_private)

if __name__ == '__main__':
  elgamal = ElGamal()
  elgamal.key_gen(6)
  a = elgamal.read_file("key.pub")
  b = elgamal.read_file("key.pri")
  print(a)
  print(b)

