from part1.practice.abstract_classes.app.abc import Transport


class Boat(Transport):
    def start_engine(self):
        print('Катер громко затарахтел')

    def stop_engine(self):
        print('Двигатель катера чихнул напоследок и заглох')

    def move(self):
        print('Катер быстро набирает скорость')

    def stop(self):
        print('Катер остановился')