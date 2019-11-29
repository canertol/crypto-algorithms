


class ECC():
    def __init__(self, a=-1, b=188, p=751, P =(1,3)):
        self.a = a
        self.b = b
        self.p = p
        self.P = P
    def _mod_inverse(self, x):
        for k in range(self.p):
            if (k * x) % self.p == 1:
                return k

    def _lambda(self, P, Q):
        if P == Q:
            L = (3*P[0]*P[0] + self.a)*self._mod_inverse(2*P[1])
            L = L % self.p
        else:
            L = (Q[1]-P[1])*self._mod_inverse(Q[0]-P[0])
            L = L % self.p
        return L

    def addPQ(self, P, Q):
        L = self._lambda(P, Q)
        x3 = (L**2 - P[0] - Q[0]) % self.p
        y3 = (L*(P[0]-x3)-P[1]) % self.p
        return (x3, y3)

    def nP(self, n, P):
        t = P
        for _ in range(n-1):
            t = self.addPQ(P, t)
        return t

    def num_points(self):
        t = self.P
        counter=0
        while True:
            t = self.addPQ(self.P,t)
            counter += 1
            if self.P == t:
                break
        return counter

if __name__ == '__main__':
    a = int(input('a = '))
    b = int(input('b = '))
    p = int(input('p = '))
    P = (int(input('Px = ')),int(input('Py = ')))
    ecc = ECC(a, b, p, P)
    #if P is None:
    #    P = (0, 376)
    [print(n, ecc.nP(n, P)) for n in range(1,40)]

    #print(ecc.num_points())


