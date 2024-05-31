import json
import matplotlib.pyplot as plt
import numpy as np

# A function for extracting the data from a JSON file.
def dataFromFileExtraction(filename: str):
    with open(filename, encoding = "utf-8") as inputFile:
        return json.load(inputFile)

# # Creates lists of all the categories.
# def categories(data: list):
#     activities = []
#     genders = []
#     for item in data[1:]:
#         if item["alle aktiviteter"] not in activities:
#             activities.append(item["alle aktiviteter"])
#         if item["kjønn"] not in genders:
#             genders.append(item("kjønn"))

# # A function for plotting values on a bar diagram.
# def barGraphing(yValues: list, xValues: list, slice: list):
#     # Slices the variables.
#     yValues = yValues[slice[0]:slice[1]]
#     xValues = xValues[slice[0]:slice[1]]

#     # Various pyplot functions for displaying the diagram.
#     plt.barh(yValues, xValues)
#     plt.subplots_adjust(left=0.25)
#     plt.gca().invert_yaxis()
#     plt.title("...")
#     plt.grid()
#     plt.show()

# A function for plotting values on a bar diagram with multiple parallell bars.
def multiBarGraphing(xValues: list, yValueNames: list, slice: list, labels: list):
    # Slices the variables.
    yValueNames = yValueNames[slice[0]:slice[1]]
    xValues = [item[slice[0]:slice[1]] for item in xValues]
    yValues = []

    # Creates new values.
    barWidth = 0.2

    # Various pyplot functions for displaying the diagram, and a loop for creating a variable amount of graphs
    for i in range(len(xValues)):
        if i == 0:
            yValues.append(np.arange(len(xValues[0])))
        else:
            yValues.append([x + barWidth*i for x in yValues[0]])

        plt.barh(yValues[i], xValues[i], height=barWidth, label=labels[i])
    plt.subplots_adjust(left=0.25)
    plt.gca().invert_yaxis()
    plt.title("...")
    plt.ylabel('Aktivitet', fontweight ='bold', fontsize = 15) 
    plt.xlabel('Tid brukt (timer og minutter)', fontweight ='bold', fontsize = 15) 
    plt.yticks(yValues[0], yValueNames)
    plt.grid()
    plt.legend()
    plt.show()

filename = "05994_20240126-145813-json.json"
data = dataFromFileExtraction(filename)
yValuesAktiviteter = [item["alle aktiviteter"] for item in data[1:] if item["kjønn"] == "Alle"]
xValuesMenn = [item["Tidsbruk 2000 I alt"] for item in data[1:] if item["kjønn"] == "Menn"]
xValuesKvinner = [item["Tidsbruk 2000 I alt"] for item in data[1:] if item["kjønn"] == "Kvinner"]
xValuesAlle = [item["Tidsbruk 2000 I alt"] for item in data[1:] if item["kjønn"] == "Alle"]
multiBarGraphing([xValuesMenn, xValuesKvinner, xValuesAlle], yValuesAktiviteter, [0, len(yValuesAktiviteter)], ["Menn", "Kvinner", "Alle"])