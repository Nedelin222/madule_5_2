class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        i = 0
        print(self.name, self.number_of_floors)
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f"Такого этажа не существует")
        else:
            for i in range(new_floor):
                print(i + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, Количество этажей: {self.number_of_floors} ')

open_spaces = House("ЖК Просторы", 20)
parking = House("Парковка", 4)
print(str(open_spaces))
print(len(open_spaces))
print(str(parking))
print(len(parking))


# open_spaces.go_to(5)
# parking.go_to(-5)
# parking.go_to(0)