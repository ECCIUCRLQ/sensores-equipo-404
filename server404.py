import socket
import struct
import packet_builder
import datetime
import file_manager

UDP_IP = "10.1.137.67"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET,    # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)    # Buffer size is 1024 bytes
    print ("Received message: ")
    packet = struct.unpack(packet_builder.FORMAT, data)

    sequence = str(packet[0])
    date = str(datetime.datetime.fromtimestamp(packet[1]))
    team_id = str(packet[2])
    sensor_id = str(int.from_bytes(packet[3], "big"))
    sensor_type = str(packet[4])
    data_packet = str(packet[5])


    print(sequence + ' ' + date + ' ' + team_id + ' ' + sensor_id + ' ' + sensor_type + ' ' + data_packet)

    file_manager.save_data(date, team_id, sensor_id, sensor_type, data_packet)
