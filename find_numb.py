# An algorithm that finds the largest of 3 numbers\

# 3개의 숫자 중 가장 큰 숫자를 찾는 알고리즘

def numbers(a,b,c):
  if a >b:    # Agar 22 soni 133 dan katta bo'lsa
    if a>c: # Agar 22 soni 44 dan ham katta bo'lsa'
      return f'The number {a}  is the largest'
    else: # Agar 22 soni 44 dan  katta bo'lmasa'
      return f'The number {c}  is the largest'
  else: # Agar 22 soni 133 dan katta bo'lmasa
    if b>c:
      return f'The number {b}  is the largest'
    else:
      return f'The number {c}  is the largest'
print(numbers(22,133,44))              