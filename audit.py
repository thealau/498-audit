#!/usr/bin/env python

from __future__ import print_function, unicode_literals
import csv
import sys
import openElectionsParser
import calculations
import click
from PyInquirer import style_from_dict, Token, prompt, Separator
from PyInquirer import Validator, ValidationError
from pprint import pprint

@click.command()
@click.option('--mode', '-m', help='Choose a mode: cli, web, auto')
@click.argument('input_csv')
def get_input(mode, input_csv):
    data_dict = {}
    audit_type = ""
    percent = 0
    if (mode == "web"):
        msg = sys.stdin.readline()
        inputs = msg.split(',')
        audit_type = inputs[0]
        col = inputs[1]
        race = inputs[2]
        percent = float(inputs[3])
        data_dict = openElectionsParser.parse("csvs/"+input_csv, col, race, audit_type)
    else:
        if (mode == "auto"):
            state = get_state()
            if (state == 'Michigan'):
                data_dict = openElectionsParser.parse("csvs/20161108__mi__general__precinct.csv", 'precinct', 'President', 'Percentage of precincts in each county.')
                audit_type = get_audit_type()
            else:
                print("Program under construction.")
                exit(0)
        else:
            audit_type = get_audit_type()
            col = ""
            if audit_type == 'Percentage of precincts in each county.':
                col = get_columns()
            else:
                col = get_column()
            race = get_race()
            data_dict = openElectionsParser.parse("csvs/"+input_csv, col, race, audit_type)
            percent = get_percent()
    if (audit_type == 'Percentage of all precincts.'):
        calculations.audit_precinct(percent, data_dict)
    elif (audit_type == 'Percentage of ballots in each county.'):
        calculations.audit_percent_votes_county(percent, data_dict)
    elif (audit_type == 'Percentage of ballots in the state.'):
        calculations.audit_state(percent, data_dict)
    elif (audit_type == 'Percentage of precincts in each county.'):
        calculations.audit_percent_precincts_county(percent, data_dict)

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


def get_columns():
    questions = [
        {
            'type': 'list',
            'name': 'col',
            'message': 'What column represents the precincts for this data?',
            'choices': ['precinct',
            'ward', 
            'district']
        }
    ]
    answers = prompt(questions)
    return answers['col']


def get_audit_type():
    questions = [
        {
            'type': 'list',
            'name': 'audit_type',
            'message': 'Select audit_type',
            'choices': ['Percentage of all precincts.', 
            'Percentage of precincts in each county.', 
            'Percentage of ballots in each county.', 
            'Percentage of ballots in the state.']
        }
    ]
    answers = prompt(questions)
    return answers['audit_type']

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

def get_race():
    questions = [
        {
            'type': 'input',
            'name': 'race',
            'message': 'Enter the race to audit.'
        }
    ]
    answers = prompt(questions)
    return answers['race']

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

if __name__ == "__main__":
    get_input()
