import argparse

class NotOddDegreeException(Exception):
    def __init__(self, text):
        self.txt = text


class DegreeIsTooBigException(Exception):
    def __init__(self, text):
        self.txt = text


eps = 1e-7


class Polynomial:

    def __init__(self, *poli):

        if len(poli) == 1:
            poli = poli[0]
            if isinstance(poli, list):
                self.poli = poli
            elif isinstance(poli, dict):
                mm = max(poli.keys()) + 1
                self.poli = []
                for i in range(mm):
                    if i in poli.keys():
                        self.poli.append(poli[i])
                    else:
                        self.poli.append(0)
            elif isinstance(poli, Polynomial):
                self.poli = poli.poli
            else:
                self.poli = [poli]
        else:
            self.poli = list(poli)
        if len(self.poli) > 1:
            while self.poli[-1] == 0 and len(self.poli) > 1:
                self.poli.pop(-1)

    def __str__(self):

        new_text = ""
        mm = len(self.poli)
        if mm > 1:
            for ind, coef in enumerate(self.poli[-1::-1]):
                if coef != 0:
                    ind = mm - ind - 1
                    if coef < 0 and ind == mm - 1:
                        sign = "-"
                    elif coef < 0:
                        sign = " - "
                    elif coef > 0 and ind != mm - 1:
                        sign = " + "
                    else:
                        sign = ""

                    if ind != 0 and abs(coef) != 1 and ind != 1:
                        temp = "%s%sx^%s" % (sign, abs(coef), ind)
                    elif abs(coef) == 1 and ind != 0 and ind != 1:
                        temp = "%sx^%s" % (sign, ind)
                    elif ind == 1 and abs(coef) != 1:
                        temp = "%s%sx" % (sign, abs(coef))
                    elif abs(coef) == 1 and ind == 0:
                        temp = "%s%s" % (sign, abs(coef))
                    elif abs(coef) != 1 and ind == 0:
                        temp = "%s%s" % (sign, abs(coef))
                    elif abs(coef) == 1 and ind == 1:
                        temp = "%sx" % (sign)
                    new_text += temp
        else:
            new_text = str(self.poli[0])
        return new_text

    def __repr__(self):
        return "Polynomial " + str(self.poli)

    def degree(self):
        return len(self.poli) - 1

    def __eq__(self, other):
        if self.degree() > 0:
            if self.poli == other.poli:
                return True
            else:
                return False
        else:
            if isinstance(other, int):
                if other == self.poli[0]:
                    return True
                else:
                    return False
            elif isinstance(other, Polynomial):
                if other.poli[0] == self.poli[0]:
                    return True
                else:
                    return False

    def __add__(self, other):
        if isinstance(other, Polynomial):
            degg = max(len(other.poli), len(self.poli))
            new = [0] * degg
            for i in range(len(new)):
                if i < len(self.poli):
                    new[i] += self.poli[i]
                if i < len(other.poli):
                    new[i] += other.poli[i]
        elif isinstance(other, int):
            new = self.poli.copy()
            new[0] += other
        return Polynomial(new)

    def __radd__(self, other):
        if isinstance(other, Polynomial):
            degg = max(len(other.poli), len(self.poli))
            new = [0] * degg
            for i in range(len(new)):
                if i < len(self.poli):
                    new[i] += self.poli[i]
                if i < len(other.poli):
                    new[i] += other.poli[i]
        elif isinstance(other, int):
            new = self.poli.copy()
            new[0] += other
        return Polynomial(new)

    def __neg__(self):
        new = self.poli.copy()
        for i in range(len(new)):
            new[i] *= -1
        return Polynomial(new)

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            degg = max(len(other.poli), len(self.poli))
            new = [0] * degg
            for i in range(len(new)):
                if i < len(self.poli):
                    new[i] += self.poli[i]
                if i < len(other.poli):
                    new[i] -= other.poli[i]
        elif isinstance(other, int):
            new = self.poli.copy()
            new[0] -= other
        return Polynomial(new)

    def __rsub__(self, other):
        if isinstance(other, Polynomial):
            degg = max(len(other.poli), len(self.poli))
            new = [0] * degg
            for i in range(len(new)):
                if i < len(self.poli):
                    new[i] += self.poli[i]
                if i < len(other.poli):
                    new[i] -= other.poli[i]
        elif isinstance(other, int):
            new = self.poli.copy()
            for i in range(len(new)):
                new[i] *= -1
            new[0] += other
        return Polynomial(new)

    def __call__(self, x):
        value = 0
        for ind, coef in enumerate(self.poli):
            value += self.poli[ind] * (x ** ind)
        return value

    def der(self, d=1):
        new = self.poli.copy()
        for j in range(d):
            if len(new) > 1:
                for i in range(len(new)):
                    new[i] *= (i)
                new.pop(0)
            else:
                new = [0]
        return Polynomial(new)

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            degg = len(other.poli) + len(self.poli) - 1
            new = [0] * degg
            for i in range(len(self.poli)):
                for j in range(len(other.poli)):
                    new[i + j] += self.poli[i] * other.poli[j]
        elif isinstance(other, int):
            new = self.poli.copy()
            for i in range(len(new)):
                new[i] *= other
        return Polynomial(new)

    def __rmul__(self, other):
        if isinstance(other, Polynomial):
            degg = len(other.poli) + len(self.poli) - 1
            new = [0] * degg
            for i in range(len(self.poli)):
                for j in range(len(other.poli)):
                    new[i + j] += self.poli[i] * other.poli[j]
        elif isinstance(other, int):
            new = self.poli.copy()
            for i in range(len(new)):
                new[i] *= other
        return Polynomial(new)
    
    def __mod__(self, other):
        x1 = self.poli.copy()
        x2 = other.poli.copy()
        
        while len(x1) >= len(x2):
            k = x1[-1]/x2[-1]
            for i in range(len(x2)):
                x1[-1 - i] = x1[-1 - i] - x2[-1 - i]*k
            x1.pop(-1)
        
        return Polynomial(x1)
        
    def __truediv__(self, other):
        x1 = self.poli.copy()
        x2 = other.poli.copy()
        new = []
        while len(x1) >= len(x2):
            k = x1[-1]/x2[-1]
            for i in range(len(x2)):
                x1[-1 - i] = x1[-1 - i] - x2[-1 - i]*k
            x1.pop(-1)
            new.append(k)
        
        return (Polynomial(new[::-1]), Polynomial(x1))
    
    def gcd(self, other):
        x1 = self.poli.copy()
        x2 = other.poli.copy()
        buffer = []
        if len(x1) < len(x2):
            buffer = x1.copy()
            x1 = x2.copy()
            x2 = buffer.copy()
        if (self % other).poli != [0.0]:
            for i in range(len(x1)):
                    x1[i] /= x1[-1]  
            for i in range(len(x2)):
                    x2[i] /= x2[-1] 
        while (len(x1) > 1  ) and\
              (len(x2) > 1   ) :
             
            p1 = Polynomial(x1)
            p2 = Polynomial(x2)
            temp = (p1 % p2)#.poli.copy()
            print(temp)
            temp = temp.poli.copy()
            x1 = x2.copy()
            x2 = temp.copy()
            if x2[-1] != 0:
                for i in range(len(x2)):
                    x2[i] /= x2[-1]   
        return Polynomial(x1)
        
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.poli):
            x = self.n
            self.n += 1
            return (x, self.poli[x])
        else:
            raise StopIteration


