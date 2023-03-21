import csv
import pandas as pd
import time
import os
import numpy as np

hour_now = time.strftime("%H") + ":00"

directory = "./results/"
leg_filename = time.strftime("%m%d%Y") + "_LaneData.csv"
class_breakdown_filename = time.strftime("%m%d%Y") + "_ClassData.csv"

if not os.path.exists(directory):
    os.makedirs(directory)

def create_empty_lane_csv(csv_filename):
    csv_file = csv_filename
    fieldnames = ["Date", "Time", "Camera 1", "Camera 2",
                  "Camera 3", "Camera 4", "Total Vehicles", "Daily Total"]
    list_data_count_keys = list(fieldnames)
    list_data_count_values = [0, 0, 0, 0, 0, 0, 0]
    data_time = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00',
                 '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00',
                 '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    try:
        with open(csv_file, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fieldnames)
            for write_zero in range(24):
                writer.writerow(list_data_count_values)
        reader = pd.read_csv(csv_file)
        for rows in range(len(reader.index)):
            reader.loc[rows, "Time"] = data_time[rows]
            reader.to_csv(csv_file, index=False)
        reader.loc[0, "Daily Total"] = 0
        reader.to_csv(csv_file, index=False)
    except Exception as e:
        print(e)

def create_temp_csv(csv_filedata):
    csv_filename = directory+"temp.csv"
    list_data_count_keys = list(csv_filedata.keys())
    list_data_count_values = list(csv_filedata.values())
    initial_value = [0, hour_now, 0, 0, 0, 0]
    vehicle_count_to_add = []
    try:
        reader = pd.read_csv(csv_filename)
        try:
            if list_data_count_values[2:6] == list(reader.loc[1, list_data_count_keys[2:6]]):
                reader.loc[2, list_data_count_keys[2:6]
                           ] = initial_value[2:6]
                reader.to_csv(csv_filename, index=False)
                print("free pass")
            elif (reader.loc[0, list_data_count_keys[2:6]] > 0).any():
                '''Have atleast 1 element/data greater than 0'''
                reader.loc[1, list_data_count_keys] = list_data_count_values    # new vehicle count data
                vehicle_count_to_add.extend(np.subtract(
                    reader.loc[1, list_data_count_keys[2:6]], reader.loc[0, list_data_count_keys[2:6]]))
                reader.loc[2, list_data_count_keys[2:6]] = vehicle_count_to_add
                # new value of previous data
                reader.loc[0, list_data_count_keys[2:6]] = vehicle_count_to_add
                reader.to_csv(csv_filename, index=False)
                print(f"Added new line {csv_filename}")
            else:
                '''If whole row is 0 or empty'''
                reader.loc[1, list_data_count_keys[2:6]
                           ] = reader.loc[1, list_data_count_keys[2:6]]
                reader.loc[2, list_data_count_keys[2:6]
                           ] = reader.loc[1, list_data_count_keys[2:6]]
                reader.to_csv(csv_filename, index=False)
                print("zero")
        except Exception as e:
            print(e)
    except:
        with open(csv_filename, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(list_data_count_keys)
            writer.writerow(list_data_count_values)
            writer.writerow(list_data_count_values)
            writer.writerow(list_data_count_values)

def to_csv_leg_data(csv_filename, csv_filedata):
    csv_file = directory+csv_filename
    list_data_count_keys = list(csv_filedata.keys())
    list_data_count_values = list(csv_filedata.values())
    final_vehicle_count_to_add = []
    try:
        reader = pd.read_csv(csv_file)
        try:
            for line_count in range(len(reader.index)):
                if reader.loc[line_count, "Time"] == list_data_count_values[1]:
                    if (reader.loc[line_count, list_data_count_keys[2:6]]>0).any():
                        '''Have atleast 1 element/data greater than 0'''
                        create_temp_csv(csv_filedata)
                        temp_reader = pd.read_csv(directory+"temp.csv")
                        final_vehicle_count_to_add.extend(temp_reader.loc[2, list_data_count_keys[2:6]])
                        #print(final_vehicle_count_to_add)
                        reader.loc[line_count, list_data_count_keys[2:6]
                                   ] += final_vehicle_count_to_add
                        reader.to_csv(csv_file, index=False)
                        #print("not Zero")
                        break
                    else:
                        '''If whole row is 0 or empty'''
                        #print("zero")
                        reader.loc[line_count, list_data_count_keys[2:6]] += list_data_count_values[2:6]
                        reader.to_csv(csv_file, index=False)
                        print(f"Successfully Updated {csv_file}")
                        break
                if line_count == range(len(reader.index))[-1] and reader.loc[line_count, "Time"] != list_data_count_values[1]:
                    print(f"Time Invalid")
        except Exception as e: print(e)
            # print(f"Error Updating {csv_file}")  # change print content
    except:
        create_empty_lane_csv(csv_file)
        to_csv_leg_data(csv_filename, csv_filedata)

    try:
        reader = pd.read_csv(csv_file)
        daily_total_vehicles = []
        for row in range(len(reader.index)):
            # change x in [2:x] if new csv header is added
            reader.loc[row, "Total Vehicles"] = sum(
                reader.loc[row, list_data_count_keys[2:6]])
            daily_total_vehicles.append(reader.loc[row, "Total Vehicles"])
            reader.to_csv(csv_file, index=False)
        reader.loc[0, "Daily Total"] = sum(
            daily_total_vehicles)        # for daily total
        reader.to_csv(csv_file, index=False)
    except:
        print(f"Error Updating Total {csv_file}")  # change print content

def to_csv_vehicle_class_breakdown(csv_filename, csv_filedata):
    csv_file = directory+csv_filename
    list_vehicle_class_count_keys = list(csv_filedata.keys())
    list_vehicle_class_count_values = list(csv_filedata.values())

    try:
        reader = pd.read_csv(csv_file)
        try:
            for line_count in range(len(reader.index)):
                if reader.loc[line_count, "Time"] == list_vehicle_class_count_values[1]:
                    # change x in [2:x] if new csv header is added
                    reader.loc[line_count, list_vehicle_class_count_keys[2:]
                               ] += list_vehicle_class_count_values[2:]
                    reader.to_csv(csv_file, index=False)
                    print(f"Successfully Updated {csv_file}")
                    break
                if line_count == range(len(reader.index))[-1] and reader.loc[line_count, "Time"] != list_vehicle_class_count_values[1]:
                    with open(csv_file, "a", newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(list_vehicle_class_count_values)
                        print(f"Successfully Added New Line in {csv_file}")
        except:
            print(f"Error Updating {csv_file}")  # change print content
    except:
        with open(csv_file, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(list_vehicle_class_count_keys)
            writer.writerow(list_vehicle_class_count_values)


# Sample data run


vehicle_count_data = {
    "Date" : 0,
    "Time" : 0,
    "Ambulance" : 69,
    "Bike" : 0,
    "Car" : 0,
    "Jeep" : 0,
    "Modern Jeep": 0
}

lane_data = {
    "Date" : 0.0,
    "Time" : hour_now,
    "Camera 1" : 2,
    "Camera 2" : 5,
    "Camera 3" : 10,
    "Camera 4" : 11,
}

# to_csv_vehicle_class_breakdown(class_breakdown_filename, vehicle_count_data)
to_csv_leg_data(leg_filename, lane_data)
# create_temp_csv(lane_data)
