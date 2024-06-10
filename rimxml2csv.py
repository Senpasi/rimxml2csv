import xml.etree.ElementTree as ET
import csv
import sys

if not all([sys.argv[1], sys.argv[2]]):
    exit('usage: python rimxml2csv.py input.xml output.csv')

tree = ET.parse(sys.argv[1])
root = tree.getroot()

with open(sys.argv[2], 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['Tag', 'Value'])

    for record in root:
        row = [record.tag, record.text]
        writer.writerow(row)
