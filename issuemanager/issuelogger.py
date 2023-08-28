import json
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QDialog,
    QPushButton, QHBoxLayout, QVBoxLayout, QScrollArea,
    QMessageBox, QListWidget, QListWidgetItem
)
from PyQt5.QtCore import Qt
Issuefile = input('Enter File To Log Errors To: )

class Issue:
    def __init__(self, title, description):
        self.title = title
        self.description = description


class IssueDialog(QDialog):
    def __init__(self, issue):
        super().__init__()

        # Create UI elements
        self.title_label = QLabel('Title:')
        self.title_input = QLineEdit(issue.title)
        self.description_label = QLabel('Description:')
        self.description_input = QTextEdit(issue.description)
        self.save_button = QPushButton('Save')
        self.delete_button = QPushButton('Delete')

        # Create layout
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.title_label)
        input_layout.addWidget(self.title_input)
        input_layout.addWidget(self.description_label)
        input_layout.addWidget(self.description_input)
        input_layout.addWidget(self.save_button)
        input_layout.addWidget(self.delete_button)

        self.setLayout(input_layout)

        # Connect signals and slots
        self.save_button.clicked.connect(self.accept)
        self.delete_button.clicked.connect(self.delete_issue)

    def get_issue(self):
        # Get updated issue details
        title = self.title_input.text()
        description = self.description_input.toPlainText()
        return Issue(title, description)

    def delete_issue(self):
        self.done(QMessageBox.DestructiveRole)


class IssueTracker(QWidget):
    def __init__(self):
        super().__init__()

        # Create UI elements
        self.title_label = QLabel('Title:')
        self.title_input = QLineEdit()
        self.description_label = QLabel('Description:')
        self.description_input = QTextEdit()
        self.save_button = QPushButton('Save')
        self.search_input = QLineEdit()
        self.search_button = QPushButton('Search')
        self.issue_list = QListWidget()

        # Create layout
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.title_label)
        input_layout.addWidget(self.title_input)
        input_layout.addWidget(self.description_label)
        input_layout.addWidget(self.description_input)
        input_layout.addWidget(self.save_button)
        input_layout.addWidget(self.search_input)
        input_layout.addWidget(self.search_button)

        main_layout = QHBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.issue_list)

        self.setLayout(main_layout)

        # Connect signals and slots
        self.save_button.clicked.connect(self.save_issue)
        self.search_button.clicked.connect(self.search_issues)
        self.issue_list.itemDoubleClicked.connect(self.edit_issue)
        self.issue_list.itemPressed.connect(self.select_issue)

        # Initialize data
        self.issues = self.load_issues()

        # Populate issue list UI with saved issues
        self.update_list_widget()

    def load_issues(self):
        try:
            with open('issue file', 'r') as file:
                issues = json.load(file)
                return [Issue(issue['title'], issue['description']) for issue in issues]
        except FileNotFoundError:
            return []

    def save_issues(self):
        with open('v1.3.8.txt', 'w') as file:
            json.dump([{'title': issue.title, 'description': issue.description} for issue in self.issues], file)

    def save_issue(self):
        issue = Issue(
            title=self.title_input.text(),
            description=self.description_input.toPlainText()

        )
        self.issues.append(issue)
        self.update_list_widget()

        # Save issues to file
        self.save_issues()

    def edit_issue(self, item):
        # Get selected issue
        issue = self.get_selected_issue()

        # Open issue dialog with
        dialog = IssueDialog(issue)
        # Show the dialog and get updated issue details
        if dialog.exec_() == QDialog.Accepted:
            updated_issue = dialog.get_issue()

            # Update issue list with updated issue
            index = self.issues.index(issue)
            self.issues[index] = updated_issue

            # Update issue list UI with updated issue
            item.setText(updated_issue.title)
            self.update_list_widget()

            # Save issues to file
            self.save_issues()

    def delete_issue(self, item):
        # Get selected issue
        issue = self.get_selected_issue()

        # Remove issue from issue list
        self.issues.remove(issue)

        # Remove issue from issue list UI
        self.issue_list.takeItem(self.issue_list.row(item))

        # Save issues to file
        self.save_issues()

    def select_issue(self, item):
        # Get selected issue
        issue = self.get_selected_issue()

        # Update input fields with selected issue details
        self.title_input.setText(issue.title)
        self.description_input.setText(issue.description)

    def search_issues(self):
        # Get search query
        query = self.search_input.text()

        # Filter issues based on search query
        filtered_issues = [issue for issue in self.issues if query.lower() in issue.title.lower()]

        # Update issue list UI with filtered issues
        self.update_list_widget(filtered_issues)

    def get_selected_issue(self):
        # Get selected issue
        selected_item = self.issue_list.currentItem()
        index = self.issue_list.row(selected_item)
        return self.issues[index]

    def update_list_widget(self, issues=None):
        # Clear current items in issue list UI
        self.issue_list.clear()

        # If no issues provided, use all issues
        if issues is None:
            issues = self.issues

        # Add each issue to issue list UI
        for issue in issues:
            item = QListWidgetItem(issue.title)
            self.issue_list.addItem(item)

    def closeEvent(self, event):
        # Save issues to file when application is closed
        self.save_issues()
        event.accept()

app = QApplication(sys.argv)
issue_tracker = IssueTracker()
issue_tracker.show()
sys.exit(app.exec_())