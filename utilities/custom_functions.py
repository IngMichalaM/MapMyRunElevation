import csv
from typing import Union, List


def save_line_to_file(month: str, year: Union[int, float, str], elevation: Union[int, float], sport: Union[List, str],
                      file: str) -> None:
    """ Save (append) given values as a new line into the given csv (semicolon delimited) file. """
    # ToDo: header of the file.

    # check the input
    if isinstance(elevation, (int, float)):
        elevation = str(elevation)

    if len(sport) > 1:
        sport = ', '.join(sport)

    with open(file, 'a') as f:
        # create the csv writer
        writer = csv.writer(f, delimiter=';')

        # write a row to the csv file
        writer.writerow([month, year, elevation, sport])


if __name__ == '__main__':
    from tkinter.filedialog import askopenfilename
    my_file = askopenfilename()
    save_line_to_file('January', '2022', 125, ['Swim', 'run'], my_file)

