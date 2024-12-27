import pandas as pd

def read_ieee_format(file_path):
    """
    Reads IEEE format data from an Excel file.

    Args:
        file_path (str): Path to the Excel file.

    Returns:
        dict: A dictionary containing bus and branch data as DataFrames.
              Example:
              {
                  "buses": DataFrame of bus data,
                  "branches": DataFrame of branch data
              }
    """
    try:
        # Read all sheets from the Excel file
        data = pd.read_excel(file_path, sheet_name=None)
        
        # Extract specific sheets (assuming "Buses" and "Branches" sheets)
        buses = data.get("Buses")
        branches = data.get("Branches")

        if buses is None or branches is None:
            raise ValueError("Missing required sheets: 'Buses' or 'Branches' in the Excel file.")
        
        return {
            "buses": buses,
            "branches": branches
        }
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Please check the path and try again.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def display_ieee_data(data):
    """
    Displays IEEE format data in a user-friendly format.

    Args:
        data (dict): A dictionary containing bus and branch data.
    """
    if not data:
        print("No data to display.")
        return

    print("\nBus Data:")
    print(data["buses"])

    print("\nBranch Data:")
    print(data["branches"])

