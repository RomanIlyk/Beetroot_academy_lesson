class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    @property
    def get_workers(self):
        return self.workers

    def add_worker(self, worker):
        self.workers.append(worker)

    def __str__(self):
        return (f'id: {self.id}, name: {self.name}')

    def __repr__(self):
        return Boss.__str__(self)

class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    @property
    def get_boss(self):
        return self.boss

    @get_boss.setter
    def get_boss(self, boss: Boss) -> None:
        if isinstance(boss, Boss):
            self.boss = boss
            boss.workers.append(self)
        else:
            raise TypeError('Not an instance of Boss class')

    def __str__(self):
        return (f'id: {self.id}, name: {self.name}')

    def __repr__(self):
        return Worker.__str__(self)


boss1 = Boss(1, 'Kiril', 'Mass')
boss2 = Boss(2, 'Andrew', 'Kolins')

worker1 = Worker(1, 'Olia', 'Mass', boss1)
worker2 = Worker(2, 'Anton', 'Mass', boss1)
worker3 = Worker(3, 'Nikita', 'Mass', boss1)
worker4 = Worker(4, 'Natalia', 'Kolins',boss2)
worker5 = Worker(5, 'Igor', 'Kolins',boss2)

boss1.add_worker(worker1)
boss1.add_worker(worker2)
boss1.add_worker(worker3)
boss2.add_worker(worker4)
boss2.add_worker(worker5)
print(boss2.name)
print(f'Boss {boss1.name}  workers: {boss1.get_workers}')
print(f'Boss {boss2.name}  workers: {boss2.get_workers}')


