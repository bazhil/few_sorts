# Сортировка слиянием

# Сортировка называется устройчивой, если она не меняет порядок равных элементов.

first = [1, 2, 3, 4, 5]
second = [6, 7, 8, 9, 10]

# Слияние отсортированных массивов в один
def merge(A:list, B:list):
  C = [0] * (len(A) + len(B))
  i = k = n = 0
  while i < len(A) and k < len(B):
    if A[i] <= B[k]:
      C[n] = A[i]
      i += 1
      n += 1
    else:
      C[n] = B[k]
      k += 1
      n += 1
  while i < len(A):
    C[n] = A[i]
    i += 1
    n += 1
  while k < len(B):
    C[n] = B[k]
    k += 1
    n += 1
  return C
print(first, second)
print(merge(first, second))

third = [9, 4, 7, 2, 0, 8, 1, 6, 10, 3, 11, 5]

# Рекурентная сортировка слиянием
def merge_sort(A:list):
  if len(A) <= 1:
    return
  middle = len(A)//2
  L = [A[i] for i in range(0, middle)]
  R = [A[i] for i in range(middle, len(A))]
  merge_sort(L)
  merge_sort(R)
  C = merge(L, R)
  for i in range(len(A)):
    A[i] = C[i]
  return A

print(third)
print(merge_sort(third))

fourth =  [12, 9, 4, 7, 2, 0, 8, 1, 6, 10, 3, 11, 5]

# Сортировка Тони Хоара (Быстрая сортировка)
def hoar_sort(A:list):
  if len(A) <= 1:
    return
  barrier = A[0]
  L = []
  M = []
  R = []
  for x in A:
    if x < barrier:
      L.append(x)
    elif x == barrier:
      M.append(x)
    else:
      R.append(x)
  hoar_sort(L)
  hoar_sort(R)
  k = 0
  for x in L+M+R:
    A[k] = x
    k += 1
  return A

print(fourth)
print(hoar_sort(fourth))

# Проверка отсортированности массива
def check_sorted(A:list, ascending=True):
  """
  Проверка отсортированости за O(len(A))
  """
  flag = True
  s = 2 * int(ascending) - 1
  N = len(A)
  for i in range(0, N-1):
    if s*A[i] > s*A[i+1]:
      flag = False
      break
  return flag

print(check_sorted(fourth))
