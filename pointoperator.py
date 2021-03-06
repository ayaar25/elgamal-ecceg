import sys
from point import Point
from ecceg import EllipticCurveCryptoElGamal
from base.general import is_prime, inverse

class PointOperatorECC(object):

  def __init__(self, A, B, P):
    self.A = A
    self.B = B
    self.P = P

  def _get_A(self):
    return self.A
  
  def _get_B(self):
    return self.B
  
  def _get_P(self):
    return self.P
  
  def double_point(self, p):
    result = Point()

    if p._get_y() == 0:
      result._set_x(sys.maxsize)
      result._set_y(sys.maxsize)
    else:
      inv = inverse(2 * p._get_y(), self._get_P())
      lamda = ((3 * (p._get_x())**2 + self._get_A()) * inv) % self._get_P()
      lamda = int(lamda % self._get_P())
      # print(lamda)

      xr = (lamda**2 - (2 * p._get_x())) % self._get_P()
      # print(xr)
      yr = (lamda * (p._get_x() - xr) - p._get_y()) % self._get_P()
      # print(yr)

      result._set_x(int(xr))
      result._set_y(int(yr))
      
    return result

  def add(self, p1, p2):
    result = Point()

    if p1._get_x() == 0 and p1._get_y() == 0:
      result._set_x(p2._get_x())
      result._set_x(p2._get_y())
    elif p2._get_x() == 0 and p2._get_y() == 0:
      result._set_x(p1._get_x())
      result._set_x(p1._get_y())
    elif p1._get_y() - p2._get_y() == 0:
      result._set_x((0 - p1._get_x() - p2._get_x()) % self._get_P())
      result._set_x((0 - p1._get_x()) % self._get_P())
    elif p1._get_x() - p2._get_x() == 0:
      result._set_x(sys.maxsize)
      result._set_y(sys.maxsize)
    else:
      inv = inverse((p1._get_x() - p2._get_x()), self._get_P())
      lamda = ((p1._get_y() - p2._get_y()) * inv) % self._get_P()

      xr = (lamda**2 - p1._get_x() - p2._get_x()) % self._get_P()
      yr = (lamda*(p1._get_x()-xr)-p1._get_y()) % self._get_P()

      result._set_x(xr)
      result._set_y(yr)
    
    return result

if __name__ == '__main__':
  point = Point()
  point._set_x(2)
  point._set_y(4)
  # p1 = Point()
  # p1._set_x(2)
  # p1._set_y(4)
  # p2 = Point()
  # p2._set_x(5)
  # p2._set_y(9)
  op = PointOperatorECC(1,6,11)
  result = op.double_point(point)
  print(result._get_x(), result._get_y())  

  
