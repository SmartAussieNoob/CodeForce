l = []
N = int(input())
word_idx = 0
for i in range(N):
   word = str(input())
   if len(word) <= 10:
      l.append(word)
   else:
      sym_list = list(word)
      t = "".join( sym_list[:1] + [str(len(word) - 2)] + sym_list[-1:])
      l.append(t)
for i in l:
    print(i)
