from data import Data


class Camera:
    """The Camera class have:

        Attributes:
            title : Camera name
            date_from : start date
            date_to : end date
            options : what options the camera has
            data : the camera data
            selected_camera_data : the selected_camera

        Methods:
            get_data() : Function that get the data
            fetch_data() :  Function that fetch the data.
            get_info() : Function that checks if there is data and return info about the camera if there is. Otherwise, it returns
            text that it can't find any data.
            get_info_result() :  Function that show how many accepted, failed, passed or notDone tests have been done.
            get_info_option(option) : Function that checks if there is option and show info about the camera if there is. Otherwise, it returns
            empty text.
            get_sorted_types() : Function that sort the types.
            get_options() : Function that return list of options.
        """
    def __init__(self, title, date_from, date_to):
        self.__title = title
        self.__date_from = date_from
        self.__date_to = date_to

        self.__options = ''
        self.__data = self.fetch_data()
        self.__selected_camera_data = ''

    def get_data(self):
        """
            get_data()
            Function that get the data

            Returns:
                data (DataFrame)
        """
        return self.__data

    def fetch_data(self):
        """
            fetch_data()
            Function that fetch the data.

            Returns:
                self.__selected_camera_data.get_data() (DataFrame)
        """
        self.__selected_camera_data = Data(self.__title, self.__date_from, self.__date_to)
        self.__options = self.__selected_camera_data.get_options()
        return self.__selected_camera_data.get_data()

    def get_info(self):

        """
            get_info()
            Function that checks if there is data and return info about the camera if there is. Otherwise, it returns
            text that it can't find any data.

            Returns:
                'No results found' (sting)
                or
                camera information that includes
                the camera types and
                how many tests were accepted or passed with each type (string)
        """
        if self.__data.empty:
            return "No results found"
        else:
            return f'{self.__data.groupby("CameraType").size().sort_index()}'

    def get_info_result(self):
        """
            get_info_result()
            Function that show how many accepted, failed, passed or notDone tests have been done.

            Returns:
                camera information that includes
                how many accepted, failed, passed or notDone tests (string)
        """
        selected_camera_data = Data(self.__title, self.__date_from, self.__date_to)
        data_test_result = selected_camera_data.get_complete_test_res()
        return f'{data_test_result.groupby("CompleteTestRes").size().sort_index()}'

    def get_info_option(self, option):
        """
            get_info_option()
            Function that checks if there is option and show info about the camera if there is. Otherwise, it returns
            empty text.

            Args:
                option (str) : The option that is selected

            Returns:
                camera information that includes
                how much is the minimum, maximum and average value of a selected option.(string)
        """
        if option == '':
            return ""
        else:
            return f'{self.__data.groupby("CameraType").agg({option:["min", "max", "mean"]})}'

    def get_sorted_types(self):
        """
            get_sorted_types()
            Function that sort the types.

            Returns:
                map(str, values) (map object)
        """
        values = []
        types = self.__data['CameraType'].unique()

        for t in types:
            try:
                int(t)
                values.append(int(t))
            except Exception as e:
                print(e)

        values = sorted(values)
        return map(str, values)

    def get_options(self):
        """
            get_options()
            Function that return list of options.

            Returns:
                options (list)
        """
        options = []
        all_options = self.__options['column_name'].unique()

        for opt in all_options:
            options.append(opt)
        return options

