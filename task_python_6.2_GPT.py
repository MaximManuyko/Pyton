class Tomato:
    states = {'Отсутствует': 0, 'Цветение': 1, 'Зеленый': 2, 'Красный': 3}
    
    def __init__(self, index):
        self._index = index
        self._state = self.states['Отсутствует']
        print(f'Создан новый объект Tomato с индексом {index} и состоянием "Отсутствует"')

    def grow(self):
        if self._state < 3:
            self._state += 1
        print(f'Томат с индексом {self._index} вырос до состояния "{list(self.states.keys())[self._state]}"')

    def is_ripe(self):
        ripe = self._state == 3
        print(f'Томат с индексом {self._index} созрел: {ripe}')
        return ripe
        
class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = []
        for i in range(num_tomatoes):
            self.tomatoes.append(Tomato(i))
        print(f'Создан новый объект TomatoBush с {num_tomatoes} помидорами')

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
        print('Все помидоры на кусте выросли на один шаг')

    def all_are_ripe(self):
        all_ripe = all([tomato.is_ripe() for tomato in self.tomatoes])
        print(f'Все помидоры на кусте созрели: {all_ripe}')
        return all_ripe
    
    def give_away_all(self):
        self.tomatoes.clear()
        print('Все помидоры на кусте были собраны')
        
class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
        print(f'Создан новый объект Gardener с именем {name}')

    def work(self):
        self._plant.grow_all()
        print(f'{self.name} сделал шаг в работе с кустом помидоров')

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print(f'{self.name} собрал урожай!')
        else:
            print('Некоторые плоды еще не созрели!')

    @staticmethod
    def knowledge_base():
        print('Время сбора урожая томатов в идеале должно приходиться на период, когда плод зрелый зеленый и затем дают созреть на лозе.') 
        print('Это предотвращает расщепление или синяки и позволяет в некоторой степени контролировать процесс созревания.')


Gardener.knowledge_base()
great_tomato_bush = TomatoBush(4)
gardener = Gardener('Emilio', great_tomato_bush)
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()