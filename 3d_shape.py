def string_match(a, b):
  x = 0
  z = len(a)
  y = len(b)
  if z == y:
    for i in range(z):
      if a[i] == b[i]:
        x += 1
    return x
  else:
    return "Different length"
print(string_match("abacadaba","abacadaba"))