# Post-Election Audit Interface

This project uses [OpenElections](https://github.com/openelections) data to calculate probability of detecting interference in a given election. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install [PyInquirer](https://github.com/CITGuru/PyInquirer)

### Installing

Download the files.

## Running the tests

audit.py has two modes:

```
audit.py
```

This mode will ask you to select a state and get the input data from the database.

```
audit.py [state data input csv file]
```

This mode will parse the input file and ask for the column you want to parse by.

## Authors

* **Chand Rajendra-Niccoluci** 
* **Theadora Lau** 
* **Derek Lau** 

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc