import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




def readCoronaCases():
    """
    Read english coronavirus cases from csv file
    """

    cases = pd.read_csv("data_2020-Sep-02.csv")
    return cases


def readFTSEData():
    FTSEData = pd.read_csv("FTSE 100 Historical Data (1).csv")
    
    return FTSEData

def coronavirusDataCleaning(data):
    data['clean_date'] = pd.to_datetime(data['date'], dayfirst = False, yearfirst = False)
    
    return data


def FTSEDataCleaning(data):
    data.columns = [c.replace(' ', '_') for c in data.columns]
    
    data['clean_date'] = pd.to_datetime(data['Date'], dayfirst = False, yearfirst = False)

    data["Price"] = data["Price"].str.replace(",", "")
    data["Change_%"] = data["Change_%"].str.replace("%", "")

    data["Price"] = data["Price"].astype(float)
    data["Change_%"] = data["Change_%"].astype(float)


    return data


def main():

    df1 = readCoronaCases()
    df2 = readFTSEData()

    covidData = coronavirusDataCleaning(df1)
    FTSEData = FTSEDataCleaning(df2)


    covidData.sort_values(by=["newCasesBySpecimenDate"], inplace=True, ascending=False)

    #covidData.sort_values(by=["clean_date"], inplace=True, ascending=False)

    covidData['clean_date'] =pd.to_datetime(covidData.date)

    #print(covidData)

    nationalCases = covidData[covidData['Area_code'] == "E92000001"]
    nationalCases.sort_values(by=["newCasesBySpecimenDate"], inplace=True, ascending=True)

    #print(nationalCases)

    nationalCases.plot(kind="line", x="date", y="newCasesBySpecimenDate")


    FTSEData.sort_values(by=["clean_date"], inplace=True, ascending=False)

    FTSEData["Price"] = FTSEData["Price"].astype(float)

    print(FTSEData.dtypes)

    print(FTSEData)

    FTSEData.plot(kind="line", x="clean_date", y="Price")


    plt.show()

"""
    virusInterestingFields = pd.DataFrame({"DailyCases" : nationalCases["Daily_lab-confirmed_cases"], "Date" : nationalCases["clean_date"], "TotalCases" : nationalCases["Cumulative_lab-confirmed_cases"]})
 
    virusInterestingFields.sort_values(by=["TotalCases"], inplace=True, ascending=True)

    print(virusInterestingFields)

    virusInterestingFields.plot(kind="line", x="Date", y="DailyCases", color="red")
"""








if __name__ == "__main__":
    main()
    