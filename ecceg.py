import random
import pickle
import array
import math
import re
from base.general import is_prime
from point import Point
from pointoperatorecc import PointOperatorECC

class EllipticCurveCryptoElGamal(object):

  def __init__(self, A, B, P, k):
    # ECC Equation Constanta, y^2 mod P = x^3 + Ax + B mod P
    self.A = A
    self.B = B
    self.P = P
    self.k = k # For encoding & decoding
    
  def _get_A(self):
    return self.A
  
  def _get_B(self):
    return self.B
  
  def _get_P(self):
    return self.P
  
  def _get_k(self):
    return self.k

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

  def generate_pow_two(self):
    list_powered_two = []
    for i in range(self._get_P()):
      list_powered_two.append(i*i)
    return list_powered_two

  def generate_galois_field(self):
    field = []
    for i in range(self._get_P()):
      list_y = self.compute_ecc_equation(i)
      if list_y:
        for j in range(len(list_y)):
          point = Point()
          point._set_x(i)
          point._set_y(list_y[j])
          field.append(point)
    return field
  
  def compute_ecc_equation(self, x):
    result = []
    list_powered_two = self.generate_pow_two()
    y = x**3 + self._get_A()*x + self._get_B()
    for i in range(self._get_P()):
      if list_powered_two[i] % self._get_P() == y % self._get_P():
        result.append(i)
    return result
  
  def key_gen(self, n):
    process = PointOperatorECC(self._get_A(), self._get_B(), self._get_P())
    field = self.generate_galois_field()
    # Base point in galois field[0]
    base = field[0]
    a = random.randrange(n)
    b = random.randrange(n)
    Ka = process.multiply(a, base)
    Kb = process.multiply(b, base)
    pointA = [Ka._get_x(), Ka._get_y()]
    pointB = [Kb._get_x(), Kb._get_y()]
    
    self.write_file_list("keyA.pri", a)
    self.write_file_list("keyB.pri", b)
    self.write_file_list("keyA.pub", pointA)
    self.write_file_list("keyB.pub", pointB)

    print(a,b)
    print(pointA,pointB)

    
  def encoding(self, list_message):
    result = []
    for i in range(len(list_message)):
      for j in range(self._get_k()-1):
        x = (list_message[i] * self._get_k() + (j + 1))
        y = self.compute_ecc_equation(x)
        if y:
          point = Point()
          point._set_x(x)
          point._set_y(y[0]) 
          result.append(point)
    return result

  def decoding(self, list_message):
    result = []
    for i in range(len(list_message)):
      x = list_message[i]._get_x()
      message = math.floor((x-1)/self._get_k())
      result.append(message)
    return result
  
  def encrypt(self, filename, keyB_public, k):
    plaintext = self.read_file(filename)
    list_plaintext = list(plaintext)
    list_plain_int = list(map(int, plaintext))
    print(len(list_plain_int))

    key_pub = self.read_file_list(keyB_public)
    point_key_pub = Point()
    point_key_pub._set_x(key_pub[0])
    point_key_pub._set_y(key_pub[1])
    list_message_point = self.encoding(list_plain_int)

    
    process = PointOperatorECC(self._get_A(), self._get_B(), self._get_P())
    field = self.generate_galois_field()
    # Base point in galois field[0]
    base = field[0]

    for i in range(len(list_message_point)):
      print(list_message_point[i]._get_x(), list_message_point[i]._get_y())

    print("==============================================================")

    # K value, different from k for encoding
    kG = process.multiply(k, base)
    cipher = []
    cipher.append(kG._get_x())
    cipher.append(kG._get_y())
    for i in range(len(list_message_point)):
      msg_cipher = process.add(list_message_point[i], point_key_pub)
      cipher.append(msg_cipher._get_x())
      cipher.append(msg_cipher._get_y())
    
    regex = re.compile('.\w+').findall(filename)
    self.write_file_list("cipher_ecceg" + regex[-1], cipher)
    
  def decrypt(self, filename, keyB_private):
    ciphertext = self.read_file_list(filename)
    
    process = PointOperatorECC(self._get_A(), self._get_B(), self._get_P())

    key_pri = self.read_file_list(keyB_private)
    
    kG = Point()
    kG._set_x(ciphertext.pop(0))
    kG._set_y(ciphertext.pop(0))
    kGPub = process.multiply(key_pri, kG)
    
    i = 0
    list_plain_point = []
    while i <  len(ciphertext):
      point_cipher = Point()
      point_cipher._set_x(ciphertext[i])
      point_cipher._set_y(ciphertext[i+1])
      list_plain_point.append(process.minus(point_cipher, kGPub))
      i+=2
    
    for i in range(len(list_plain_point)):
      print(list_plain_point[i]._get_x(), list_plain_point[i]._get_y())

    list_plain_int = self.decoding(list_plain_point)
    regex = re.compile('.\w+').findall(filename)
    self.write_file_list("out_ecceg" + regex[-1], list_plain_int)
    

if __name__ == '__main__':
  ecceg = EllipticCurveCryptoElGamal(-1,188,751,5)
  field = ecceg.generate_galois_field()
  # keygen = ecceg.key_gen(20)
  result = ecceg.encrypt("plain.txt", "keyB.pub", 7)
  result = ecceg.decrypt("cipher_ecceg.txt", "keyB.pri")
  