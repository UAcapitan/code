class DepartmentIT:
    PYTHON_DEV = 3
    GO_DEV = 1
    C_DEV = 2

    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.C_DEV)

    def info2(self):
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.C_DEV)

    @property
    def info3(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.C_DEV)

    @classmethod
    def info4(cls):
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.C_DEV)

    @staticmethod
    def info5():
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.C_DEV)

    def add_dev(self, n):
        if n == 'P':
            DepartmentIT.PYTHON_DEV += 1
        elif n == 'G':
            DepartmentIT.GO_DEV += 1
        elif n == 'C':
            DepartmentIT.C_DEV += 1

it1 = DepartmentIT()
it1.info()
it1.info2()
it1.info3
it1.info4()
it1.info5()
it1.add_dev('P')
print(DepartmentIT.__dict__)