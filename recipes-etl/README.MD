# Technical Assessment
### Savvateeva Daria

## Description
   
   This program is designed to analyze recipes file in json format, filtering and enhancing the data based on specific criteria.<br/>
   The script begins by downloading the dataset, a collection of recipes.

   The script reads through the recipes in the dataset, extracting every recipe that includes "Chilies" as one of the ingredients. The implementation is robust, accommodating variations of misspelling, such as "Chiles", "Chilis", "Chillie", as well as the singular form of the word - "Chili".<br/>
   The code also extracts minutes and hours from the time columns "prepTime" and "cookTime" and sums their data into a new column "total_time".<br/>

   Based on "total_time" column an additional column, named "difficulty," is added to each extracted recipe. The difficulty is classified as follows:<br/>
- "Hard" if the sum of prepTime and cookTime is greater than 1 hour.
- "Medium" if the total time is between 30 minutes and 1 hour.
- "Easy" if the total time is less than 30 minutes.
- "Unknown" for any other cases.<br>
  
The resulting dataset, containing the filtered recipes with the added "difficulty" column, is saved as a CSV file.

For the program to work , the json file should comtain the following fields:<br/>
- 'ingredients';
- 'prepTime';
- 'cookTime';
  



 



## Dependencies
- Python 3.12.1
- Pandas 2.2.0


## How to run programm
1. Install Python version 3.12.1<br/>
2. Install Pandas library in windows terminal <br>`$ pip install pandas`<br/>
3. Original json file for further analysis should be located in the same directory under the name `data.json`.<br/>
4. Run the program in terminal <br> `$ python main.py `.<br/>
5. Analyzed data will be saved in `chilies_recipes.csv`








