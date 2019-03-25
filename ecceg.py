import random
import pickle
import array
import re
from base.general import is_prime

class EllipticCurveCryptoElGamal(object):

  def __init__(self, A, B, P):
    # ECC Equation Constanta, y^2 mod P = x^3 + Ax + B mod P
    self.A = A
    self.B = B
    self.P = P
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
    
  def compute_ecc_equation(self, k, point):
    pass
    
  def encoding(self, list_message):
    pass

  def decoding(self, list_message):
    pass
  
  def encrypt(self, filename, key_public, key_private):
    pass

  def decrypt(self, filename, key_public, key_private):
    pass