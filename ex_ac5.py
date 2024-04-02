from abc import ABC, abstractmethod

class A(ABC):
    def metodo_m(self):
        pass

    @abstractmethod
    def metodo_n(self):
        pass

class B(A):
    def metodo_o():
        pass

x = B()

