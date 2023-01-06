import steamspypi
import steampi.text_distances
import requests
import pandas as pd
import xlsxwriter

# Remove all "nan" values
def remove_nan(list):
    return [ele for ele in list if str(ele) != 'nan']

# Get steamspy data
def get_steam_data(games_list, progress, percent):
    cleaned_games_list = remove_nan(games_list)
    steamspy_database = steamspypi.load()
    all_games_data = requests.get('http://steamspy.com/api.php?request=all').json()
    if len(all_games_data) == 0:
        print("Steamspy API is down. For example, http://steamspy.com/api.php?request=all is returning empty dictionary")
        # TODO: Implement an alternate method
    else:
        total_game_count = len(cleaned_games_list)
        first = True

        # Construct table
        for game_name in cleaned_games_list:
            sorted_app_ids, text_distances = steampi.text_distances.find_most_similar_game_names(game_name, steamspy_database) #Crysis 2 is being matched with Crysis, instead of Crysis 2 - Maximum Edition. preprocess separate games
            app_id = sorted_app_ids[0]

            from operator import itemgetter
            data = requests.get('https://steamspy.com/api.php?request=appdetails&appid='+str(app_id)).json()

            # If first time inside the for loop, create all dictionaries
            if first:
                first = False
                keydata = {}
                keydata['input_names'] = []
                keydata['levenshtein_distance'] = []
                for key in data.keys():
                    keydata[key] = []

            all_dicts = []
            keydata['input_names'].append(game_name)
            keydata['levenshtein_distance'].append(text_distances[app_id])

            for key in data.keys():
                keydata[key].append(data[key])

        # Done constructing table, Update progress to 100%
        progress['value'] = 100
        percent['text'] = "{}%".format(int(100))

    df1 = pd.DataFrame.from_dict(keydata)

    #https://xlsxwriter.readthedocs.io/working_with_pandas.html

    workbook = xlsxwriter.Workbook('Output_Files\ChoosenGamesData_SecondQuery.xlsx')

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('Output_Files\ChoosenGamesData_SecondQuery.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df1.to_excel(writer, sheet_name='Sheet1')
    df1.to_excel(writer, sheet_name='Sheet1')

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()




# Next step: https://stackoverflow.com/questions/50411346/update-an-excel-sheet-in-real-time-using-python
# Hint: Just highlight the ones that are duplicates and show the matched name, let them manually fix
