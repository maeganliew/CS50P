class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid Capacity")
        self._capacity = capacity
        self.size = 0   #initialising the size to 0

    def __str__(self):
        return (self.size * '🍪')

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError("Insufficient space")
        self._size +=  n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Too less cookies in jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size


def main():
    jar = Jar(15)
    jar.deposit(1)
    print(jar)


if __name__ == "__main__":
    main()