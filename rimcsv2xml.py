import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import csv
import sys

if not all([sys.argv[1], sys.argv[2]]):
    exit('usage: python rimcsv2xml.py input.csv output.xml')

root = ET.Element('LanguageData')

with open(sys.argv[1], 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for idx, row in enumerate(reader):
        if idx == 0:
            continue
        node = ET.Element(row[0])
        node.text = row[1]
        root.append(node)

dom = minidom.parseString(ET.tostring(root))
pretty_xml = dom.toprettyxml(encoding='utf-8')
with open(sys.argv[2], 'bw') as xmlfile:
    xmlfile.write(pretty_xml)
