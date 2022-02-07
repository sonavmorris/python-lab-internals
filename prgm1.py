import csv
fields=['NAMES','MFC','DC','DS','ASE']
rows=[['Sona','87','70','65','78'],
      ['Tony','76','45','93','56'],
      ['Mariya','79','70','60','78'],
      ['Agnes','52','63','66','64'],
      ['Aleena','61','67','79','32'],
      ['Ancy','59','77','80','68'],
      ['Benson','59','66','70','78'],
      ['Bebetto','79','70','60','78'],
      ['Brilla','98','89','52','80'],
      ['Mary','79','58','76','77']]
filename="mark.csv"
with open(mark2.csv,'w') as excel:
    csvw=csv.writer(excel)
    csvw.writerow(fields)
    csvw.writerows(rows)
