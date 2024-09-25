from PyQt6.QtWidgets import QMainWindow, QTextEdit, \
    QLineEdit, QPushButton, QApplication
import sys
from backend import Chatbot
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500)

        self.chatArea = QTextEdit(self)
        self.chatArea.setGeometry(10, 10, 480, 320)
        self.chatArea.setReadOnly(True)

        self.inputField = QLineEdit(self)
        self.inputField.setGeometry(10, 340, 480, 40)
        self.inputField.returnPressed.connect(self.sendMessage)

        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.sendMessage)

        self.show()

    def sendMessage(self):
        userInput = self.inputField.text().strip()
        self.chatArea.append(f"<p style='color: #333333'>Me: {userInput}</p>")
        self.inputField.clear()

        thread = threading.Thread(target=self.getBotResponse, args=(userInput,))
        thread.start()

    def getBotResponse(self, userInput):
        response = self.chatbot.getResponse(userInput)
        self.chatArea.append(f"<p style='color: #333333; background-color: #E9E9E9'>Bot: {response}</p>")


app = QApplication(sys.argv)
mainWindow = ChatbotWindow()
sys.exit(app.exec())

# sk-gckXkmKf_BZTaEs8K5xKC7nHeMDHzLuC6Qqh-U1j-IT3BlbkFJKFLPJMytpUBaz9iu73ZxAOHnqBDkxF3s8Zdh3Yk3wA