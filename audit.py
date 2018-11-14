from __future__ import print_function, unicode_literals
import csv
import sys
import openElectionsParser
import calculations
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
            'district',
            'county']
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
            'Percentage of precincts in each county.', 
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
        # TODO: add a func to get race from user
        data_dict = openElectionsParser.parse(args[1], col, 'President')
    mode = get_mode()
    if (mode == 'Percentage of all precincts.'):
        percent = get_percent()
        calculations.audit_precinct(percent, data_dict)
    elif (mode == 'Percentage of ballots in each county.'):
        percent = get_percent()
        calculations.audit_percent_votes_county(percent, data_dict)

if __name__ == "__main__":
    get_input(sys.argv)
