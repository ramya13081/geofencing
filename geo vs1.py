import time

class Geofence:
    def __init__(self, min_lat, max_lat, min_lng, max_lng):
        self.min_lat = min_lat
        self.max_lat = max_lat
        self.min_lng = min_lng
        self.max_lng = max_lng

    def contains(self,lat,lng):
        return self.min_lat <= lat <= self.max_lat and self.min_lng <= lng <= self.max_lng

class Vehicle:
    def __init__(self,geofence,initial_lat,initial_lng,velocity):
        self.geofence = geofence
        self.current_lat = initial_lat
        self.current_lng = initial_lng
        self.velocity = velocity

    def move(self,target_lat,target_lng):
        lat_diff = target_lat-self.current_lat
        lng_diff = target_lng-self.current_lng
        distance = (lat_diff**2+lng_diff**2)**0.5

        if distance <= self.velocity:
            self.current_lat = target_lat
            self.current_lng = target_lng
        else:
            direction_lat = lat_diff/distance
            direction_lng = lng_diff/distance
            delta_lat = direction_lat*self.velocity
            delta_lng = direction_lng*self.velocity
            self.current_lat += delta_lat
            self.current_lng += delta_lng

            if self.geofence.contains(self.current_lat,self.current_lng):
                print("vehicle moved to lat:{},lng:{}".format(self.current_lat,self.current_lng))
            else:
                print("vehicle movement aborted.new location is outside the geofence.")   
geofence = Geofence(40.0,41.0,-74.0,-73.0)
initial_lat = 39.5
initial_lng = -74.5
velocity = 0.01
vehicle = Vehicle(geofence,initial_lat,initial_lng,velocity)
while True:
    target_lat = (geofence.min_lat + geofence.max_lat)/2
    target_lng = (geofence.min_lng + geofence.max_lng)/2

    if vehicle.move(target_lat,target_lng):
        print("Vehicle reached the point inside the geofence.Stopping.")
        break

    print("updated latitude:{},longitude:{}".format(vehicle.current_lat,vehicle.current_lng))
    time.sleep(1)    
