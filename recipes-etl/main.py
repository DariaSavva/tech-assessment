# Import libraries
import pandas as pd 
import re

data_file = 'data.json'


def data_analyzer():
    # 1. Read dataset. Use read_json function to load json file:
    data = pd.read_json(data_file, lines=True)

    # 2. Creat condition that extracts every recipe that has “Chilies” as ingredient allowing misspeled and singular form:
    chilies_condition = data['ingredients'].str.contains(r'\bChil(?:i?|ies?|es?|is?|lie)\b', case=False, regex=True)

    # 3. Apply chilies_condition to the data frame:
    filtered_data = data[chilies_condition]

    # 4. Create function to extract minutes from cookTime and prepTime columns:
    def convert_to_min(time_field):
        # find hours and minutes using regex expression that expression to search for one or more digits 
        # followed by the letter 'M' or 'H' in the time_field
        hours_match = re.search(r'(\d+)H', time_field)
        minutes_match = re.search(r'(\d+)M', time_field)
        # hours can be missing, convert hours to int if exist
        if hours_match != None:
            hours = int(hours_match.group(1))
        else:
            hours = 0

        # the same conversion for minutes       
        if minutes_match !=None:
            minutes = int(minutes_match.group(1))
        else:
            minutes = 0

        return hours*60 + minutes

    # 5. Create extra column for preparation time and cook time in minutes:
    filtered_data['cook_time_min'] = filtered_data['cookTime'].apply(convert_to_min)     

    filtered_data['prep_time_min'] = filtered_data['prepTime'].apply(convert_to_min)

    # 6. Create column for total time:
    filtered_data['total_time'] = filtered_data['cook_time_min'] + filtered_data['prep_time_min']

    # 7. For creating difficulty column based on total time define function:
    def difficulty(total_time):
        if total_time > 60:
            return 'Hard'
        elif total_time >= 30 and total_time <= 60:
            return 'Medium'
        elif total_time < 30:
            return 'Easy'
        else:
            return 'Unknown'

    # 8. Apply function to create difficulty column:
    filtered_data['difficulty'] = filtered_data['total_time'].apply(difficulty)     

    # 9. Remove not needed columns:
    final_df = filtered_data.drop(columns=['cook_time_min', 'prep_time_min', 'total_time'])

    # 10. Save data frame to csv:
    final_df.to_csv('chilies_recipes.csv', index=False)


data_analyzer()