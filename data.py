from sqlalchemy import create_engine
import pandas as pd

USER = 'sqluser'
PASSWORD = 'Chroma1.0'
HOST = '192.168.86.12'
PORT = 3306
DATABASE = 'production_data'
CONNECTION = create_engine(url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(USER, PASSWORD, HOST, PORT, DATABASE))


class CamerasData:
    """The CamerasData class have:

               Methods:
                  get_cameras_name() : Function that return numpy.ndarray with the names of the cameras.

    """
    def get_cameras_name(self):
        """
            get_cameras_name()
            Function that return numpy.ndarray with the names of the cameras.

            Returns:
                cameras_name.values (numpy.ndarray)
        """
        sql = f"SELECT TABLE_NAME FROM information_schema.tables where TABLE_NAME LIKE '%%TCD-2719-PRNU-Test_Log' and table_schema = 'production_data'"
        cameras_name = pd.read_sql_query(sql, CONNECTION)
        return cameras_name.values

class Data:
    """The MainWindow class inherits QMainWindow and Ui_MainWindow class and have:

               Attributes:
                   table_name :
                   date_from :
                   date_to :

               Methods:
                  get_data() :  Function that return DataFrame with data for selected camera and selected period of time
                  get_options() : Function that return DataFrame with data for every option with decimal or integer values.
                  get_complete_test_res() : Function that return DataFrame with data for all tests, not only the
                  accepted and passed test.
    """
    def __init__(self, table_name, date_from, date_to):
        self.__table_name = table_name
        self.__date_from = date_from
        self.__date_to = date_to

    def get_data(self):
        """
            get_data()
            Function that return DataFrame with data for selected camera and selected period of time.

            Returns:
                data_accepted_passed.set_index('Date') (DataFrame)
        """
        sql = f'SELECT * FROM {self.__table_name} WHERE Date >= "{self.__date_from}" and Date <= "{self.__date_to}" and (CompleteTestRes = "Accepted" or CompleteTestRes = "Passed")'

        data_accepted_passed = pd.read_sql_query(sql, CONNECTION)
        return data_accepted_passed.set_index('Date')

    def get_options(self):
        """
            get_option()
            Function that return DataFrame with data for every option with decimal or integer values.

            Returns:
                data_accepted_passed.set_index('Date') (DataFrame)
        """
        sql = f"SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{self.__table_name}'and (DATA_TYPE = 'decimal' or DATA_TYPE = 'int')"
        options = pd.read_sql_query(sql, CONNECTION)
        return options

    def get_complete_test_res(self):
        """
            get_complete_test_res()
            Function that return DataFrame with data for all tests, not only the accepted and passed test.

            Returns:
                compete_test_res (DataFrame)
        """
        sql = f'SELECT CompleteTestRes FROM {self.__table_name} WHERE Date >= "{self.__date_from}" and Date < "{self.__date_to}"'

        complete_test_res = pd.read_sql_query(sql, CONNECTION)
        return complete_test_res
