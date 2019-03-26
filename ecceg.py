import random
import pickle
import array
import re
from base.general import is_prime
from point import Point

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
      # print(i)
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
    
  def encoding(self, list_message):
    list_message_int = list(map(int, list_message))
    # print("lent massage: ", len(list_message_int))
    result = []
    for i in range(len(list_message_int)):
      for j in range(self._get_k()-1):
        x = (list_message_int[i] * self._get_k() + (j + 1))
        y = self.compute_ecc_equation(x)
        if y:
          point = Point()
          point._set_x(x)
          point._set_y(y[0]) 
          result.append(point)
    return result

  def decoding(self, list_message):
    pass
  
  def encrypt(self, filename):
    plaintext = self.read_file(filename)
    list_plaintext = list(plaintext)
    list_plain_int = list(map(int, plaintext))
  
    return self.encoding(list_plain_int)

  def decrypt(self, filename, key_public, key_private):
    pass

if __name__ == '__main__':
  ecceg = EllipticCurveCryptoElGamal(-1,188,751,5)
  field = ecceg.generate_galois_field()
  result = ecceg.encrypt("plain.txt")
  for i in range(len(result)):
    print(result[i]._get_x(),result[i]._get_y())
  # p = Point()
  # p._set_x(2)
  # p._set_y(4)
  # if p in field:
  #   print('Ade brur')
  # print(ecceg.generate_pow_two())