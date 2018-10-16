#!/usr/bin/env python3

import argparse
import csv

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
                      # 'Date_assigned_to_inv': row[7],
                      'Calibration_Date': row[8][:-2] + '20' + row[8][-2:],
                      'Calibration_Frequency': row[9],
    })

print(equipment[0])

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nova_geotechnical.settings")
django.setup()

from inventory.models import *
import datetime

for item in equipment:
    added_item = Equipment()
    added_item.Equipment_List = item['Equipment_Type'] # list convert
    added_item.Inventory_Number = item['Inventory_Number']
    added_item.Description_of_Item = item['Description_of_Item']
    added_item.Manufacturer = item['Manufacturer']
    added_item.Model_Number = item['Model_Number']
    added_item.Serial_Number = item['Serial_Number']
    added_item.Condition_as_recieved = item['Condition_as_recieved'] # list convert
    added_item.Calibration_Date = datetime.datetime.strptime(item['Calibration_Date'], '%m/%d/%y') # to datetime?
    added_item.Calibration_Frequency = int(item['Calibration_Frequency'])
    # added_item.Due_Date = item['Due_Date'] # to datetime?
    added_item.save()

print(Equipment.objects.all())
