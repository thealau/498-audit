from math import ceil

def audit_precinct(percentage, data_dict):
    state_wide_sorted = sorted(data_dict["vote_totals"].items(), key=lambda kv: kv[1], reverse=True)
    difference = state_wide_sorted[0][1] - state_wide_sorted[1][1]
    votes_to_flip = difference/2
    winner_name = state_wide_sorted[0][0]
    second_place = state_wide_sorted[1][0]
    total_num_precincts = len(data_dict["results"])
    print(total_num_precincts)
    precincts_sorted = sorted(data_dict["results"], key=lambda k: k["vote_totals"][winner_name], reverse=True)
    winner_total = 0
    count = 0
    while winner_total < votes_to_flip:
        winner_total += precincts_sorted[count]["vote_totals"][winner_name]
        count += 1
    num_to_flip = count
    prob_miss_interf = 1
    print(num_to_flip)
    for i in range(0, ceil(percentage*total_num_precincts)):
        prob_miss_interf *= (total_num_precincts - i - num_to_flip)/(total_num_precincts - i)
    print("Probability of detecting interference:", round(1 - prob_miss_interf, 2))

def audit_state(percentage, data_dict):
    state_wide_sorted = sorted(data_dict["vote_totals"].items(), key=lambda kv: kv[1], reverse=True)
    difference = state_wide_sorted[0][1] - state_wide_sorted[1][1]
    total = 0
    for i in range(0, len(data_dict)):
        total += state_wide_sorted[i][1]
    votes_to_flip = difference/2
    print(votes_to_flip)
    print(total)
    prob_miss_interf = 1
    for i in range(0, ceil(percentage*total)):
        prob_miss_interf *= (total - votes_to_flip - i) / (total - i)
    print("Probability of detecting interference:", round(1 - prob_miss_interf, 2))