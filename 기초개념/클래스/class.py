class Car(object):
    def __init__(self, name):
        self.kinds = []
        self.kinds.append(name)
    maxSpeed = 300
    maxPeople = 5
    def move(self, x):
        print(x, '의 스피드로 움직이고 있습니다.')
    def stop(self):
        print('멈췄습니다.')
    def __getattr__(self, miss):
        print(miss + "속성은 없습니다.")

class Maxwheel(object):
    wheel = 19
class Minwheel(object):
    wheel = 15
class LargeCar(Car, Maxwheel):
    pass
#다중 상속
class LargeCar(Car, Maxwheel):
    pass
#클래스 상속
class HybridCar(Car):
    battery = 1000
    batteryKM = 300
    
k5 = Car('k5') #instance
k3 = Car('k3') #instance
hybrid_k5 = HybridCar('Hybrid_k5')

'''
k5.move(10)
k5.stop()
k3.move(5)
k3.stop()
print(k5.kinds)
print(k5.MaxSpeed)
print(k3.MaxSpeed)
'''

print(hybrid_k5.battery)
print(hybrid_k5.maxSpeed)
print(hybrid_k5.maxmaxSpeed)