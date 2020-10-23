import time


class TrafficLight:

    __color = 'Off'
    __color_count = 0

    def running(self):
        colors = ['red', 'yellow', 'green']
        timers = [7, 2, 5]
        TrafficLight.__color = colors[TrafficLight.__color_count]
        print(TrafficLight.__color)
        time.sleep(timers[TrafficLight.__color_count])
        TrafficLight.__color_count += 1
        if TrafficLight.__color_count == 3:
            TrafficLight.__color_count = 0

    def off(self):
        TrafficLight.__color = 'Off'
        TrafficLight.__color_count = 0


a = TrafficLight()
a.running()
a.running()
a.running()
a.running()
a.off()

b = TrafficLight()
b.running()
b.running()
a.off()
