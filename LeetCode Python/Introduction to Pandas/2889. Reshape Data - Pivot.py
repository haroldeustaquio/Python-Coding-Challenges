import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    weather=pd.pivot(weather, index='month',columns='city',values='temperature')
    return weather 