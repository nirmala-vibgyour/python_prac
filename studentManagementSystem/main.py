from PyQt6.QtWidgets import QWidget, \
    QApplication, QGridLayout, QLineEdit, \
    QLabel, QPushButton, QComboBox, QMainWindow, QTableWidget, \
    QTableWidgetItem, QDialog, QVBoxLayout, QToolBar, QStatusBar, \
    QMessageBox
from PyQt6.QtGui import QAction, QIcon
from PyQt6 import QtCore
import sys
import sqlite3


class DatabaseConnection:
    def __init__(self, databaseFile = "database.db"):
        self.databaseFile = databaseFile

    def connect(self):
        connection = sqlite3.connect(self.databaseFile)
        return connection


""" QMainWindow provides the way to add nav, tool, status bar. """


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setMinimumSize(800, 600)

        fileMenuItem = self.menuBar().addMenu("&File")
        helpMenuItem = self.menuBar().addMenu("&Help")
        editMenuItem = self.menuBar().addMenu("&Edit")

        addStudenAction = QAction(QIcon("icons/add.png"), "Add Student", self)
        addStudenAction.triggered.connect(self.insert)
        fileMenuItem.addAction(addStudenAction)

        aboutAction = QAction("About", self)
        helpMenuItem.addAction(aboutAction)
        aboutAction.triggered.connect(self.about)

        searchAction = QAction(QIcon("icons/search.png"), "Search", self)
        editMenuItem.addAction(searchAction)
        searchAction.triggered.connect(self.search)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(addStudenAction)
        toolbar.addAction(searchAction)

        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        self.table.cellClicked.connect(self.cellClicked)

    def cellClicked(self):
        editButton = QPushButton("Edit Record")
        editButton.clicked.connect(self.edit)

        deleteButton = QPushButton("Delete Record")
        deleteButton.clicked.connect(self.delete)

        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        self.statusbar.addWidget(editButton)
        self.statusbar.addWidget(deleteButton)

    def loadTable(self):
        connection = DatabaseConnection().connect()
        result = connection.execute("SELECT * From students")
        self.table.setRowCount(0)
        for rowNum, rowData in enumerate(result):
            self.table.insertRow(rowNum)
            for colNum, data in enumerate(rowData):
                self.table.setItem(rowNum, colNum, QTableWidgetItem(str(data)))

        connection.close()

    def about(self):
        dialog = AboutDialog()
        dialog.exec()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def search(self):
        dialog = SearchDialog()
        dialog.exec()

    def edit(self):
        dialog = EditDialog()
        dialog.exec()

    def delete(self):
        dialog = DeleteDialog()
        dialog.exec()


class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        content = """
        This app was created during the course "The Python Mega Course".
        Feel free to modify and reuse this app.
        """
        self.setText(content)


class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        index = studentManagementSystem.table.currentRow()
        studentName = studentManagementSystem.table.item(index, 1).text()
        self.studentName = QLineEdit(studentName)
        self.studentName.setPlaceholderText("Name")
        layout.addWidget(self.studentName)

        self.studentId = studentManagementSystem.table.item(index, 0).text()

        courseName = studentManagementSystem.table.item(index, 2).text()
        self.courseName = QComboBox()
        courses = ["Astronomy", "Biology", "Math", "Physics"]
        self.courseName.addItems(courses)
        self.courseName.setCurrentText(courseName)
        layout.addWidget(self.courseName)

        mobile = studentManagementSystem.table.item(index, 3).text()
        self.mobile = QLineEdit(mobile)
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        button = QPushButton("Update", self)
        button.clicked.connect(self.updateStudent)
        layout.addWidget(button)

    def updateStudent(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET name = ?, course = ?, mobile = ? WHERE id = ?",
                       (self.studentName.text(), self.courseName.itemText(self.courseName.currentIndex()),
                        self.mobile.text(), self.studentId))
        connection.commit()
        cursor.close()
        connection.close()
        studentManagementSystem.loadTable()


class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Student Data")
        # self.setFixedWidth(300)
        # self.setFixedHeight(300)

        layout = QGridLayout()
        self.setLayout(layout)

        confirmation = QLabel("Are you sure... that you want to delete this record?")
        yes = QPushButton("Yes")
        no = QPushButton("No")

        layout.addWidget(confirmation, 0, 0, 1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 1)

        yes.clicked.connect(self.deleteStudent)

    def deleteStudent(self):
        index = studentManagementSystem.table.currentRow()
        studentId = studentManagementSystem.table.item(index, 0).text()

        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("DELETE from students WHERE id = ?", (studentId, ))
        connection.commit()
        cursor.close()
        connection.close()
        studentManagementSystem.loadTable()

        self.close()

        confirmationWidget = QMessageBox()
        confirmationWidget.setWindowTitle("Success")
        confirmationWidget.setText("Record deleted successfully!!")
        confirmationWidget.exec()


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.studentName = QLineEdit()
        self.studentName.setPlaceholderText("Name")
        layout.addWidget(self.studentName)

        self.courseName = QComboBox()
        courses = ["Astronomy", "Biology", "Math", "Physics"]
        self.courseName.addItems(courses)
        layout.addWidget(self.courseName)

        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        button = QPushButton("Register", self)
        button.clicked.connect(self.addStudent)
        layout.addWidget(button)

    def addStudent(self):
        name = self.studentName.text()
        course = self.courseName.itemText(self.courseName.currentIndex())
        mobile = self.mobile.text()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
                       (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        studentManagementSystem.loadTable()


class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Search Student")
        self.setFixedWidth(300)
        self.setFixedWidth(300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.studentName = QLineEdit()
        self.studentName.setPlaceholderText("Name")
        layout.addWidget(self.studentName)

        button = QPushButton("Search")
        button.clicked.connect(self.search)
        layout.addWidget(button)

    def search(self):
        name = self.studentName.text()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        rows = list(result)
        items = studentManagementSystem.table.findItems(name, QtCore.Qt.MatchFlag.MatchFixedString)
        for item in items:
            studentManagementSystem.table.item(item.row(), 1).setSelected(True)

        cursor.close()
        connection.close()


app = QApplication(sys.argv)
studentManagementSystem = MainWindow()
studentManagementSystem.show()
studentManagementSystem.loadTable()
sys.exit(app.exec())


# example of code smells:
# unclear names
# long methods
# repeated number of lines
# not commented
# fixing the algorithm to speed up the code execution
