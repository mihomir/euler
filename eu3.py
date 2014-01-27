import eu
from math import sqrt

gen = eu.prime_optimus()

primes = eu.taketo(gen,sqrt(600851475143))

print max([_ for _ in primes if 600851475143%_==0])
6857
