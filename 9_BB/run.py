# 6 possible states
# 2 values
# 2 moves
# 6*2*2 = 24
# 24^10 possible for sigma(5, 2)

# See Tree Normal Form from Bra66

#t0 = "B1L A1L C1R B1R A1L D1R A1L E1R H1L C0R".split(" ")
t0 = "B1L C1R C1L B1L D1L E0R A1R D1R H1L A0R".split(" ")

def run(t0, ms=-1):
  t = [0]*30000
  pos = 15000
  s = "A"

  cnt = 0
  halt = True
  while 1:
    assert pos > 0
    assert pos < len(t)
    #if cnt%1000 == 0:
    #  print(cnt, s, pos)
    ns = ord(s) - ord("A")
    if t[pos] == 0:
      tt = t0[ns*2+0]
    elif t[pos] == 1:
      tt = t0[ns*2+1]
    s = tt[0]
    t[pos] = int(tt[1])
    if tt[2] == "L":
      pos -= 1
    else:
      pos += 1
    cnt += 1
    if s == "H":
      break
    if ms != -1 and cnt > ms:
      halt = False
      break
  return halt, cnt, sum(t)

def draw(t0):
  import matplotlib.pyplot as plt
  import networkx as nx
  G = nx.DiGraph()

  for i,x in enumerate(t0):
    ts = chr(ord("A") + i//2)
    ns = x[0]
    lbl = str(i%2)+x[1:]
    G.add_edge(ts, ns, label=lbl)

  pos = nx.spring_layout(G)
  nx.draw_networkx(G, pos)
  edge_labels = nx.get_edge_attributes(G, 'label')
  nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels)
  plt.show()


if __name__ == "__main__":
  print(run(t0))
  #draw(t0)
'''
# https://sci-hub.tw/10.1109/PGEC.1966.264572
# Hmm, the tree normal form description is kind of annoying, it's a graph, right?
# Oh, "Attacking the Busy Beaver 5" has a clearer description
# Does the first move need to print a one?

# A0 = B1L looks like the default start in "Attacking the Busy Beaver 5"
# E0 | E1 = H1L is the final one

# They even seem to be reasoning about the machines while they generate them
# This is a little annoying as the function can only be computed in order

# Hmm https://arxiv.org/pdf/1610.03184.pdf

from run import run

# 4*2*2 = 16
# 16^6 possible for sigma(3, 2)

def gen(x,b=3):
  e = (b+1)*2*2
  ret = []
  for i in range(b*2):
    t = x%e
    ss = "L" if t%2 else "R"
    t //= 2
    ss = ("0" if t%2 else "1") + ss
    t //= 2
    if t==b:
      ss = "H" + ss
    else:
      ss = chr(ord("A") + t) + ss
    ret.append(ss)
    x //= e
  return ret

if __name__ == "__main__":
  b = 3
  all_s = 0
  all_sigma = 0
  for m in range(((b+1)*2*2)**(b*2)):
    mm = gen(m, b)
    halt, s, sigma = run(mm, ms=100)
    print(mm, halt, s, sigma, all_s, all_sigma)
    if halt:
      all_s = max(s, all_s)
      all_sigma = max(sigma, all_sigma)
 '''
