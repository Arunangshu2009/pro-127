from bs4 import BeautifulSoup as soupe
import time
import pandas as pd 

scraped_data = []

def scrape():
    # Find <table>
    bright_star_table = soup.find("table", attrs={"class", "wikitable"})
    # Find <tbody>
    table_body = bright_star_table.find('tbody')
    # Find <tr>
    table_rows = table_body.find_all('tr')

    #Get data from <td>
    for row in table_rows:
        table_cols = row.find_all('td')
        # print(table_cols)

        temp_list = []

        for col_data in table_cols:
            # Printing Only colums textu data using ".text" property 
            # print(col_data.text)

            # Remove Extra white spaces using strip() method
            data = col_data.text.strip()
            # print(data)
            temp_list.append(data)
        # append data to start list
        scarped_data.append(temp_list)

    stars_data = []
    scarped_data = []
    for i in range(0,len(scarped_data)):
        Star_names = scarped_data[i][1]
        Distance = scarped_data[i][3]
        Mass = scarped_data[i][5]
        Radius = scarped_data[i][6]
        Lum = scarped_data[i][7]
        required_data = [Star_names, Distance, Mass, Radius, Lum] 
        stars_data.append(required_data)

        # Define Header
        headers = ['Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity']
        #Define pandas DataFrame
        star_df_1 = pd.DataFrame (stars_data, columns=headers)

    #Convert to CSV
    star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")