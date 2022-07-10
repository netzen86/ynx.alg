def anomaly(days, temp_values):
    anomaly_days = 0
    counter = 0
    for temp in temp_values:
        if counter == 0:
            if len(temp_values) == 1:
                return 1
            if temp > temp_values[counter + 1]:
                anomaly_days += 1
        elif counter == (days - 1):
            if temp > temp_values[counter - 1]:
                anomaly_days += 1
        elif temp_values[counter - 1] < temp > temp_values[counter + 1]:
            anomaly_days += 1
        counter += 1
    return anomaly_days


days = int(input())
temp_values = input()

temp_values = [int(i) for i in temp_values.split()]

print(anomaly(days, temp_values))
