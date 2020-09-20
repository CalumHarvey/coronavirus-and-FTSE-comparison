from requests import get
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.style as style


def getData(url):
    response = get(url, timeout=10)
    
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
        
    return response.json()
    

def makeUrl():
    endpoint = (
        'https://api.coronavirus.data.gov.uk/v1/data?'
        'filters=areaType=overview&'
        'structure={"date":"date","newCases":"newCasesByPublishDate", "newTests":"newTestsByPublishDate"}'
    )
    
    data = getData(endpoint)

    df = pd.DataFrame(data["data"])

    return df


if __name__ == "__main__":
    df = makeUrl()

    df.dropna(inplace=True)
    df["newTests"] = df["newTests"].astype(int)
    df["positiveTestRate"] = 2
    df["positiveTestRate"] = df["positiveTestRate"].astype(float)
    df['positiveTestRate'] = list(map(lambda x,y: x/y, df['newCases'],df['newTests']))

    df['date'] = pd.to_datetime(df['date'], dayfirst = False, yearfirst = False)
    df.sort_values(by=["date"], inplace=True, ascending=True)

    print(df)

    style.use('ggplot')


    g = sns.relplot(x="date", y="positiveTestRate", kind="line", data=df, )
    g.fig.autofmt_xdate()
    plt.show()


 