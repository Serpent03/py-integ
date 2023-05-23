class Vector3():
    def __init__(self, x, y, z) -> 'Vector3':
        self.x = x
        self.y = y
        self.z = z

    def mag(self) -> 'float':
        return ((self.x)**2 + (self.y)**2 + (self.z)**2) ** 0.5

    @staticmethod
    def addVector(v1, v2) -> 'Vector3':
        return Vector3(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)
    
    @staticmethod
    def subVector(v1, v2) -> 'Vector3':
        return Vector3(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)

    @staticmethod
    def mulVector(v1, mag) -> 'Vector3':
        return Vector3(v1.x * mag, v1.y * mag, v1.z * mag)
    
    @staticmethod
    def magnitudeOf(vector1) -> float:
        print(vector1.x)
        return ((vector1.x)**2 + (vector1.y)**2 + (vector1.z)**2) ** 0.5

    def get(self):
        return (f'[{self.x}, {self.y}, {self.z}]')

    def printVector(self):
        print(f'[{self.x}, {self.y}, {self.z}]')


class stateVector():
    def __init__(self):
        self.vdot = Vector3(0, 0, 0)
        self.v = Vector3(0, 0, 0)
        self.p = Vector3(0, 0, 0)

    def setP(self, x, y, z):
        self.p = Vector3(x, y, z)

    def setV(self, x, y, z):
        self.v = Vector3(x, y, z)

    def setVDot(self, x, y, z):
        self.vdot = Vector3(x, y, z)

    def intg(self, delta):
        self.v = Vector3.addVector(
            self.v,
            Vector3.mulVector(self.vdot, delta)
        ) 

        self.p = Vector3.addVector(
            self.p,
            Vector3.mulVector(self.v, delta)
        )
        self.p = Vector3.addVector(
            self.p,
            Vector3.mulVector(self.vdot, 0.5*delta**2)
        )

    def printSV(self):
        print(f'P: {self.p.get()}\nV: {self.v.get()}\nA: {self.vdot.get()}')

sv = stateVector()
sv.printSV()
