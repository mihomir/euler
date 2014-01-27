import eu

x=eu.fib()
print sum([_ for _ in list(eu.taketo(x,4*10**6)) if _ % 2 == 0])
