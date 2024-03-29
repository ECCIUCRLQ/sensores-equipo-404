import data_detector
import os
import pickle

def save_data(date, team_id, sensor_id, sensor_type, data_packet):

    name_file = data_detector.detect_team(team_id)

    if( name_file != None ):                    # If there is no error.
        file = open(name_file + ".txt", "a+")

        file.write("Date and time: " + str(date) + " - Team id: " + str(team_id) + " - Sensor id: " + str(sensor_id) + " - Sensor type: " + str(sensor_type)
                   + " - Data: " + str(data_packet) + "\n")
        file.close()

    else:
        print("team_id no reconocido: " + team_id )


def save_object(path, name, data):

    if(os.path.exists(path) == False):
        os.makedirs(path)

    # x = if the file exists, truncate and write.
    file = open(path + name, "wb")
    pickle.dump(data, file, pickle.HIGHEST_PROTOCOL)
    file.close()

def delete_file(path):
    os.remove(path) 
    

def get_object(path):
    file = open(path, "rb")
    data = pickle.load(file)
    file.close()

    return data


def write_file(path, data):
    file = file = open(path, "w")
    file.write(data)
    file.close()
