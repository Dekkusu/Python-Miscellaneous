import csv
import pandas as pd
import time
import os

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


def to_csv_leg_data(csv_filename, csv_filedata):
    csv_file = directory+csv_filename
    list_data_count_keys = list(csv_filedata.keys())
    list_data_count_values = list(csv_filedata.values())
    try:
        reader = pd.read_csv(csv_file)
        try:
            for line_count in range(len(reader.index)):
                if reader.loc[line_count, "Time"] == list_data_count_values[1]:
                    reader.loc[line_count, list_data_count_keys[2:6]] = list_data_count_values[2:6]
                    # reader.loc[line_count, "Total Vehicles"] = sum(reader.loc[line_count, list_data_count_keys[2:6]])      #change x in [2:x] if new csv header is added
                    reader.to_csv(csv_file, index=False)
                    print(f"Successfully Updated {csv_file}")
                    break
                if line_count == range(len(reader.index))[-1] and reader.loc[line_count, "Time"] != list_data_count_values[1]:
                    # reader.to_csv(csv_file, mode='a', header=False)
                    with open(csv_file, "a", newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(list_data_count_values)
                        print(f"Successfully Added New Line in {csv_file}")
        except:
            print(f"Error Updating {csv_file}")  # change print content
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
    "Camera 1" : 5,
    "Camera 2" : 5,
    "Camera 3" : 5,
    "Camera 4" : 5,
}

to_csv_vehicle_class_breakdown(class_breakdown_filename, vehicle_count_data)
to_csv_leg_data(leg_filename, lane_data)
