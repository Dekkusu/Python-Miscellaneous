import csv
import os

def to_csv_summarized(csv_filename, csv_filedata, csv_fileheader):
    csv_file = csv_filename
    csv_header_1 = csv_fileheader
    fieldname_first = ["", "", csv_header_1[0], "", "", csv_header_1[1], "", "", csv_header_1[2], "", "", csv_header_1[3], ""]
    fieldname_second = ["Time", "Movement 1", "Movement 2", "Movement 3", "Movement 1", "Movement 2", "Movement 3", "Movement 1", "Movement 2", "Movement 3", "Movement 1", "Movement 2", "Movement 3"]
    
    if not os.path.exists(csv_file):
        with open(csv_file, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fieldname_first)
            writer.writerow(fieldname_second)

    list_lane_data_values = list(csv_filedata.values())
    with open(csv_file, "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(list_lane_data_values)

def to_csv_detailed(csv_filename, csv_filedata):
    csv_file = csv_filename
    list_vehicle_count_keys = list(csv_filedata.keys())
    list_vehicle_count_values = list(csv_filedata.values())

    if not os.path.exists(csv_file):
        with open(csv_file, "w", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list_vehicle_count_keys)
            writer.writeheader()

    with open(csv_file, "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(list_vehicle_count_values)

# Sample data run
#
# vehicle_count_data = {
#     "Time & Date" : 0.0,
#     "ambulance": 0,
#     "bike" : 0,
#     "bus" : 5,
# } 

# lane_data = {
#     "Time" : 1.0,
#     "S1_Movement 1" : 1,
#     "S1_Movement 2" : 4,
#     "S1_Movement 3" : 5 
# }

# street_name = [
#     "street 1",
#     "street 2",
#     "street 3",
#     "street 4"
# ]

# to_csv_summarized("detailed.csv", lane_data, street_name)
# to_csv_detailed("summarized.csv", vehicle_count_data)