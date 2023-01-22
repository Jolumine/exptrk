from PyQt5.QtWidgets import QPushButton, QDialog, QComboBox, QLabel, QHBoxLayout, QVBoxLayout, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon

from exptrk.templates.settings.Modify.Modify import Modify_Window
from exptrk.templates.dialogs.Confirm import Confirm

from exptrk.utils.get_currency import get_currency
from exptrk.utils.get_categorys import get_categorys
from exptrk.const import CURRENCYS

import json

class Settings(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.settings = "./.data/settings.json"
        self.user = "./.data/user.json"

        self.currency_label = QLabel("Currency")

        self.currencys = QComboBox(self)
        self.currencys.addItems(CURRENCYS)
        self.currencys.setCurrentText(f"{get_currency()[0]}/{get_currency()[1]}")

        self.category_label = QLabel("Categorys:")

        self.categorys = QComboBox(self)
        self.categorys.addItems(get_categorys())

        self.create_category = QPushButton("", self)
        self.create_category.setIcon(QIcon("assets/create.png"))
        self.create_category.setFixedHeight(30)
        self.create_category.setFixedWidth(30)
        self.create_category.setToolTip("Click to create a new category.")
        self.create_category.clicked.connect(self.toggle)

        self.delete_category = QPushButton("", self)
        self.delete_category.setIcon(QIcon("assets/delete.png"))
        self.delete_category.setFixedHeight(30)
        self.delete_category.setFixedWidth(30)
        self.delete_category.setToolTip("Click to delete the selected category.")
        self.delete_category.clicked.connect(self.delete)

        # Toggled Widgets

        self.create_name = QLineEdit(self)
        self.create_name.setPlaceholderText("Name")
        self.create_name.hide()

        self.confirm = QPushButton("", self)
        self.confirm.setIcon(QIcon("assets/confirm.png"))
        self.confirm.setToolTip("Click to create category.")
        self.confirm.clicked.connect(self.confirm_creation)
        self.confirm.hide()

        self.cancel = QPushButton("", self)
        self.cancel.setIcon(QIcon("assets/cancel.png"))
        self.cancel.setToolTip("Click to cancel the creation.")
        self.cancel.clicked.connect(self.cancel_creation)
        self.cancel.hide()

        self.toggled_layout = QHBoxLayout()
        self.toggled_layout.addWidget(self.create_name)
        self.toggled_layout.addWidget(self.confirm)
        self.toggled_layout.addWidget(self.cancel)

        # ----------------------------
        
        self.modify_label = QLabel("Modify user:")

        self.modify_button = QPushButton("Modify", self)
        self.modify_button.setToolTip("Click to modify the user information.")
        self.modify_button.clicked.connect(self.modify_user)

        self.savebtn = QPushButton("Save", self)
        self.savebtn.setToolTip("Click to save the selected settings.")
        self.savebtn.clicked.connect(self.save)

        self.currency_layout = QHBoxLayout()
        self.currency_layout.addWidget(self.currency_label)
        self.currency_layout.addWidget(self.currencys)

        self.categorys_layout = QHBoxLayout()
        self.categorys_layout.addWidget(self.category_label)
        self.categorys_layout.addWidget(self.categorys)
        self.categorys_layout.addWidget(self.create_category)
        self.categorys_layout.addWidget(self.delete_category)

        self.mod_layout = QHBoxLayout()
        self.mod_layout.addWidget(self.modify_label)
        self.mod_layout.addWidget(self.modify_button)
        
        self.root = QVBoxLayout()
        self.root.addLayout(self.currency_layout)
        self.root.addLayout(self.categorys_layout)
        self.root.addLayout(self.mod_layout)
        self.root.addWidget(self.savebtn)

        self.setWindowTitle("Settings")
        self.setWindowIcon(QIcon("assets/settings.png"))
        self.setGeometry(175, 300, 500, 350)
        self.setLayout(self.root)
        self.exec_()

    def render(self):
        self.currencys.clear()
        self.currencys.addItems(CURRENCYS)
        self.currencys.setCurrentText(f"{get_currency()[0]}/{get_currency()[1]}")

        self.categorys.clear()
        self.categorys.addItems(get_categorys())

    def toggle(self):
        self.root.removeItem(self.mod_layout)
        self.root.removeItem(self.reset_layout)
        self.root.removeWidget(self.export_button)
        self.root.removeWidget(self.savebtn)

        self.create_name.show()
        self.confirm.show()
        self.cancel.show()
        self.create_category.setDisabled(True)
        self.delete_category.setDisabled(True)

        self.root.addLayout(self.toggled_layout)
        self.root.addLayout(self.mod_layout)
        self.root.addLayout(self.reset_layout)
        self.root.addWidget(self.export_button)
        self.root.addWidget(self.savebtn)

    def cancel_creation(self):
        self.root.removeItem(self.toggled_layout)

        self.confirm.hide()
        self.cancel.hide()
        self.create_name.hide()
        self.create_category.setDisabled(False)
        self.delete_category.setDisabled(False)
    
    def confirm_creation(self):
        window = Confirm(200, 300, "Confirm", "Confirm the creation.")
        rep = window.exec_()

        if rep == QMessageBox.Apply:
            with open(self.user, "r") as f: 
                parsed = json.load(f)
                f.close()

            parsed["Categorys"].append(self.create_name.text())

            with open(self.user, "w") as f: 
                json.dump(parsed, f, indent=4, sort_keys=False)

            self.root.removeItem(self.toggled_layout)
            self.confirm.hide()
            self.cancel.hide()
            self.create_name.hide()
            self.create_category.setDisabled(False)
            self.delete_category.setDisabled(False)

            self.render()
        else: 
            self.cancel_creation()


    def delete(self): 
        selected = self.categorys.currentText()

        if selected != "":
            window = Confirm(200, 300, "Confirm", "Confirm the deletion.")
            rep = window.exec_()
            if rep == QMessageBox.Apply:
                with open(self.user, "r") as f: 
                    parsed = json.load(f)
                    f.close()

                with open(self.user, "w") as f: 
                    parsed["Categorys"].remove(selected)
                    json.dump(parsed, f, indent=4, sort_keys=False)
                    f.close()

                self.render()
            else: 
                pass
        else: 
            # TODO Add error
            pass


    def modify_user(self): 
        return Modify_Window()

    def save(self):
        currency = self.currencys.currentText()

        settings = {
            "currency": currency, 
        }

        parsed = json.dumps(settings, indent=4, sort_keys=False)

        with open(self.settings, "w") as f: 
            f.write(parsed)
            f.close()

        self.close()