class RealPolynomial(Polynomial):

    def __init__(self, *poli):
        if isinstance(poli, tuple) and len(poli) == 1:
            poli = poli[0]
            if isinstance(poli, Polynomial):
                poli = poli.poli
            elif isinstance(poli, int):
                poli = [poli]
        elif isinstance(poli, tuple) and len(poli) > 1:
            poli = list(poli)

        if len(poli) > 1:
            while poli[-1] == 0 and len(poli) > 1:
                poli.pop(-1)
        if len(poli) % 2 == 0:
            super().__init__(*poli)
        else:
            raise NotOddDegreeException("NotOddDegreeException")

    def find_root(self):
        gr = self.poli[-1]
        if gr != 1:
            new = [i / gr for i in self.poli]
        else:
            new = self.poli.copy()
        temp_poli = RealPolynomial(new)
        x_left = -1
        y_left = temp_poli(x_left)
        if y_left > 0:
            x_right = x_left
            y_right = y_left
            while y_left > 0:
                x_left *= 2
                y_left = temp_poli(x_left)
        elif y_left < 0:
            x_right = 1
            y_right = temp_poli(x_right)
            while y_right < 0:
                x_right *= 2
                y_right = temp_poli(x_right)
        else:
            return x_left

        x_search = (x_left + x_right) / 2
        step = (x_right - x_left) / 2
        y_search = temp_poli(x_search)
        while abs(y_search) > eps / 10:
            if y_search > 0:
                x_search -= step

            else:
                x_search += step
            y_search = temp_poli(x_search)
            step /= 2

        return x_search

    def der(self, d=2):
        if d % 2 == 1:
            raise NotOddDegreeException("NotOddDegreeException")
        else:
            y = Polynomial(self.poli)
            y = y.der(d)
            return RealPolynomial(y)

    def __add__(self, other):
        x1 = Polynomial(self)
        x2 = Polynomial(other)
        return RealPolynomial(x1 + x2)

    def __radd__(self, other):
        x1 = Polynomial(self)
        x2 = Polynomial(other)
        return RealPolynomial(x1 + x2)

    def __sub__(self, other):
        x1 = Polynomial(self)
        x2 = Polynomial(other)
        return RealPolynomial(x1 - x2)

    def __rsub__(self, other):
        x1 = Polynomial(self)
        x2 = Polynomial(other)
        return RealPolynomial(x1 - x2)

    def __mul__(self, other):
        x1 = Polynomial(self)
        x2 = Polynomial(other)
        return RealPolynomial(x1 * x2)

    def __rmul__(self, other):
        x1 = Polynomial(self)
        x2 = Polynomial(other)
        return RealPolynomial(x1 * x2)

    def __repr__(self):
        return "RealPolynomial " + str(self.poli)


