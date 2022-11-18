from part1.practice.abstract_classes.app.abc import Transport


class Person:

    def use_transport(self, transport: Transport):
        transport.start_engine()
        transport.move()
        transport.stop()
        transport.stop_engine()