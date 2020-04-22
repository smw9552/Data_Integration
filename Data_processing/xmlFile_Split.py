import xml.etree.ElementTree as ET
context = ET.iterparse('C:\\Users\\username\\Documents\\Tasks.xml', events=('end', ))

for event, elem in context:

    if elem.tag == 'Task':
       title = elem.find('TaskID').text
       filename = format(title + ".txt")
       with open(filename, 'wb') as f:
           f.write(ET.tostring(elem))