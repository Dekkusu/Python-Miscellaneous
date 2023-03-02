import csv
import os

vehicle_count_data = {
    "Time & Date" : 0.0,
    "ambulance": 0,
    "bike" : 0,
    "bus" : 5,
} 

lane_data = {
    "Time" : 1.0,
    "S1_Movement 1" : 1,
    "S1_Movement 2" : 4,
    "S1_Movement 3" : 5 
}

street_name_1 = "street 1"
street_name_2 = "street 2"
street_name_3 = "street 3"
street_name_4 = "street 4"

fieldname_first = ["", "", street_name_1, "", "", street_name_2, "", "", street_name_3, "", "", street_name_4, ""]
fieldname_second = ["Time", "Movement 1", "Movement 2", "Movement 3", "Movement 1", "Movement 2", "Movement 3", "Movement 1", "Movement 2", "Movement 3", "Movement 1", "Movement 2", "Movement 3"]

def to_csv_summarized():
    csvfile_check = "lane_count_data.csv"
    if not os.path.exists(csvfile_check):
        with open(csvfile_check, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fieldname_first)
            writer.writerow(fieldname_second)
        
    #list_lane_data_keys = list(lane_data.keys())
    list_lane_data_values = list(lane_data.values())
    with open(csvfile_check, "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(list_lane_data_values)

def to_csv_detailed():
    csvfile_check = "vehicle_count_data.csv"
    list_vehicle_count_keys = list(vehicle_count_data.keys())
    list_vehicle_count_values = list(vehicle_count_data.values())

    if not os.path.exists(csvfile_check):
        with open(csvfile_check, "w", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list_vehicle_count_keys)
            writer.writeheader()

    with open(csvfile_check, "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(list_vehicle_count_values)