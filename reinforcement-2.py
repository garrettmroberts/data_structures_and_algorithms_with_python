from random import randint, random

# 2.4
class Flower:
    def __init__(self, name: str, petals: int, price: float):
        self.set_name(name)
        self.set_petals(petals)
        self.set_price(price)

    def set_name(self, name):
        self.name = name
    
    def get_name(self, name):
        return self.name
    
    def set_petals(self, petals):
        self.petals = petals
    
    def get_petals(self, petals):
        return self.petals

    def set_price(self, price):
        self.price = price
    
    def get_price(self, price):
        return self.price

#2.5
class CreditCard():
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
        
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._account
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance
    
    def set_balance(self, value):
        self._balance = value
          
    def charge(self, price):
        try:
            price = float(price)
        except:
            print ('Invalid input')
            return False       
        if price + self._balance > self._limit:
            print(f'Your deposit of {price} exceeds your remainder of {self.get_limit() - self.get_balance()}')
            return False #You are going over your limit
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        try:
            amount = float(amount)
        except:
            print ('Invalid input')
            return False 
        self._balance -= amount
        return True
    
#2.6
class CreditCard():
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
        
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._account
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance
    
    def set_balance(self, value):
        self._balance = value
          
    def charge(self, price):
        try:
            price = float(price)
        except:
            print ('Invalid input')
            return False       
        if price + self._balance > self._limit:
            print(f'Your deposit of {price} exceeds your remainder of {self.get_limit() - self.get_balance()}')
            return False #You are going over your limit
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        try:
            amount = float(amount)
        except:
            print ('Invalid input')
            return False 
        if amount < 0:
            raise ValueError('Negative input detected. Enter a positive number.')
        else:
            self._balance -= amount
        return True

# 2.7
class CreditCardWithBalance(CreditCard):
    def __init__(self, customer, bank, acnt, limit, balance=0):
        super().__init__(self, customer, bank, acnt, limit)
        self._balance = balance

# 2.9, 2.10, 2.12, 2.13
class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:                                  
            try:                                     # we test if param is iterable
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):          # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other             # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation


    def __lt__(self, other):
        """Compare vectors based on lexicographical order."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords < other._coords

    def __le__(self, other):
        """Compare vectors based on lexicographical order."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords <= other._coords
    
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Vectors must be of the same size.')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    
    def __neg__(self):
        res = Vector(len(self))
        for j in range(len(self)):
            res[j] = -self[j]
        return res
    
    def __mul__(self, value):
        res = Vector(len(self))
        for j in range(len(self)):
            res[j] = self[j] * value
        return res
    
    def __rmul__(self, value):
        return self * value
    
# 2.36
class RiverEcosystem():

    class Bear():
        def __init__(self, location):
            self._location = location

    class Fish():
        def __init__(self, location):
            self._location = location
    
    MOVE_CHANCE = 0.3
    LR_CHANCE = 0.5

    def __init__(self, ecosystem_length=40, bears=3, fish=10):
        self._ecosystem = [None] * ecosystem_length
        self._bears = self.populate_animal(self.Bear, bears)
        self._fish = self.populate_animal(self.Fish, fish)
    
    def __len__(self):
        return len(self._ecosystem)
    
    def __getitem__(self, idx):
        return self._ecosystem[idx]
    
    def __setitem__(self, idx, item):
        self._ecosystem[idx] = item

    def __repr__(self):
        printable_view = []
        for element in self._ecosystem:
            if isinstance(element, self.Bear):
                printable_view.append('B')
            elif isinstance(element, self.Fish):
                printable_view.append('F')
            else:
                printable_view.append('-')
        return str(printable_view)
    
    def populate_animal(self, type, count):
        assigned = 0
        item_list = []
        attempts = 0
        maxAttempts = 100
        while assigned < count and attempts <= maxAttempts:
            attempts += 1
            rand = randint(0, len(self) - 1)
            if self[rand] == None:
                assigned += 1
                new_animal = type(rand)
                self[rand] = new_animal
                item_list.append(new_animal)
        return item_list
    
    def time_step(self):
        for b in self._bears:
            self._determine_action(b)
        for f in self._fish:
            self._determine_action(f)

    def _determine_action(self, obj):
        if random() < self.MOVE_CHANCE:
            if (random() < self.LR_CHANCE):
                self.attempt_move(obj, obj._location - 1)
            else:
                self.attempt_move(obj, obj._location + 1)
    
    def _delete_item(self, obj, list):
        target = None
        for i in range(len(list)):
            if obj is list[i]:
                target = i
        if target is not None: del (list[target])
    
    def attempt_move(self, obj, target_location):
        if target_location < 0 or target_location >= len(self):
            return False
        elif self[target_location] == None:
            self[target_location], self[obj._location] = self[obj._location], self[target_location]
        elif type(obj) == type(self[target_location]):
            self.populate_animal(type(obj), 1)
        elif isinstance(obj, self.Fish):
            self._delete_item(obj, self._fish)
        elif isinstance(self[target_location], self.Fish):
            self._delete_item(self[target_location], self._fish)
            

    


river = RiverEcosystem()
for i in range(40):
    print(river)
    river.time_step()