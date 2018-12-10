from math import ceil, factorial
from decimal import Decimal

def audit_precinct(percentage, data_dict):
    state_wide_sorted = sorted(data_dict["vote_totals"].items(), key=lambda kv: kv[1], reverse=True)
    difference = state_wide_sorted[0][1] - state_wide_sorted[1][1]
    votes_to_flip = difference/2
    winner_name = state_wide_sorted[0][0]
    second_place = state_wide_sorted[1][0]
    total_num_precincts = len(data_dict["results"])
    print(total_num_precincts)
    precincts_sorted = sorted(data_dict["results"], key=lambda k: k["vote_totals"].get(winner_name, 0), reverse=True)
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
    print("Probability of detecting interference:", round(1 - prob_miss_interf, 4))


def audit_percent_votes_county(percentage, data_dict):
    state_wide_sorted = sorted(data_dict["vote_totals"].items(), key=lambda kv: kv[1], reverse=True)
    difference = state_wide_sorted[0][1] - state_wide_sorted[1][1]
    votes_to_flip = difference/2
    winner_name = state_wide_sorted[0][0]
    second_place = state_wide_sorted[1][0]
    first_second_total = state_wide_sorted[0][1] + state_wide_sorted[1][1]
    print(first_second_total)
    print(winner_name)
    print(second_place)
    print(votes_to_flip)
    prob_miss_interf = Decimal(1)
    for county in data_dict["results"]:
        winner_votes = county["vote_totals"][winner_name]
        second_place_votes = county["vote_totals"][second_place]
        votes_flipped = ((winner_votes + second_place_votes)/first_second_total) * votes_to_flip
        print(votes_flipped)
        num_votes_county = county["vote_totals"]["num_votes"]
        num_sampled = int(ceil(percentage * num_votes_county))
        bad_thresh = int(ceil(num_sampled*.005))
        print(bad_thresh)
        county_prob = Decimal(0)
        for i in range(0, bad_thresh):
            temp_prob = Decimal(1)
            for j in range(0, num_sampled):
                if j < i:
                    temp_prob *= Decimal(votes_flipped/(num_votes_county-j))
                else:
                    temp_prob *= Decimal((num_votes_county - j - votes_flipped)/(num_votes_county - j))
            temp_prob *= factorial(num_sampled)//factorial(num_sampled-i)//factorial(i)
            county_prob += temp_prob
        prob_miss_interf *= county_prob
    print("Probability of detecting interference:", round(1 - prob_miss_interf, 4))


def audit_state(percentage, data_dict):
    state_wide_sorted = sorted(data_dict["vote_totals"].items(), key=lambda kv: kv[1], reverse=True)
    difference = state_wide_sorted[0][1] - state_wide_sorted[1][1]
    total = 0
    for i in range(0, len(data_dict)):
        total += state_wide_sorted[i][1]
    votes_to_flip = difference/2
    print(votes_to_flip)
    print(total)
    num_sampled = int(ceil(percentage*total))
    bad_thresh = int(ceil(num_sampled * .005))
    prob_miss_interf = 0
    for i in range(0, bad_thresh):
        temp_prob = Decimal(1)
        for j in range(0, num_sampled):
            if j < i:
                temp_prob *= Decimal(votes_to_flip/(total-j))
            else:
                temp_prob *= Decimal((total - votes_to_flip - j) / (total - j))
        temp_prob *= factorial(num_sampled)//factorial(num_sampled-i)//factorial(i)
        prob_miss_interf += temp_prob
    print("Probability of detecting interference:", round(1 - prob_miss_interf, 4))


def audit_percent_precincts_county(percentage, data_dict):
    state_wide_sorted = sorted(data_dict["vote_totals"].items(), key=lambda kv: kv[1], reverse=True)
    difference = state_wide_sorted[0][1] - state_wide_sorted[1][1]
    votes_to_flip = difference/2
    winner_name = state_wide_sorted[0][0]
    second_place = state_wide_sorted[1][0]
    print(winner_name, second_place)
    print(votes_to_flip)
    votes_flipped = 0
    counties = {}
    for cty in data_dict["results"]:
        precincts = list(cty["precincts"].values())
        sorted_precincts = sorted(precincts, key=lambda k: k.get(winner_name, 0), reverse=True)
        counties[cty["name"]] = {"sorted_precincts": sorted_precincts, "num_flipped": 0}
    probabilities = {}
    while votes_flipped < votes_to_flip:
        max_score = 0
        max_county = ""
        for county, precincts in counties.items():
            sorted_precincts = precincts["sorted_precincts"]
            num_precincts_flipped = precincts["num_flipped"]
            num_precincts = len(sorted_precincts)
            prob_miss_interf = 1
            for i in range(ceil(percentage*num_precincts)):
                prob_miss_interf *= (num_precincts - i - num_precincts_flipped - 1)/(num_precincts - i)
            total_probability = 1
            for key, value in probabilities.items():
                if key != county:
                    total_probability *= value
            total_probability *= prob_miss_interf
            curr_score = total_probability * sorted_precincts[num_precincts_flipped].get(winner_name, 0)
            if curr_score > max_score:
                max_score = curr_score
                max_county = county
                max_county_prob = prob_miss_interf
                max_county_votes = sorted_precincts[num_precincts_flipped][winner_name]
        votes_flipped += max_county_votes
        print(max_county_votes)
        print(max_county)
        probabilities[max_county] = max_county_prob
        counties[max_county]["num_flipped"] += 1
    final_prob = 1
    for value in probabilities.values():
        final_prob *= value
    print("Probability of detecting interference:", round(1 - final_prob, 4))





