# Evengelos Kontopantelis, David Reeves, Jose M Valderas, Stephen Campbell, Tim Doran, 2023.

import sys, csv, re

codes = [{"code":"G61..00","system":"readv2"},{"code":"G61..11","system":"readv2"},{"code":"G61..12","system":"readv2"},{"code":"G613.00","system":"readv2"},{"code":"G618.00","system":"readv2"},{"code":"G61X.00","system":"readv2"},{"code":"G61X000","system":"readv2"},{"code":"G61X100","system":"readv2"},{"code":"G64..12","system":"readv2"},{"code":"G640.00","system":"readv2"},{"code":"G640000","system":"readv2"},{"code":"G641.00","system":"readv2"},{"code":"G641.11","system":"readv2"},{"code":"G641000","system":"readv2"},{"code":"G64z.12","system":"readv2"},{"code":"G64z200","system":"readv2"},{"code":"G64z300","system":"readv2"},{"code":"G65..00","system":"readv2"},{"code":"G65y.00","system":"readv2"},{"code":"G65z000","system":"readv2"},{"code":"G65z100","system":"readv2"},{"code":"G66..00","system":"readv2"},{"code":"G66..13","system":"readv2"},{"code":"G660.00","system":"readv2"},{"code":"G661.00","system":"readv2"},{"code":"G662.00","system":"readv2"},{"code":"G664.00","system":"readv2"},{"code":"Gyu6200","system":"readv2"},{"code":"Gyu6400","system":"readv2"},{"code":"Gyu6D00","system":"readv2"},{"code":"Gyu6F00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('stroke-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["stroke-cereb---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["stroke-cereb---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["stroke-cereb---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
