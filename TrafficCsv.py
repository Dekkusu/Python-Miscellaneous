import CsvWriter as to_csv
import random
import time

lane_data = {
    "Date" : 0.0,
    "Time" : 1.0,
    "Camera 1" : 0,
    "Camera 2" : 0,
    "Camera 3" : 0,
    "Camera 4" : 0,
    "Total Vehicles": 0
}

for i in range(1):
    print("Red Time")
    lane_data["Camera 1"] += random.randrange(15)+1
    lane_data["Camera 2"] += random.randrange(15)+1
    lane_data["Camera 3"] += random.randrange(15)+1
    lane_data["Camera 4"] += random.randrange(15)+1
    print(f"Queued: {lane_data['Camera 1']}")
    print(f"Queued: {lane_data['Camera 2']}")
    print(f"Queued: {lane_data['Camera 3']}")
    print(f"Queued: {lane_data['Camera 4']}")
    print("Writing to CSV...")
    time.sleep(3)
    for k in range(2):
        print(f"{k} Green Time")
        camera_1_vehicle_lost = random.randrange(3)+1
        camera_2_vehicle_lost = random.randrange(3)+1
        camera_3_vehicle_lost = random.randrange(3)+1 
        camera_4_vehicle_lost = random.randrange(3)+1

        vehicle_loss = {
            "Date" : 0.0,
            "Time" : 1.0,
            "Camera 1" : camera_1_vehicle_lost,
            "Camera 2" : camera_2_vehicle_lost,
            "Camera 3" : camera_3_vehicle_lost,
            "Camera 4" : camera_4_vehicle_lost,
            "Total Vehicles": 0
        }

        lane_data["Camera 1"] -= camera_1_vehicle_lost
        if lane_data["Camera 1"] < 0:                       # para if ang diff kay negative iya set balik to 0
            lane_data["Camera 1"] = 0
            vehicle_loss["Camera 1"] = 0
        
        lane_data["Camera 2"] -= camera_2_vehicle_lost
        if lane_data["Camera 2"] < 0:
            lane_data["Camera 2"] = 0
            vehicle_loss["Camera 2"] = 0
        
        lane_data["Camera 3"] -= camera_3_vehicle_lost
        if lane_data["Camera 3"] < 0:
            lane_data["Camera 3"] = 0
            vehicle_loss["Camera 3"] = 0
        
        lane_data["Camera 4"] -= camera_4_vehicle_lost
        if lane_data["Camera 4"] < 0:
            lane_data["Camera 4"] = 0
            vehicle_loss["Camera 4"] = 0

        print(f"DeQueued: {vehicle_loss['Camera 1']} Queued: {lane_data['Camera 1']}")
        print(f"DeQueued: {vehicle_loss['Camera 2']} Queued: {lane_data['Camera 2']}")
        print(f"DeQueued: {vehicle_loss['Camera 3']} Queued: {lane_data['Camera 3']}")
        print(f"DeQueued: {vehicle_loss['Camera 4']} Queued: {lane_data['Camera 4']}")
        
        to_csv.to_csv_leg_data("try.csv", vehicle_loss)
        time.sleep(1)
    

