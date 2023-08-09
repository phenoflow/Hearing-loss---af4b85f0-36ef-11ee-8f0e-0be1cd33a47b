# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"100449.0","system":"med"},{"code":"101755.0","system":"med"},{"code":"108029.0","system":"med"},{"code":"108030.0","system":"med"},{"code":"19694.0","system":"med"},{"code":"59392.0","system":"med"},{"code":"68636.0","system":"med"},{"code":"84365.0","system":"med"},{"code":"89253.0","system":"med"},{"code":"91930.0","system":"med"},{"code":"93278.0","system":"med"},{"code":"93446.0","system":"med"},{"code":"95814.0","system":"med"},{"code":"96555.0","system":"med"},{"code":"97657.0","system":"med"},{"code":"97761.0","system":"med"},{"code":"98241.0","system":"med"},{"code":"98553.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hearing-loss-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hearing-loss-procedure---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hearing-loss-procedure---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hearing-loss-procedure---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
