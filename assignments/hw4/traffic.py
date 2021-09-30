"""
Name: Joseph Fagua
traffic.py

Purpose: Create a python program that analyzes traffic patterns

Certificate of Authenticity:
I certify that this assignment is entirely my work.
"""


def main():
    num_roads = eval(input("How many roads were surveyed? "))
    hrm = 0
    for i in range(num_roads):
        days_roads = eval(input("How many days was road " + str(i + 1) + " surveyed?"))
        acc = 0
        for j in range(days_roads):
            car_traveled = eval(input("How many cars traveled on day " + str(j + 1) + "?"))
            acc = acc + car_traveled
            hrm = hrm + car_traveled
            road_average = acc / days_roads
        print("Road " + str(i + 1) + " average vehicles per day:", round(road_average, 2))
    average_vehicles = hrm / num_roads
    print("Total number of vehicles traveled on all roads:", hrm)
    print("Average number of vehicles per road:", round(average_vehicles, 2))


if __name__ == '__main__':
    main()
