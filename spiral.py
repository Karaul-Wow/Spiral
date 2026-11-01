import math

def get_spiral(matrix) -> list[int]:
    """
    Обход прямоугольной матрицы по спирали против часовой стрелки начиная с левого-верхненго угла.
    Сохранение последовательности членов матрицы по ходу обхода в список
    """
    lst_out = []  # список-результат
    x_max = len(matrix[0]) - 1  # последний индекс столбца (горизонталь)
    y_max = len(matrix) - 1     # последний индекс строки (вертикаль)
    i = 1                       # номер витка
    c_0 = i - 1                 # текущая левая и верхняя граница (индекс)
    x_1 = x_max + 1 - i         # текущая правая граница (индекс столбца)
    y_1 = y_max + 1 - i         # текущая нижняя граница (индекс строки)
    while c_0 <= x_1 and c_0 <= y_1:      
      lst_top = []              # инвертированный список верхней строны спирали
      lst_bottom = []           # список нижней строны спирали
      lst_left = []             # список левой строны спирали
      lst_right = []            # инвертированный список правой строны спирали
      for j in range(c_0, y_1 + 1):
        lst_left.append(matrix[j][c_0])
        if c_0 != x_1: lst_right.append(matrix[j][x_1])
      if c_0 != y_1: lst_top = matrix[c_0][c_0 + 1: x_1:]
      lst_bottom = matrix[y_1][c_0 + 1: x_1:]
      lst_out = lst_out + lst_left + lst_bottom + lst_right[:: -1] + lst_top[:: -1]
      i += 1
      c_0 = i - 1
      x_1 = x_max + 1 - i
      y_1 = y_max + 1 - i
    return lst_out;



if __name__ == "__main__":

  matrix_in = [[]]
  
  list_out = get_spiral(matrix_in )
  print (list_out)

  matrix_in = [[10]]

  list_out = get_spiral(matrix_in )
  print (list_out)

  matrix_in = [[10, 20, 30, 40, 50], 
              [60, 70, 80, 90, 100],
              [110, 120, 130, 140, 150],
              [160, 170, 180, 190, 200],
              [210, 220, 230, 240, 250]]

  list_out = get_spiral(matrix_in )
  print (list_out)

  matrix_in = [[10, 20, 30, 40], 
              [50, 60, 70, 80],
              [90, 100, 110, 120],
              [130, 140, 150, 160],
              [170, 180, 190, 200]]

  list_out = get_spiral(matrix_in )
  print (list_out)

  matrix_in = [[10, 20, 30, 40, 50], 
              [60, 70, 80, 90, 100],
              [110, 120, 130, 140, 150],
              [160, 170, 180, 190, 200]]

  list_out = get_spiral(matrix_in )
  print (list_out)

  matrix_in = [[10, 20, 30, 40], 
              [50, 60, 70, 80],
              [90, 100, 110, 120],
              [130, 140, 150, 160],
              [170, 180, 190, 200],
              [210, 220, 230, 240]]

  list_out = get_spiral(matrix_in )
  print (list_out)