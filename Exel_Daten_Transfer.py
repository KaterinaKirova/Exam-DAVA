from sqlalchemy import create_engine
import pandas as pd

USER = 'sqluser'
PASSWORD = 'Chroma1.0'
HOST = '192.168.86.12'
PORT = 3306
DATABASE = 'production_data_test'

excel_file = 'D:\Katerina\EMVA-TEST\TCD-2719-PRNU-Test_Log_new.xlsx'
df = pd.read_excel(excel_file, header=1, skiprows=[2])

engine = create_engine(url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(USER, PASSWORD, HOST, PORT, DATABASE))


df.to_sql(name='TCD-2719-PRNU-Test_Log_2023_12', con=engine, if_exists='replace', index=True)



#result_df = pd.read_sql('SELECT * FROM TCD-2719-PRNU-Test_Log_2023_12', con=engine)
#print(result_df)

