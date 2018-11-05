from __future__ import print_function, unicode_literals
import csv
import sys
import openElectionsParser
from math import ceil
from PyInquirer import style_from_dict, Token, prompt, Separator
from PyInquirer import Validator, ValidationError
from pprint import pprint

def get_state():
    state_prompt = {
        'type': 'list',
        'name': 'state',
        'message': 'Which state would you like to audit?',
        'choices': ['Alabama','Alaska','Arizona','Arkansas','California','Colorado',
        'Connecticut','District of Columbia', 'Delaware','Florida','Georgia','Hawaii','Idaho', 
        'Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
        'Maine' 'Maryland','Massachusetts','Michigan','Minnesota',
        'Mississippi', 'Missouri','Montana','Nebraska','Nevada',
        'New Hampshire','New Jersey','New Mexico','New York',
        'North Carolina','North Dakota','Ohio',    
        'Oklahoma','Oregon','Pennsylvania','Rhode Island',
        'South  Carolina','South Dakota','Tennessee','Texas','Utah',
        'Vermont','Virginia','Washington','West Virginia',
        'Wisconsin','Wyoming']
    }
    answers = prompt(state_prompt)
    return answers['state']

def get_column():
    questions = [
        {
            'type': 'list',
            'name': 'col',
            'message': 'What column do you want to parse by?',
            'choices': ['precinct', 
            'ward', 
            'district']
        }
    ]
    answers = prompt(questions)
    return answers['col']

def get_mode():
    questions = [
        {
            'type': 'list',
            'name': 'mode',
            'message': 'Select mode',
            'choices': ['Percentage of all precincts.', 
            'Percentage/number of precincts in each county.', 
            'Percentage of ballots in each county.', 
            'Percentage of ballots in the state.', 
            'Risk-limiting audit.', 'Automatic.']
        }
    ]
    answers = prompt(questions)
    return answers['mode']

class NumberValidator(Validator):
    def validate(self, document):
        try:
            float(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end
        if (float(document.text) > 1 or float(document.text) < 0):
            raise ValidationError(
                message='Please enter a number between 0 and 1, inclusive',
                cursor_position=len(document.text))  # Move cursor to end

def get_percent():
    questions = [
        {
            'type': 'input',
            'name': 'percent',
            'message': 'Enter percentage (0 to 1, inclusive).',
            'validate': NumberValidator,
            'filter': lambda val: float(val)
        }
    ]
    answers = prompt(questions)
    return answers['percent']

def get_input(args):
    data_dict = {}
    if (len(args) == 0):
        state = get_state()
        if (state == 'Michigan'):
            data_dict = openElectionsParser.parse("20161108__mi__general__precinct.csv", 'precinct', 'President')
        else:
            print("Program under construction.")
            exit(0)
    else:
        col = get_column()
        data_dict = openElectionsParser.parse(args[1], col, 'President')
    mode = get_mode()
    if (mode == 'Percentage of all precincts.'):
        percent = get_percent()
        audit_precinct(percent, data_dict)

def audit_precinct(percentage, data_dict):
    state_wide_sorted = sorted(data_dict["vote_totals"].items(), key=lambda kv: kv[1], reverse=True)
    difference = state_wide_sorted[0][1] - state_wide_sorted[1][1]
    votes_to_flip = difference/2
    winner_name = state_wide_sorted[0][0]
    second_place = state_wide_sorted[1][0]
    total_num_precincts = len(data_dict["results"])
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

if __name__ == "__main__":
    get_input(sys.argv)
