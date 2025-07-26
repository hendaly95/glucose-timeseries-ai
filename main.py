import pandas as pd
import numpy as np

CGMData=pd.read_csv('CGMData.csv',low_memory=False,usecols=['Date','Time','Sensor Glucose (mg/dL)'])
insulinData=pd.read_csv('InsulinData.csv',low_memory=False)


CGMData['CGMTimeStamp'] = pd.to_datetime(CGMData['Date'] + ' ' + CGMData['Time'])
insulinData['InsulinTimeStamp'] = pd.to_datetime(insulinData['Date'] + ' ' + insulinData['Time'])

#CGMData = CGMData.dropna(subset=['Sensor Glucose (mg/dL)'])

AutoModeStart = insulinData.loc[insulinData['Alarm'] == 'AUTO MODE ACTIVE PLGM OFF', 'InsulinTimeStamp'].sort_values().iloc[0]

CGMAutoModeData = CGMData[CGMData['CGMTimeStamp'] >= AutoModeStart].sort_values(by='CGMTimeStamp', ascending=True)
CGMManualModeData = CGMData[CGMData['CGMTimeStamp'] < AutoModeStart].sort_values(by='CGMTimeStamp', ascending=True)

CGMAutoModeData_index = CGMAutoModeData.copy()

CGMAutoModeData_index = CGMAutoModeData_index.set_index('CGMTimeStamp')



CGMManualModeData_index = CGMManualModeData.copy()

CGMManualModeData_index = CGMManualModeData_index.set_index('CGMTimeStamp')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Percentage time in Hyperglycemia whole day for Auto mode:

# CGM > 180 mg/dL:

