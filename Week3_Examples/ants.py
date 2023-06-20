import random

N = 1000
nsims = 10000

t_total_max = 0
t_total_min = 0

for i in range(nsims):
    t_max = 0
    t_min = 1.0
    for j in range(N):
        x = random.random()
        d = random.randint(1,2)
        if d == 1:
            dist = 1 - x
        else:
            dist = x
        t = dist
        if (t>t_max):
            t_max = t
        if (t<t_min):
            t_min = t
    t_total_max += t_max
    t_total_min += t_min

t_avg_max = t_total_max/nsims
t_avg_min = t_total_min/nsims

print(t_avg_max, t_avg_min)