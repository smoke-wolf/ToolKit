import csv
import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QTextBrowser, QVBoxLayout, QWidget, QGroupBox, \
    QScrollArea, QHBoxLayout, QPushButton, QDialog

import os
import requests

CACHE_DIR = ".cache"

def cache_command_usage(command_name, usage_text):
    cache_file = os.path.join(CACHE_DIR, f"{command_name}.txt")

    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(cache_file, "w") as f:
        f.write(usage_text)

def load_cached_command_usage(command_name):
    cache_file = os.path.join(CACHE_DIR, f"{command_name}.txt")

    if os.path.isfile(cache_file):
        with open(cache_file, "r") as f:
            return f.read()

    return None



class CommandSearchApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Command Search App")
        self.setGeometry(100, 100, 600, 400)

        # Create GUI elements
        self.keyword_label = QLabel("Enter keyword(s):")
        self.keyword_input = QLineEdit()
        self.search_button = QPushButton("Search")
        self.result_scroll_area = QScrollArea()
        self.result_scroll_area.setWidgetResizable(True)
        self.result_container = QWidget()
        self.result_layout = QVBoxLayout()
        self.result_container.setLayout(self.result_layout)
        self.result_scroll_area.setWidget(self.result_container)

        # Set up the layout
        layout = QVBoxLayout()
        search_group_box = QGroupBox()
        search_layout = QHBoxLayout()
        search_layout.addWidget(self.keyword_label)
        search_layout.addWidget(self.keyword_input)
        search_layout.addWidget(self.search_button)
        search_group_box.setLayout(search_layout)
        layout.addWidget(search_group_box)
        layout.addWidget(self.result_scroll_area)

        # Set the central widget and apply the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connect the search function to the search button's clicked signal
        self.search_button.clicked.connect(self.search_commands)

        # Load the command data from the CSV file
        self.commands = self.load_commands()

    def load_commands(self):
        commands = []
        with open("cms.txt", "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=":")
            for row in reader:
                if len(row) == 2:
                    command_name = row[0].strip()
                    command_description = row[1].strip()
                    commands.append((command_name, command_description))
        return commands

    def search_commands(self):
        keyword = self.keyword_input.text().lower()
        results = []

        # Search for commands that contain the keyword
        for command_name, command_description in self.commands:
            if keyword in command_name.lower() or keyword in command_description.lower():
                results.append((command_name, command_description))

        # Display the search results
        self.display_results(results)

    def display_results(self, results):
        # Clear previous results
        for i in reversed(range(self.result_layout.count())):
            self.result_layout.itemAt(i).widget().setParent(None)

        if results:
            for command_name, command_description in results:
                command_group_box = QGroupBox(command_name)
                command_layout = QVBoxLayout()
                description_label = QLabel(command_description)
                usage_button = QPushButton("Usage")
                usage_button.clicked.connect(lambda _, c=command_name: self.show_command_usage(c))
                command_layout.addWidget(description_label)
                command_layout.addWidget(usage_button)
                command_group_box.setLayout(command_layout)
                self.result_layout.addWidget(command_group_box)
        else:
            no_results_label = QLabel("No results found.")
            self.result_layout.addWidget(no_results_label)

    def show_command_usage(self, command_name):
        cached_usage = load_cached_command_usage(command_name)
        if cached_usage:
            self.display_usage(cached_usage)
        else:
            try:
                url = f"https://ss64.com/osx/{command_name[2:]}.html"
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, "html.parser")
                    pre_element = soup.find("pre")

                    if pre_element:
                        usage_text = pre_element.get_text().strip()
                        if usage_text:
                            self.display_usage(usage_text)
                            cache_command_usage(command_name, usage_text)
                        else:
                            self.display_usage("Usage information not found.")
                    else:
                        self.display_usage("Usage information not found.")
                else:
                    self.display_usage("Failed to fetch usage information.")
            except:
                self.display_usage("Not Connected to the Internet <-> No Cache Exists")

    def display_usage(self, usage_text):
        usage_dialog = QDialog(self)
        usage_dialog.setWindowTitle("Command Usage")
        usage_dialog.setGeometry(200, 200, 600, 400)
        layout = QVBoxLayout()
        text_browser = QTextBrowser()
        text_browser.setPlainText(usage_text)
        layout.addWidget(text_browser)
        usage_dialog.setLayout(layout)
        usage_dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Set the color palette
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(0, 0, 0))  # Set black background
    palette.setColor(QPalette.WindowText, QColor(0, 255, 0))  # Set green text color
    app.setPalette(palette)

    window = CommandSearchApp()
    window.show()
    sys.exit(app.exec_())

