# when using the scrape_icons.py script to download icons the paths that 
# are stored in the CSV are incorrect - this fixes them

import csv

if __name__ == "__main__":
    in_fname = 'server/output_fixed.csv'
    out_fname = 'server/sources_final.csv'
    in_file = open(in_fname)
    out_file = open(out_fname, 'a')
    reader = csv.reader(in_file)
    writer = csv.writer(out_file)

    for row in reader:
        new_path = row[4][16:]
        new_row = [row[0],row[1],row[2],row[3],new_path]
        writer.writerow(new_row)
    in_file.close()
    out_file.close()
