import csv

filepath='Storage/healthcare-dataset-stroke-data-v1.csv'
x=0
ls=[]
with open(filepath, mode='r') as file:
    csvFile=csv.DictReader(file)
    for lines in csvFile:
        # x+=1
        # print(lines['hypertension'])
        # print(x)
        # print(lines['avg_glucose_level'])
        # if lines['hypertension'] != "0" and lines['hypertension'] !="1":
        #     print("yikes")
        if lines['bmi']!="N/A":
            x+=1
            print("L")
    print(x)
    print(5138-204)