# IOET_application
## Exercise
The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:

Example 1:

INPUT
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00


OUTPUT:
ASTRID-RENE: 2
ASTRID-ANDRES: 3
RENE-ANDRES: 2

Example 2:

INPUT:
RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
RENE-ASTRID: 3

## Solution Overview
To solve the following exercise, the following considerations have been made:
  1. The text file always has the same format and is not badly written.
  2. Employee names are not repeated

To parse a text file, it is necessary to read the lines of the file and handle them individually.
Each line contains the name and weekly schedules of each employee.

Therefore, dictionaries will be used to store the ordered information.

These dictionaries will be analyzed and the day and hours of each employee will be compared and if the dates coincide, the counter will be increased.

## Step by step solution  
In the following flowchart you can see how the program is structured.

![image](https://user-images.githubusercontent.com/57976123/164083170-efed3ce1-3fc5-419b-9934-7eecfbafdac1.png)

 A main function is executed and the result is displayed immediately, no user input is required.

The structure of the program is separated into 3 main parts differentiated by colors: green, aquamarine and purple.

The green section is responsible for transforming the text file into data that can be handled in the code (strings, dictionaries, lists, etc.).
The aquamarine section is responsible for taking the already processed data and comparing them with each other.
The purple section is responsible for taking the results and displaying them in the desired way.

At the beginning of the program, the fileToDicc function is executed. This seeks to transform the text file into a dictionary whose key is the name of the employee and its value is a dictionary that has the days in which this employee has worked as a key and the hours as a value.

Within this function, readFile is executed, which is responsible for transforming the file into a list of lines.
![image](https://user-images.githubusercontent.com/57976123/164088658-dc92951c-24e3-451e-b32e-b9eb1259817f.png)


This list enters the userToDicc function, which transforms each element of the list into dictionaries that contain the employee's name as a key and a text string with the schedule as a value. This string will be processed by the scheduleToDicc function to transform it into a dictionary.

![image](https://user-images.githubusercontent.com/57976123/164090064-62eb4c2e-fdf6-436b-a6f4-be26d9f9a4af.png)

The dictionary is passed to the compareUsers function, where the values ​​of each element of the dictionary are taken. In this comparison, the compareDicc function is used, which takes each dictionary of an employee and checks if the other employee has worked on the same day. If it is true, the compareHours function proceeds to analyze if these hours cross.
If the schedules cross, the counter is increased until all the days of one employee have been reviewed with the other.

Finally, a list of tuples is filled, in which the name of an employee is found, the name of the employee with whom it has been compared and the number of times that they coincide in the office.

![image](https://user-images.githubusercontent.com/57976123/164091279-3cdb1199-a724-448e-bc4e-4f54a7aac36f.png)


Finally, the formatResults function is used to display the data in a more user-friendly way, as requested in the exercise statement.

![image](https://user-images.githubusercontent.com/57976123/164091544-449d0674-ef44-4ce3-8b8a-fb8588668563.png)

## Tests

To test the program we have carried out 3 different tests detailed below.

EXAMPLE 1

INPUT: 

![image](https://user-images.githubusercontent.com/57976123/164093313-4c6d2bf5-4286-4d67-93d1-c9470da1fba8.png)

OUTPUT: 

![image](https://user-images.githubusercontent.com/57976123/164093361-8fef2ae9-e061-4820-8221-32f17f9ff5ef.png)

EXAMPLE 2

INPUT:

![image](https://user-images.githubusercontent.com/57976123/164093721-934f1271-6c57-4a7f-b969-4efb1b4cbf43.png)


OUTPUT:

![image](https://user-images.githubusercontent.com/57976123/164093773-a32327f3-bcde-4c63-9903-2485bcc61143.png)


EXAMPLE 3


INPUT:

![image](https://user-images.githubusercontent.com/57976123/164093810-da62eeda-4a36-4336-b3ef-c9d8d8788abc.png)


OUTPUT:

![image](https://user-images.githubusercontent.com/57976123/164093871-a5dc4374-7c30-48f5-a865-31ae91802e71.png)



## How to run this program locally

IMPORTANT: This program has been developed in python 3. This version or any of its versions is necessary to run it. You also need to have git installed on your computer.

1. Open the windows console and go to the directory where you want to install the folder. In this case it will be the desktop.

![image](https://user-images.githubusercontent.com/57976123/164106388-41a1a1b3-ba14-4fcb-8afc-40fb1e91a93b.png)

2. Copy the link from github and clone the file with the following command:

      - git clone https://github.com/renatojaraor/IOET_application.git
      - NOTE: Login to your github account is required.
      

![image](https://user-images.githubusercontent.com/57976123/164105284-522f5924-8fee-4259-9cd7-ef9bdbff656a.png)


3. Open the project directory

![image](https://user-images.githubusercontent.com/57976123/164105189-8b7dd41f-077f-4a68-8900-e1a3fc3dea9d.png)

4. Run the program using the following command.

      - python exercise.py
      - NOTE: If the message "Python not found" appears. Use "py" instead of "python" : py exercise.py
      
![image](https://user-images.githubusercontent.com/57976123/164106143-b4afccf8-c116-4a60-9142-1f899f3292ce.png)

NOTE: Different tests of the program can be carried out by modifying the file "file.txt" from a notepad.
  
