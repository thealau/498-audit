import csv   




def parse(filename, data_format, office):
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        headers = csv_reader.fieldnames
        print(headers)
        master_dict = {}
        data_dict = {}
        master_dict['vote_totals'] = {}
        master_dict['results'] = []
        first_line = True
        for row in csv_reader:
            if "Total" not in row.values():
                if row['office'] == office:
                    if row[data_format] not in data_dict: 
                        data_dict[row[data_format]] = {}
                        data_dict[row[data_format]]['num_votes'] = 0
                    data_dict[row[data_format]][row['candidate']] = int(row['votes'])
                    data_dict[row[data_format]]['num_votes'] += int(row['votes'])
                    if row['candidate'] not in master_dict['vote_totals']:
                        master_dict['vote_totals'][row['candidate']] = int(row['votes'])
                    else:
                        master_dict['vote_totals'][row['candidate']] += int(row['votes'])
        for key, value in data_dict.items():
            master_dict['results'].append({"name": key, "vote_totals": value})
        return master_dict
