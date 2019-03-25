import random
import pickle
import array
import re
from base.general import is_prime
from point import Point

class EllipticCurveCryptoElGamal(object):

  def __init__(self, A, B, P):
    # ECC Equation Constanta, y^2 mod P = x^3 + Ax + B mod P
    self.A = A
    self.B = B
    self.P = P
    pass
  
  def _get_A(self):
    return self.A
  
  def _get_B(self):
    return self.B
  
  def _get_P(self):
    return self.P

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
      print(i)
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
    pass

  def decoding(self, list_message):
    pass
  
  def encrypt(self, filename, key_public, key_private):
    pass

  def decrypt(self, filename, key_public, key_private):
    pass

if __name__ == '__main__':
  ecceg = EllipticCurveCryptoElGamal(1,12,11)
  field = ecceg.generate_galois_field()
  for i in range(len(field)):
    print(field[i]._get_x(),field[i]._get_y())
  # print(ecceg.generate_pow_two())