import cmath
import numpy
import matplotlib.pyplot as plot

class RootSolver():
    def __init__(self, f, fp, TOL=1.e-8):
        self.f = f
        self.fp = fp
        self.TOL = TOL

    def newton(self, z0):
        dz = f(z0)/fp(z0)
        print(dz)
        z = z0
        n = 200

        while abs(dz) > self.TOL:
            if n <= 0:
                return False
            z -= dz
            dz = f(z)/fp(z)
            n -= 1

        return z

    def create_and_populate_arr(self, domain, n=200):
        matx = numpy.zeros((n, n), dtype=complex)
        xmin, ymin, xmax, ymax = domain
        unit_size = (ymax-ymin)/n
        for i, row in enumerate(matx):
            for j, item in enumerate(row):
                matx[i][j] = xmin + unit_size*j + (xmax-i*unit_size)*1j
                print(item)

        return matx

    def root_index(self, roots, root):
        for i, item in enumerate(roots):
            if cmath.isclose(root, item, abs_tol=1.e-5):
                return i
        
        roots += [root]
        return len(roots) - 1
        


    def draw_fractal(self):
        matx = self.create_and_populate_arr((-1, -1, 1, 1))
        r = 0
        tx = ty = 0
        roots = []
        # Note: not good programming
        mx = numpy.zeros((200, 200))
        for i, row in enumerate(matx):
            for j, num in enumerate(row):
                r = self.newton(matx[i][j])
                if r is not False:
                    rindex = self.root_index(roots, r)
                    mx[i][j] = rindex

        plot.imshow(mx, cmap='twilight', origin='upper')
        plot.axis('off')
        plot.show()

        
                


if __name__ == "__main__":
    print("hello")
    f = lambda z: z**5 - 2*z + 10 
    fp = lambda z: 5*z**4 - 2 
    r = RootSolver(f, fp)
    r.draw_fractal()
