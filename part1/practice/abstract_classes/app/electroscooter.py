from part1.practice.abstract_classes.app.abc import Transport


class Electroscooter(Transport):
    def start_engine(self):
        print('Мигнул светодиодом')

    def stop_engine(self):
        print('Мигнул светодиодом дважды')

    def move(self):
        print('Прохожие в ужасе разбегаются от очередного камикадзе')

    def stop(self):
        print('Торможение об стену прошло успешно')