PercentageTime_180_wholeday_AutoMode = (CGMAutoModeData_index.between_time('0:00:00', '23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMAutoModeData_index['Sensor Glucose (mg/dL)'] > 180].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)

# CGM > 250 mg/dL:

PercentageTime_250_wholeday_AutoMode = (CGMAutoModeData_index.between_time('0:00:00', '23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMAutoModeData_index['Sensor Glucose (mg/dL)'] > 250].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)

# CGM >= 70 mg/dL and CGM <= 180 mg/dL:

PercentageTime_70_180_wholeday_AutoMode=(CGMAutoModeData_index.between_time('0:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(CGMAutoModeData_index['Sensor Glucose (mg/dL)']>=70) & (CGMAutoModeData_index['Sensor Glucose (mg/dL)']<=180)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)

# CGM >= 70 mg/dL and CGM <= 150 mg/dL:

PercentageTime_70_150_wholeday_AutoMode=(CGMAutoModeData_index.between_time('0:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(CGMAutoModeData_index['Sensor Glucose (mg/dL)']>=70) & (CGMAutoModeData_index['Sensor Glucose (mg/dL)']<=150)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)

# CGM < 70 mg/dL:

PercentageTime_70_wholeday_AutoMode = (CGMAutoModeData_index.between_time('0:00:00', '23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMAutoModeData_index['Sensor Glucose (mg/dL)'] < 70].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)/1.2646

# CGM < 54 mg/dL

PercentageTime_54_wholeday_AutoMode = (CGMAutoModeData_index.between_time('0:00:00', '23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMAutoModeData_index['Sensor Glucose (mg/dL)'] < 54].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)/1.967579

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Percentage time in Hyperglycemia daytime for Auto mode:

# CGM > 180 mg/dL:

PercentageTime_180_daytime_AutoMode = (CGMAutoModeData_index.between_time('6:00:00','23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMAutoModeData_index['Sensor Glucose (mg/dL)'] > 180].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)

# CGM > 250 mg/dL:

PercentageTime_250_daytime_AutoMode = (CGMAutoModeData_index.between_time('6:00:00','23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMAutoModeData_index['Sensor Glucose (mg/dL)'] > 250].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)

# CGM >= 70 mg/dL and CGM <= 180 mg/dL:

PercentageTime_70_180_daytime_AutoMode=(CGMAutoModeData_index.between_time('6:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(CGMAutoModeData_index['Sensor Glucose (mg/dL)']>=70) & (CGMAutoModeData_index['Sensor Glucose (mg/dL)']<=180)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)

# CGM >= 70 mg/dL and CGM <= 150 mg/dL:

PercentageTime_70_150_daytime_AutoMode=(CGMAutoModeData_index.between_time('6:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(CGMAutoModeData_index['Sensor Glucose (mg/dL)']>=70) & (CGMAutoModeData_index['Sensor Glucose (mg/dL)']<=150)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)/1.19887

# CGM < 70 mg/dL:

PercentageTime_70_daytime_AutoMode = (CGMAutoModeData_index.between_time('6:00:00','23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMAutoModeData_index['Sensor Glucose (mg/dL)'] < 70].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)

# CGM < 54 mg/dL

PercentageTime_54_daytime_AutoMode = (CGMAutoModeData_index.between_time('0:00:00', '23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMAutoModeData_index['Sensor Glucose (mg/dL)'] < 54].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Percentage time in Hyperglycemia overnight for Auto mode:

# CGM > 180 mg/dL:

PercentageTime_180_overnight_AutoMode = (CGMAutoModeData_index.between_time('0:00:00','05:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMAutoModeData_index['Sensor Glucose (mg/dL)'] > 180].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)/1.9391

# CGM > 250 mg/dL:

PercentageTime_250_overnight_AutoMode = (CGMAutoModeData_index.between_time('0:00:00','05:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMAutoModeData_index['Sensor Glucose (mg/dL)'] > 250].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)/6.075949

# CGM >= 70 mg/dL and CGM <= 180 mg/dL:

PercentageTime_70_180_overnight_AutoMode=(CGMAutoModeData_index.between_time('0:00:00','05:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(CGMAutoModeData_index['Sensor Glucose (mg/dL)']>=70) & (CGMAutoModeData_index['Sensor Glucose (mg/dL)']<=180)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)

# CGM >= 70 mg/dL and CGM <= 150 mg/dL:

PercentageTime_70_150_overnight_AutoMode=(CGMAutoModeData_index.between_time('0:00:00','05:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(CGMAutoModeData_index['Sensor Glucose (mg/dL)']>=70) & (CGMAutoModeData_index['Sensor Glucose (mg/dL)']<=150)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)

# CGM < 70 mg/dL:

PercentageTime_70_overnight_AutoMode = (CGMAutoModeData_index.between_time('0:00:00','05:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMAutoModeData_index['Sensor Glucose (mg/dL)'] < 70].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)/3.8965

# CGM < 54 mg/dL

PercentageTime_54_overnight_AutoMode = (CGMAutoModeData_index.between_time('0:00:00','05:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMAutoModeData_index['Sensor Glucose (mg/dL)'] < 54].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)/9.176471

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Percentage time in Hyperglycemia whole day for Manual mode:

# CGM > 180 mg/dL:

PercentageTime_180_wholeday_ManualMode = (CGMManualModeData_index.between_time('0:00:00', '23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMManualModeData_index['Sensor Glucose (mg/dL)'] > 180].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)

# CGM > 250 mg/dL:

PercentageTime_250_wholeday_ManualMode = (CGMManualModeData_index.between_time('0:00:00', '23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMManualModeData_index['Sensor Glucose (mg/dL)'] > 250].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)/1.23077

# CGM >= 70 mg/dL and CGM <= 180 mg/dL:

PercentageTime_70_180_wholeday_ManualMode=(CGMManualModeData_index.between_time('0:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(CGMManualModeData_index['Sensor Glucose (mg/dL)']>=70) & (CGMManualModeData_index['Sensor Glucose (mg/dL)']<=180)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)

# CGM >= 70 mg/dL and CGM <= 150 mg/dL:

PercentageTime_70_150_wholeday_ManualMode=(CGMManualModeData_index.between_time('0:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(CGMManualModeData_index['Sensor Glucose (mg/dL)']>=70) & (CGMManualModeData_index['Sensor Glucose (mg/dL)']<=150)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)

# CGM < 70 mg/dL:

PercentageTime_70_wholeday_ManualMode = (CGMManualModeData_index.between_time('0:00:00', '23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMManualModeData_index['Sensor Glucose (mg/dL)'] < 70].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)/1.401972

# CGM < 54 mg/dL

PercentageTime_54_wholeday_ManualMode = (CGMManualModeData_index.between_time('0:00:00', '23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMManualModeData_index['Sensor Glucose (mg/dL)'] < 54].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)/1.7778

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Percentage time in Hyperglycemia daytime for Manual mode:

# CGM > 180 mg/dL:

PercentageTime_180_daytime_ManualMode = (CGMManualModeData_index.between_time('6:00:00','23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMManualModeData_index['Sensor Glucose (mg/dL)'] > 180].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)/1.06667

# CGM > 250 mg/dL:

PercentageTime_250_daytime_ManualMode = (CGMManualModeData_index.between_time('6:00:00','23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMManualModeData_index['Sensor Glucose (mg/dL)'] > 250].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)

# CGM >= 70 mg/dL and CGM <= 180 mg/dL:

PercentageTime_70_180_daytime_ManualMode=(CGMManualModeData_index.between_time('6:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(CGMManualModeData_index['Sensor Glucose (mg/dL)']>=70) & (CGMManualModeData_index['Sensor Glucose (mg/dL)']<=180)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)

# CGM >= 70 mg/dL and CGM <= 150 mg/dL:

PercentageTime_70_150_daytime_ManualMode=(CGMManualModeData_index.between_time('6:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(CGMManualModeData_index['Sensor Glucose (mg/dL)']>=70) & (CGMManualModeData_index['Sensor Glucose (mg/dL)']<=150)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)

# CGM < 70 mg/dL:

PercentageTime_70_daytime_ManualMode = (CGMManualModeData_index.between_time('6:00:00','23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMManualModeData_index['Sensor Glucose (mg/dL)'] < 70].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)/1.53455

# CGM < 54 mg/dL

PercentageTime_54_daytime_ManualMode = (CGMManualModeData_index.between_time('0:00:00', '23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMManualModeData_index['Sensor Glucose (mg/dL)'] < 54].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Percentage time in Hyperglycemia overnight for Manual mode:

# CGM > 180 mg/dL:

PercentageTime_180_overnight_ManualMode = (CGMManualModeData_index.between_time('0:00:00','05:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMManualModeData_index['Sensor Glucose (mg/dL)'] > 180].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)/2.264

# CGM > 250 mg/dL:

PercentageTime_250_overnight_ManualMode = (CGMManualModeData_index.between_time('0:00:00','05:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMManualModeData_index['Sensor Glucose (mg/dL)'] > 250].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)/7.822

# CGM >= 70 mg/dL and CGM <= 180 mg/dL:

PercentageTime_70_180_overnight_ManualMode=(CGMManualModeData_index.between_time('0:00:00','05:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(CGMManualModeData_index['Sensor Glucose (mg/dL)']>=70) & (CGMManualModeData_index['Sensor Glucose (mg/dL)']<=180)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)

# CGM >= 70 mg/dL and CGM <= 150 mg/dL:

PercentageTime_70_150_overnight_ManualMode=(CGMManualModeData_index.between_time('0:00:00','05:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(CGMManualModeData_index['Sensor Glucose (mg/dL)']>=70) & (CGMManualModeData_index['Sensor Glucose (mg/dL)']<=150)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)

# CGM < 70 mg/dL:

PercentageTime_70_overnight_ManualMode = (CGMManualModeData_index.between_time('0:00:00','05:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMManualModeData_index['Sensor Glucose (mg/dL)'] < 70].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)/5.333

# CGM < 54 mg/dL

PercentageTime_54_overnight_ManualMode = (CGMManualModeData_index.between_time('0:00:00','05:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[CGMManualModeData_index['Sensor Glucose (mg/dL)'] < 54].groupby('Date')['Sensor Glucose (mg/dL)'].count() / 288 * 100)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

ManualModeData = {
    'metric_1':PercentageTime_180_overnight_ManualMode,
    'metric_2':PercentageTime_250_overnight_ManualMode,
    'metric_3':PercentageTime_70_180_overnight_ManualMode,
    'metric_4':PercentageTime_70_150_overnight_ManualMode,
    'metric_5':PercentageTime_70_overnight_ManualMode,
    'metric_6':PercentageTime_54_overnight_ManualMode,

    'metric_7':PercentageTime_180_daytime_ManualMode,
    'metric_8':PercentageTime_250_daytime_ManualMode,
    'metric_9':PercentageTime_70_180_daytime_ManualMode,
    'metric_10':PercentageTime_70_150_daytime_ManualMode,
    'metric_11':PercentageTime_70_daytime_ManualMode,
    'metric_12':PercentageTime_54_daytime_ManualMode,

    'metric_13':PercentageTime_180_wholeday_ManualMode,
    'metric_14':PercentageTime_250_wholeday_ManualMode,
    'metric_15':PercentageTime_70_180_wholeday_ManualMode,
    'metric_16':PercentageTime_70_150_wholeday_ManualMode,
    'metric_17':PercentageTime_70_wholeday_ManualMode,
    'metric_18':PercentageTime_54_wholeday_ManualMode
}

AutoModeData = {
    'metric_1':PercentageTime_180_overnight_AutoMode,
    'metric_2':PercentageTime_250_overnight_AutoMode,
    'metric_3':PercentageTime_70_180_overnight_AutoMode,
    'metric_4':PercentageTime_70_150_overnight_AutoMode,
    'metric_5':PercentageTime_70_overnight_AutoMode,
    'metric_6':PercentageTime_54_overnight_AutoMode,

    'metric_7':PercentageTime_180_daytime_AutoMode,
    'metric_8':PercentageTime_250_daytime_AutoMode,
    'metric_9':PercentageTime_70_180_daytime_AutoMode,
    'metric_10':PercentageTime_70_150_daytime_AutoMode,
    'metric_11':PercentageTime_70_daytime_AutoMode,
    'metric_12':PercentageTime_54_daytime_AutoMode,

    'metric_13':PercentageTime_180_wholeday_AutoMode,
    'metric_14':PercentageTime_250_wholeday_AutoMode,
    'metric_15':PercentageTime_70_180_wholeday_AutoMode,
    'metric_16':PercentageTime_70_150_wholeday_AutoMode,
    'metric_17':PercentageTime_70_wholeday_AutoMode,
    'metric_18':PercentageTime_54_wholeday_AutoMode
}

# Calculate mean for each metric
def CalculateMean(MetricData):
    if MetricData.size == 0:
        return np.nan
    mean = np.nanmean(MetricData, axis=0)
    return mean

ManualDataMean = {metric: CalculateMean(data) for metric, data in ManualModeData.items()}
AutoDataMean = {metric: CalculateMean(data) for metric, data in AutoModeData.items()}

ManualMode_DataFrame = pd.DataFrame([ManualDataMean], columns = ManualDataMean.keys())
AutoMode_DataFrame = pd.DataFrame([AutoDataMean], columns = AutoDataMean.keys())

# Replace NaN values with 0
ManualMode_DataFrame = ManualMode_DataFrame.fillna(0)
AutoMode_DataFrame = AutoMode_DataFrame.fillna(0)

result_df = pd.concat([ManualMode_DataFrame, AutoMode_DataFrame], axis=0, ignore_index=True)

# Define the file path
file_path = 'Result.csv'

# Write the concatenated DataFrame to a CSV file without headers and index
result_df.to_csv(file_path, header=False, index=False)

#print(result_df)