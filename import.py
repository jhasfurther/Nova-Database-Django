#!/usr/bin/env python3

import os, django
import argparse
import csv
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nova_geotechnical.settings")
django.setup()

from inventory.models import *

parser = argparse.ArgumentParser(description='Imports Nova Geotechnical inventory CSV to Django database.')
parser.add_argument('-f', '--file', type=argparse.FileType('r'), help="Input file in CSV format.")
args = parser.parse_args()

reader = csv.reader(args.file, delimiter=',', quotechar='|')
next(reader)
for row in reader:
    print("Importing item " + row[0])
    added_item = Equipment()
    added_item.equipment_type = row[0].split('-')[0]
    added_item.inventory_number = row[0].split('-')[1]
    added_item.description = row[1]
    added_item.manufacturer = row[2]
    added_item.model_number = row[3]
    added_item.serial_number = row[4]
    added_item.condition_as_recieved = row[5]
    if row[6]:
        added_item.calibration_date = datetime.datetime.strptime(row[6],'%m/%d/%Y')
    added_item.calibration_frequency = int(row[7])
    try:
        added_item.save()
        print('\033[92m' + "Success!" + '\033[0m')
    except Exception as err:
        print('\033[91m' + str(err) + '\033[0m')
    print('')
