import re
import matplotlib
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QMessageBox
matplotlib.use('Qt5Agg')


class Chart:
    """The Chart class have:

        Attributes:
            ax :  encapsulates all the elements of an individual (sub-)plot in a figure.

        Methods:
           show_error_message() : Function that makes a new window to show that there is an error.
           show_color(concrete_option) : Function that checks whether the option name has a 'G' for green, 'R' for red
           or 'B' for blue. If none, still return 'b' for blue.
    """
    def __init__(self):
        self.__ax = None

    def show_error_message(self):
        """
            show_error_message()
            Function that makes a new window to show that there is an error.
        """
        error_message = "No results found"
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle("Error")
        error_box.setText(error_message)
        error_box.exec_()

    def show_color(self, concrete_option):
        """
            show_color()
            Function that checks whether the option name has a 'G' for green, 'R' for red or 'B' for blue. If none,
            still return 'b' for blue.

            Arg:
               concrete_option (str) : The option that is selected

            Returns:
                 'g', 'r', or 'b'(str)
        """
        if re.search("G{1}$", concrete_option):
            return 'g'

        elif re.search("R{1}$", concrete_option):
            return 'r'
        else:
            return 'b'


class Line_Chart(Chart):
    """The Line_Chart class inherits Chart class and have:

        Attributes:
            canvas : FigureCanvasQTAgg

        Methods:
           to_show(data, concrete_option) : Function that draws the data on the canvas according to the selected method.
    """
    def __init__(self, canvas):
        super().__init__()
        self.__canvas = canvas

    def to_show(self, data, concrete_option):
        """
            to_show(data, concrete_option)
            Function that draws the data on the canvas according to the selected method.

            Args:
                data (DataFrame) :
                concrete_option (str) : The option that is selected
        """
        self.__canvas.figure.clear()
        self.__ax = self.__canvas.figure.add_subplot(111)

        try:
            color = self.show_color(concrete_option)
            data.plot(y=[f'{concrete_option}'], color=[f'{color}'], figsize=(12, 8), ax=self.__ax)


            plt.grid(axis='y')
            self.__canvas.draw()
        except:
            self.__canvas.figure.clear()
            self.__canvas.draw()
            self.show_error_message()


class Average_Chart(Chart):
    """The Line_Chart class inherits Chart class and have:

           Attributes:
               canvas : FigureCanvasQTAgg

           Methods:
              to_show(data, concrete_option) : Function that draws the data on the canvas according to the selected method.
    """
    def __init__(self, canvas):
        super().__init__()
        self.__canvas = canvas

    def to_show(self, data, concrete_option):
        """
            to_show(data, concrete_option)
            Function that draws the data on the canvas according to the selected method.

            Args:
                data (DataFrame) :
                concrete_option (str) : The option that is selected
        """
        self.__canvas.figure.clear()
        self.__ax = self.__canvas.figure.add_subplot(111)

        try:
            data.groupby('CameraType').agg({f'{concrete_option}': ['min', 'max', 'mean']}).plot(kind='bar',
                                                                                                figsize=(12, 8),
                                                                                                ax=self.__ax)
            plt.grid(axis='y')
            self.__canvas.draw()
        except:
            self.__canvas.figure.clear()
            self.__canvas.draw()
            self.show_error_message()


class Line_Chart_of_specific_Type(Chart):
    """The Line_Chart class inherits Chart class and have:

           Attributes:
               method : selected method
               canvas : FigureCanvasQTAgg

           Methods:
              to_show(data, concrete_option) : Function that draws the data on the canvas according to the selected method.
    """
    def __init__(self, canvas, method='Choose which camera type to show'):
        super().__init__()
        self.__method = method
        self.__canvas = canvas

    def to_show(self, data, camera_type, concrete_option):
        """
            to_show(data, concrete_option)
            Function that draws the data on the canvas according to the selected method.

            Args:
                data (DataFrame) :
                camera_type (str) : The type that is selected
                concrete_option (str) : The option that is selected
        """
        self.__canvas.figure.clear()
        self.__ax = self.__canvas.figure.add_subplot(111)

        try:
            color = self.show_color(concrete_option)
            data[data.CameraType == camera_type].plot(y=[f'{concrete_option}'], color=[f'{color}'], figsize=(12, 8),
                                                      ax=self.__ax)
            plt.grid(axis='y')
            self.__canvas.draw()
        except:
            self.__canvas.figure.clear()
            self.__canvas.draw()
            self.show_error_message()
