import string as s
import random as r
print(r.randint(0, 10))
print(r.uniform(1, 100))
print(r.sample(range(0,10), 3))
print(s.ascii_letters)
passw = r.sample(s.ascii_letters, 6)
print(passw)
print("+".join(passw))
dig=r.sample(s.digits, 3)
print(dig)
print("+".join(dig)) 