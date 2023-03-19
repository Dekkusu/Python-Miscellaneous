import csv
import pandas as pd

def to_csv_leg_data(csv_filename, csv_filedata):
    csv_file = csv_filename
    fieldname_first = ["Date", "Time", "Camera 1", "Camera 2", "Camera 3", "Camera 4", "Total Vehicles"]
    list_lane_data_values = list(csv_filedata.values())

    if not os.path.exists(csv_file):
        with open(csv_file, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fieldname_first)
            writer.writerow(list_lane_data_values)
    else:
        try:
            reader = pd.read_csv(csv_file)
            for line_count in range(len(reader.index)):
                if reader.loc[line_count, "Time"] == list_lane_data_values[1]:
                    update_csv(csv_file, list_lane_data_values, line_count)
                    print("updated")
                    break
                if line_count == range(len(reader.index))[-1] and reader.loc[line_count, "Time"] != list_lane_data_values[1]:
                    with open(csv_file, "a", newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(list_lane_data_values)
                        print("new line added")
        except:
            print("error making file")

def update_csv(csv_filename, csv_filedata, linecount):
    line_count = linecount
    list_lane_data_values = csv_filedata
    update_csv = pd.read_csv(csv_filename)
    update_csv.loc[line_count, "Camera 1"] +=  list_lane_data_values[2]
    update_csv.loc[line_count, "Camera 2"] +=  list_lane_data_values[3]
    update_csv.loc[line_count, "Camera 3"] +=  list_lane_data_values[4]
    update_csv.loc[line_count, "Camera 4"] +=  list_lane_data_values[5]
    update_csv.loc[line_count, "Total Vehicles"] += sum(list_lane_data_values[2:])
    update_csv.to_csv(csv_filename, index=False)

def vehicle_class_update_csv(csv_filename, csv_filedata, row):
    row_line_count = row
    list_vehicle_count_keys = list(csv_filedata.keys())
    list_vehicle_count_values = list(csv_filedata.values())
    update_csv = pd.read_csv(csv_filename)
    for row_line_count in range(len(update_csv)):
        for vehicle_count_keys, vehicle_count_values in zip(list_vehicle_count_keys[2:], list_vehicle_count_values[2:]):
            update_csv.loc[row_line_count, vehicle_count_keys] = vehicle_count_values
            update_csv.to_csv("try2.csv", index=False)

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
vehicle_count_data = {
    "Date" : 0,
    "Time" : 0,
    "Ambulance" : 3,
    "Bike" : 2,
    "Car" : 1,
} 

vehicle_class_update_csv("try2.csv", vehicle_count_data, 0)

# row_line_count = 0
# list_vehicle_count_keys = list(vehicle_count_data.keys())
# list_vehicle_count_values = list(vehicle_count_data.values())
# update_csv = pd.read_csv("try2.csv")
# for row_line_count in range(len(update_csv)):
#     for vehicle_count_keys, vehicle_count_values in zip(list_vehicle_count_keys[2:], list_vehicle_count_values[2:]):
#         update_csv.loc[row_line_count, vehicle_count_keys] = vehicle_count_values
#         update_csv.to_csv("try2.csv", index=False)
        #print(vehicle_count_keys)
        #print(vehicle_count_values)

# lane_data = {
#     "Date" : 0.0,
#     "Time" : 1.0,
#     "Camera 1" : 15,
#     "Camera 2" : 20,
#     "Camera 3" : 69,
#     "Camera 4" : 90,
# }

# street_name = [
#     "street 1",
#     "street 2",
#     "street 3",
#     "street 4"
# ]
#
#to_csv_summarized("detailed.csv", lane_data, street_name)
#to_csv_leg_data("try.csv", lane_data)