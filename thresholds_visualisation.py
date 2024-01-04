import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

USER = 'sqluser'
PASSWORD = 'Chroma1.0'
HOST = '192.168.86.12'
PORT = 3306
DATABASE = 'production_data'
engine = create_engine(url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(USER, PASSWORD, HOST, PORT, DATABASE))

# Изтегляне на информацията от първата таблица като DataFrame
query1 = "SELECT `maxBlackSignalValue`, blRefMax_10_R FROM `allPIXAevo_Thresholds` RIGHT join allPIXAevo_FinalTest on allPIXAevo_FinalTest.ID = FinalTestID where CompleteTestRes='passed' or CompleteTestRes = 'accepted'"
df = pd.read_sql(query1, engine)
print(df)

# Визуализиранее на информацията с Matplotlib (Тук показвам само прост график)
plt.figure(figsize=(10, 6))
plt.plot(df['maxBlackSignalValue'], label='maxBlackSignalValue')
plt.plot(df['blRefMax_10_R'], label='blRefMax_10_R')
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Data from SQL Query')
plt.legend()
plt.show()


engine.dispose()