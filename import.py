#!/usr/bin/env python3

import argparse
import csv
import datetime

parser = argparse.ArgumentParser(description='Imports Nova Geotechnical inventory CSV to Django database.')
parser.add_argument('--file', metavar='-f', type=argparse.FileType('r'), help="Input file in CSV format.")
args = parser.parse_args()

equipment = [] # empty equipment list to append to

reader = csv.reader(args.file, delimiter=',', quotechar='|')
next(reader)
for row in reader:
    equipment.append({'Equipment_Type': row[0].split('-')[0],
                      'Inventory_Number': row[0].split('-')[1],
                      'Description_of_Item': row[1],
                      'Manufacturer': row[2],
                      'Model_Number': row[3],
                      'Serial_Number': row[4],
                      'Condition_as_recieved': row[5],
                      # 'Date_revievd': row[6],
                      #'Calibration_Date': row[8][:-2] + '20' + row[8][-2:],
                      'Calibration_Date' : datetime.datetime.strptime(row[6],'%m/%d/%Y'),
                      'Calibration_Frequency': row[7],
    })
    print(row[6])


import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nova_geotechnical.settings")
django.setup()

from inventory.models import *

for item in equipment:
    added_item = Equipment()
    added_item.equipment_type = item['Equipment_Type'] # list convert
    added_item.inventory_number = item['Inventory_Number']
    added_item.description = item['Description_of_Item']
    added_item.manufacturer = item['Manufacturer']
    added_item.model_number = item['Model_Number']
    added_item.serial_number = item['Serial_Number']
    added_item.condition_as_recieved = item['Condition_as_recieved'] # list convert
    #added_item.Calibration_Date = datetime.datetime.strptime(item['Calibration_Date'], '%m/%d/%y') # to datetime?
    added_item.calibration_date = item['Calibration_Date']
    added_item.calibration_frequency = int(item['Calibration_Frequency'])
    # added_item.Due_Date = item['Due_Date'] # to datetime?
    print(type(added_item.calibration_date))
    added_item.save()

print(Equipment.objects.all())