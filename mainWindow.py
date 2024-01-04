from PySide6.QtWidgets import QMainWindow, QFileDialog
from ui_mainwindow import Ui_MainWindow
from Charts import Line_Chart, Line_Chart_of_specific_Type, Average_Chart
from Camera import Camera
from data import CamerasData


class MainWindow(QMainWindow, Ui_MainWindow):
    """The MainWindow class inherits QMainWindow and Ui_MainWindow class and have:

               Attributes:
                   ui : Ui_MainWindow()
                   concrete_method : chosen method
                   selected_camera : chosen camera
                   concrete_type : chosen type
                   selected_option : chosen option
                   cameras_data : CamerasData()
                   cameras_name : The names of all cameras that we have in DB

               Methods:
                  set_cameras_name(cameras_name) : Function that set cameras name to comboBox from cameras_name array.
                  create_selected_camera(camera_name) :  Function that creates an object of class Camera.
                  get_date_to() : Function that get an end date.
                  get_date_from() : Function that get the date from which it starts
                  set_info(camera_name) : Function that set information on label_info
                  set_types() : Function that set sorted types on combobox_type
                  set_options() : Function that set options on combobox_type from DB
                  set_option(option) : Function that set the option information on label_info_2
                  create_chart(method) : Function that create Chart object. Depending on what method is chosen, the
                  function makes a different object Line_Chart, Average_Chart or Line_Chart_of_specific_Type.
                  set_concrete_type(concrete_type) : Function that set concrete_type
                  button_click() : Function that, when the button is pressed, checks which method(which charts class) is
                  selected and displays the result.
                  button_export_clicked() :  Function that, when the button is pressed, export the information into CSV.
    """

    def __init__(self):
        super().__init__()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

        self.__concrete_method = ''
        self.__selected_camera = ''
        self.__concrete_type = ''
        self.__selected_option = ''

        # Takes names from DB
        self.__cameras_data = CamerasData()
        self.__cameras_name = self.__cameras_data.get_cameras_name()
        self.set_cameras_name(self.__cameras_name)

        """
        1) User selects the camera
            - the camera information should be displayed
            - the combobox should display the camera types
        """

        self.__ui.comboBox_camera.currentTextChanged.connect(self.set_info)
        self.__ui.comboBox_options.currentTextChanged.connect(self.set_option)

        """
        2) User select the class method
        """

        self.__ui.comboBox_method.currentTextChanged.connect(self.create_chart)

        self.__ui.comboBox_type.currentTextChanged.connect(self.set_concrete_type)

        """
            3) After pressing the button the chart should be displayed 
        """

        self.__ui.pushButton.clicked.connect(self.button_clicked)
        self.__ui.pushButton_Export.clicked.connect(self.button_export_clicked)

    def set_cameras_name(self, cameras_name):
        """
            set_cameras_name(self, cameras_name)
            Function that set cameras name to comboBox from cameras_name array.

            Args:
                cameras_name (numpy.ndarray)
        """
        for camera in cameras_name:
            self.__ui.comboBox_camera.addItem(camera[0])

    def create_selected_camera(self, camera_name):
        """
            get_selected_camera(self, camera_name)
            Function that creates an object of class Camera.

            Args:
                camera_name(str) : this is the name of the camera
        """
        date_to = self.get_date_to()
        date_from = self.get_date_from()

        self.__selected_camera = Camera(camera_name, date_from, date_to)

    def get_date_to(self):
        """
            get_date_to()
            Function that get an end date.

            Returns:
                date_to (str)
        """
        delimiter = '-'
        date_to = self.__ui.dateEdit_to.date().getDate()
        date_to = delimiter.join([str(val) for val in date_to])
        return date_to

    def get_date_from(self):
        """
            get_date_from()
            Function that get the date from which it starts

            Returns:
                date_from (str)
        """
        delimiter = '-'
        date_from = self.__ui.dateEdit_from.date().getDate()
        date_from = delimiter.join([str(val) for val in date_from])
        return date_from

    def set_info(self, camera_name):
        """
            set_info(camera_name)
            Function that set information on label_info

            Args:
                camera_name (str) : this is the name of the camera
        """
        self.create_selected_camera(camera_name)
        info = self.__selected_camera.get_info()
        info_test_result = self.__selected_camera.get_info_result()
        self.set_types()
        self.set_options()

        self.__ui.label_info.setText(info)
        self.__ui.label_label_info_result.setText(info_test_result)

    def set_types(self):
        """
            set_types()
            Function that set sorted types on combobox_type
        """
        types = self.__selected_camera.get_sorted_types()
        self.__ui.comboBox_type.clear()
        self.__ui.comboBox_type.addItem('')
        for cam_type in types:
            self.__ui.comboBox_type.addItem(cam_type)

    def set_options(self):
        """
            set_options()
            Function that set options on combobox_type from DB
        """
        options = self.__selected_camera.get_options()
        self.__ui.comboBox_options.clear()
        self.__ui.comboBox_options.addItem('')
        for opt in options:
            self.__ui.comboBox_options.addItem(opt)

    def set_option(self, option):
        """
            set(self, option)
            Function that set the option information on label_info_2

            Args:
                option (str) : The option that is selected
        """
        self.__selected_option = option
        info = self.__selected_camera.get_info_option(option)
        self.__ui.label_info_option.clear()
        self.__ui.label_info_option.setText(info)

    def create_chart(self, method):
        """
            create_chart(method)
            Function that create Chart object. Depending on what method is chosen, the function makes a different object
            Line_Chart, Average_Chart or Line_Chart_of_specific_Type.

            Args:
                method (str) :The method that is selected
        """
        if method == 'All results sorted by time':
            self.__ui.comboBox_type.setDisabled(True)
            self.__concrete_method = Line_Chart(self.__ui.canvas)
        elif method == 'Average for each type':
            self.__ui.comboBox_type.setDisabled(True)
            self.__concrete_method = Average_Chart(self.__ui.canvas)
        elif method == 'Choose which camera type to show':
            self.__ui.comboBox_type.setDisabled(False)
            self.__concrete_method = Line_Chart_of_specific_Type(self.__ui.canvas)

    def set_concrete_type(self, concrete_type):
        """
            get_concrete_type(concrete_type)
            Function that set concrete_type

            Args:
                concrete_type (str) : The type that is selected
        """
        self.__concrete_type = concrete_type

    def button_clicked(self):
        """
            button_clicked()
            Function that, when the button is pressed, checks which method(which charts class) is selected and displays
            the result.
        """
        data = self.__selected_camera.get_data()
        if isinstance(self.__concrete_method, Line_Chart_of_specific_Type):
            self.__concrete_method.to_show(data, self.__concrete_type, self.__selected_option)
        else:
            self.__concrete_method.to_show(data, self.__selected_option)

    def button_export_clicked(self):
        """
            button_export_clicked()
            Function that, when the button is pressed, export the information into CSV.
        """
        data = self.__selected_camera.fetch_data()
        df = data[self.__selected_option]

        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Save CSV File", f'{self.__selected_option}.csv', "",
                                                   "CSV Files (*.csv)")

        if isinstance(self.__concrete_method, Line_Chart_of_specific_Type):
            filtered_data = df[data['CameraType'] == f'{self.__concrete_type}']
            filtered_data.to_csv(file_path)
        else:
            df.to_csv(file_path)
