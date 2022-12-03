str = "AAA BBB CCC"
count = 0
for sl in str.split(' '):
  k = 0
  for i in sl:
    if i == "A": k = k+1
  if k == 3: count = count + 1
