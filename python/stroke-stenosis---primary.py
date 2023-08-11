# Evengelos Kontopantelis, David Reeves, Jose M Valderas, Stephen Campbell, Tim Doran, 2023.

import sys, csv, re

codes = [{"code":"G61z.00","system":"readv2"},{"code":"G64z.00","system":"readv2"},{"code":"G64z.11","system":"readv2"},{"code":"G65z.00","system":"readv2"},{"code":"G65zz00","system":"readv2"},{"code":"G6W..00","system":"readv2"},{"code":"G6X..00","system":"readv2"},{"code":"Gyu6300","system":"readv2"},{"code":"Gyu6500","system":"readv2"},{"code":"Gyu6600","system":"readv2"},{"code":"Gyu6G00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('stroke-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["stroke-stenosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["stroke-stenosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["stroke-stenosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
