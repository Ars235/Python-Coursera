import os
import re
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand if brand != '' else -1
        self.photo_file_name = photo_file_name if photo_file_name != '' and os.path.splitext(photo_file_name)[1] != '' and os.path.splitext(os.path.splitext(photo_file_name)[0])[1] == ''  else -1
        try:
            self.carrying = float(carrying)
        except ValueError:
            self.carrying = -1
    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.passenger_seats_count = int(passenger_seats_count)
        except ValueError:
            self.passenger_seats_count = -1
        self.car_type = 'car'

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        self.car_type = 'truck'
        params = self._whl()
        try:
            self.body_length = params[0]
        except IndexError:
            self.body_length = 0.0
        try:
            self.body_width = params[1]
        except IndexError:
            self.body_width = 0.0
        try:
            self.body_height = params[2]
        except IndexError:
            self.body_height = 0.0
    def _whl(self):
        params = re.findall(r'\d*\.\d+|\d+', self.body_whl)
        if len(params) == 3:
            for i in range(len(params)):
                try:
                    params[i] = float(params[i])
                except ValueError:
                    pass
            return params
        else:
            return [0.0, 0.0, 0.0]
    def get_body_volume(self):
        return self.body_length*self.body_width*self.body_height

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra if extra != '' else -1

def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ';')
        i = 0
        for line in csv_reader:
            if 'car' == line['car_type']:
                car = Car(line['brand'], line['photo_file_name'], line['carrying'], line['passenger_seats_count'])
                if car.carrying == -1 or car.brand == -1 or car.photo_file_name == -1 or car.passenger_seats_count == -1:
                    continue
                car_list.append(car)
                i += 1
            elif 'truck' == line['car_type']:
                truck = Truck(line['brand'], line['photo_file_name'], line['carrying'], line['body_whl'])
                if truck.carrying == -1 or truck.brand == -1 or truck.photo_file_name == -1:
                    continue
                car_list.append(truck)
                i += 1
            elif 'spec_machine' == line['car_type']:
                spec_machine = SpecMachine(line['brand'], line['photo_file_name'], line['carrying'], line['extra'])
                if spec_machine.carrying == -1 or spec_machine.brand == -1 or spec_machine.photo_file_name == -1 or spec_machine.extra == -1:
                    continue
                car_list.append(spec_machine)
                i += 1
            else:
                continue
    return car_list