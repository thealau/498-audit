import csv   

def parse_percent_precincts_county(csv_file, office):
    csv_reader = csv.DictReader(csv_file)
    headers = csv_reader.fieldnames
    print(headers)
    master_dict = {}
    data_dict = {}
    master_dict['vote_totals'] = {}
    master_dict['results'] = []
    for row in csv_reader:
        if "Total" not in row.values():
            if row['office'] == office:
                if row["county"] not in data_dict: 
                    data_dict[row["county"]] = {}
                if row["precinct"] not in data_dict[row["county"]]:
                    data_dict[row["county"]][row["precinct"]] = {}
                data_dict[row["county"]][row["precinct"]][row["candidate"]] = int(row["votes"])
                if row['candidate'] not in master_dict['vote_totals']:
                    master_dict['vote_totals'][row['candidate']] = int(row['votes'])
                else:
                    master_dict['vote_totals'][row['candidate']] += int(row['votes'])
    for key, value in data_dict.items():
        master_dict['results'].append({"name": key, "precincts": value})
    return master_dict

def parse_county_or_precinct(csv_file, data_format, office):
    csv_reader = csv.DictReader(csv_file)
    headers = csv_reader.fieldnames
    print(headers)
    master_dict = {}
    data_dict = {}
    master_dict['vote_totals'] = {}
    master_dict['results'] = []
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

def parse(filename, data_format, office, audit_type):
    with open(filename, mode='r') as csv_file:
        if audit_type == 'Percentage of precincts in each county.':
            return parse_percent_precincts_county(csv_file, office)
        return parse_county_or_precinct(csv_file, data_format, office)
        
