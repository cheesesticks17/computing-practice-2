import csv
from typing import Dict

def sort_category(data: dict, itemlist: list, category: str):
    '''
    Places items and their count 
    from the itemlist into the data
    with a certain category
    '''
    for i in range(len(itemlist)):
        item = itemlist[i]
        if not category in data: #checks if the category is already in
            data[category] = {item: 1}
        else:
            itemdict = data[category] 
            if not item in itemdict:
                  count = 1
            else:
                count = itemdict[item] + 1
            itemdict[item] = count

def process_survey_data(csv_file_path: str) -> Dict[str, Dict[str, int]]:
    """
    Process CSV survey data and create a histogram structure.

    Args:
        csv_file_path: Path to the CSV file containing survey data

    Returns:
        A dictionary organized by category, with each category containing
        a dictionary of items and their vote counts
    """
    data = {}
    with open(csv_file_path, "r") as file:
        reader = csv.DictReader(file)
        for rows in reader: #all the below are lists 
            functions = rows["Python Functions"].split(";")
            strings = rows["Python String Methods"].split(";")
            lists = rows["Python List Methods"].split(";")
            sort_category(data, functions, "functions")
            sort_category(data, strings, "strings")
            sort_category(data, lists, "lists")


            
    return data

    pass

def write_histogram_to_file(histogram_data: Dict[str, Dict[str, int]], output_file: str) -> None:
    """
    Write histogram data to a text file in a formatted way.

    Args:
        histogram_data: The dictionary returned by process_survey_data
        output_file: Path to the output file
    """
    # Write your code here

    pass

def create_visual_bar_chart(histogram_data: Dict[str, Dict[str, int]], symbol: str = '#') -> str:
    """
    Create a visual bar chart representation of the histogram data.

    Args:
        histogram_data: The dictionary returned by process_survey_data
        symbol: The symbol to use for the bar chart (default: '#')

    Returns:
        A string containing the formatted bar chart
    """
    # Write your code here

    pass

if __name__ == "__main__":
    print(process_survey_data('basicpythonnotessurvey.csv'))