class QuadraticPolynomial(Polynomial):

    def __init__(self, *poli):
        if isinstance(poli, tuple) and len(poli) == 1:
            poli = poli[0]
            if isinstance(poli, Polynomial):
                poli = poli.poli
            elif isinstance(poli, int):
                poli = [poli]
        elif isinstance(poli, tuple) and len(poli) > 1:
            poli = list(poli)
        if len(poli) > 1:
            while poli[-1] == 0 and len(poli) > 1:
                poli.pop(-1)
        if len(poli) <= 3:
            super().__init__(*poli)
        else:
            raise DegreeIsTooBigException("DegreeIsTooBigException")

    def solve(self):
        if self.degree() == 0:
            if self.poli[0] == 0:
                return ["Any"]
            else:
                return []
        elif self.degree() == 1:
            return [(-self.poli[0] / self.poli[1])]
        elif self.degree() == 2:
            d = self.poli[1] ** 2 - 4 * self.poli[2] * self.poli[0]
            if d > 0:
                x1 = (-self.poli[1] + d ** 0.5) / (2 * self.poli[2])
                x2 = (-self.poli[1] - d ** 0.5) / (2 * self.poli[2])
                return [x1, x2]
            elif d == 0:
                x = -self.poli[1] / (2 * self.poli[2])
                return [x]
            else:
                return []

    def __add__(self, other):
        x1 = Polynomial(self)
        x2 = Polynomial(other)
        return QuadraticPolynomial(x1 + x2)

    def __radd__(self, other):
        x1 = Polynomial(self)
        x2 = Polynomial(other)
        return QuadraticPolynomial(x1 + x2)

    def __sub__(self, other):
        x1 = Polynomial(self)
        x2 = Polynomial(other)
        return QuadraticPolynomial(x1 - x2)

    def __rsub__(self, other):
        x1 = Polynomial(self)
        x2 = Polynomial(other)
        return QuadraticPolynomial(x1 - x2)

    def __mul__(self, other):
        x1 = Polynomial(self)
        x2 = Polynomial(other)
        return QuadraticPolynomial(x1 * x2)

    def __rmul__(self, other):
        x1 = Polynomial(self)
        x2 = Polynomial(other)
        return QuadraticPolynomial(x1 * x2)       

    def __repr__(self):
        return "QuadraticPolynomial " + str(self.poli)





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", type=str,
                        help='''enter your opertion to use

1) multiply -- to multiply polynomials (--lhs and --rhs MUST be entered)

2) derrivative -- to calculate derivitive (--lhs and --degree MUST be entered

3) solve-quadratic -- to calculate root of the square polynomial (--lhs MUST be entered)

    ATTENTION: N - MUST be less or equal 2
    
4) find-root -- to calculate root of the odd degree polynomial

    ATTENTION: N - MUST be odd
''')
    parser.add_argument("--lhs",nargs='*', type=int,
                        help="first polynomial")
    parser.add_argument("--rhs", nargs='*', type=int,
                        help="second polynomial")
    parser.add_argument("--degree", type=int,
                        help="degree need derrivative")
    parser.add_argument("--eps", type=int,
                        help="eps need for find-root")
    args = parser.parse_args()

    if args.command == "multiply":
        x1 = Polynomial(args.lhs)
        x2 = Polynomial(args.rhs)
        print(x1 * x2)
    elif args.command == "derrivative":
        x = Polynomial(args.lhs)
        print(x.der(args.degree))
    elif args.command == "solve-quadratic":
        x = QuadraticPolynomial(args.lhs)
        print(x.solve())
    elif  args.command == "find-root":
        x = RealPolynomial(args.lhs)
        print(x.find_root())