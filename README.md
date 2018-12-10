# Post-Election Audit Interface

This project uses [OpenElections](https://github.com/openelections) data to calculate probability of detecting interference in a given election. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Install [PyInquirer](https://github.com/CITGuru/PyInquirer)

Install Flask.

### Installing

Download the files.

## Running the tests

audit.py has three modes:

### Interactive Command Line (cli)

```
audit.py -m cli [input_csv]
```

This mode will ask you to customize the audit and calculates the probability of detecting interference based on your choices.

### Automatic (auto)

```
audit.py -m auto
```

This mode will ask you to select a state and uses preprocessed data to simulate an audit.

### Web (web)

This mode is used from the web interface. Please see next section for instructions on using web interface.

## Web App Startup

To start the web app on localhost, run ./bin/elecsecrun.sh from the project directory.

## Authors

* **Chand Rajendra-Niccoluci** 
* **Theadora Lau** 
* **Derek Lau** 

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Alex Halderman and Matthew Bernhard