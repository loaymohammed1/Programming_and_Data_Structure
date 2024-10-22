#!/usr/bin/python
def square_matrix_simple(matrix=[]):
 # إنشاء مصفوفة جديدة بنفس حجم المصفوفة الأصلية
   new_matrix = []
   for row in matrix:
       new_row = []
       for value in row:
           new_row.append(value ** 2)
        new_matrix.append(new_row)

      return new_matrix
  original_matrix = [[1, 2, 3], [4, 5, 6]]
  squared_matrix =square_matrix_simple(original_matrix)
  print( original_matrix)
  print(squared_matrix)
