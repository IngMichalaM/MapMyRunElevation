import configparser
from typing import Union, List

CONFIGFILE = "config.txt"

class MainConfig:
    """Read the info from the config file (CONFIGFILE), check it and return in a desired format."""

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read_file(open(fr'{CONFIGFILE}')) # self.config.read_file(open(r'config.txt'))

    def read_basic_info(self) -> tuple[List[str], int, List[str]]:

        sport_list = self.config.get('Basic_info', 'sport_list')
        if len(sport_list) == 0:
            raise ValueError(f'It seems that no sport art is defined in the config file ({CONFIGFILE}).')

        years = self.config.get('Basic_info', 'years')
        if len(years) == 0:
            raise ValueError(f'It seems that the year is missing in the config file ({CONFIGFILE}).')

        months = self.config.get('Basic_info', 'months')
        if len(months) == 0:
            raise ValueError(f'It seems that the list of months to be used is missing in the config file ({CONFIGFILE}).')

        # handle the data
        sports = sport_list.split(';')  # -> list of strings
        years_new = years.split(',')
        year_new = min([int(year) for year in years_new])  # -> int
        months_new = months.split(',')
        months_new = [month.strip().lower() for month in months_new]  # -> list of strings

        return sports, year_new, months_new


if __name__ == '__main__':
    basic_info_data = MainConfig().read_basic_info()
    sport_list = basic_info_data[0]
    years = basic_info_data[1]
    months = basic_info_data[2]
    print()
    print(f'Data from the configuration file {CONFIGFILE}:')
    print()
    print(f'List of sports: \n\t - {sport_list} \n\t - type of the variable: {type(sport_list)} '
          f'\n\t - length of the variable: {len(sport_list)}')
    print(f'The year most in the past: \n\t - {years}')
    print(f'Months to be evaluated: \n\t - {months} \n\t - their type: {type(months)}')
