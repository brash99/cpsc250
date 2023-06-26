class SimpleData:

    def __init__(self,x=1.0, y=3.0, dx=0.1, dy=0.3, name='First Data Point'):
      self.x = x
      self.y = y
      self.dx = dx
      self.dy = dy
      self.name = name

if __name__ == '__main__':

    data1 = SimpleData()
    print(data1.name, data1.x, data1.y, data1.dx, data1.dy)

    dy_new=0.112

    data2 = SimpleData(name='Second Data Point', dy=dy_new)
    print(data2.name, data2.x, data2.y, data2.dx, data2.dy)

