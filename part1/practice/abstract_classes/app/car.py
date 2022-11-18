from part1.practice.abstract_classes.app.abc import Transport


class Car(Transport):
    def start_engine(self):
        print('Машина заурчала двигателем')

    def stop_engine(self):
        print('Машина стоит с заглушенным двигателем')

    def move(self):
        print('Машина едет к цели назначения')

    def stop(self):
        print('Машина остановилась')