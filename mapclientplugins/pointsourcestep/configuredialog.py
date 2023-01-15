'''
MAP Client, a program to generate detailed musculoskeletal models for OpenSim.
    Copyright (C) 2012  University of Auckland
    
This file is part of MAP Client. (http://launchpad.net/mapclient)

    MAP Client is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    MAP Client is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with MAP Client.  If not, see <http://www.gnu.org/licenses/>..
'''
import os
from PySide6 import QtWidgets
from mapclientplugins.pointsourcestep.ui_configuredialog import Ui_Dialog

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class ConfigureDialog(QtWidgets.QDialog):
    '''
    Configure dialog to present the user with the options to configure this step.
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''
        self._previousFileLoc = ''
        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None

        self._location = None

        self._makeConnections()

    def _makeConnections(self):
        self._ui.idLineEdit.textChanged.connect(self.validate)
        self._ui.fileLocButton.clicked.connect(self._fileLocClicked)
        self._ui.fileLocLineEdit.textChanged.connect(self._fileLocEdited)

        # self._ui.colXSpinBox.setValidator(QtGui.QIntValidator())
        # self._ui.colYSpinBox.setValidator(QtGui.QIntValidator())
        # self._ui.colZSpinBox.setValidator(QtGui.QIntValidator())

    def accept(self):
        '''
        Override the accept method so that we can confirm saving an
        invalid configuration.
        '''
        result = QtWidgets.QMessageBox.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(self, 'Invalid Configuration',
                                                   'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            QtWidgets.QDialog.accept(self)

    def validate(self):
        '''
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the 
        overall validity of the configuration.
        '''
        # Determine if the current identifier is unique throughout the workflow
        # The identifierOccursCount method is part of the interface to the workflow framework.
        idValue = self.identifierOccursCount(self._ui.idLineEdit.text())
        idValid = (idValue == 0) or (idValue == 1 and self._previousIdentifier == self._ui.idLineEdit.text())
        if idValid:
            self._ui.idLineEdit.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.idLineEdit.setStyleSheet(INVALID_STYLE_SHEET)

        fileLocValid = os.path.exists(os.path.join(self._location, self._ui.fileLocLineEdit.text()))
        if fileLocValid:
            self._ui.fileLocLineEdit.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.fileLocLineEdit.setStyleSheet(INVALID_STYLE_SHEET)

        valid = idValid and fileLocValid
        # allow settings to be save as long as step id is valid
        self._ui.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(idValid)

        return valid

    def getConfig(self):
        '''
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        '''
        self._previousIdentifier = self._ui.idLineEdit.text()
        self._previousFileLoc = self._ui.fileLocLineEdit.text()
        config = {}
        config['identifier'] = self._ui.idLineEdit.text()
        config['Filename'] = self._ui.fileLocLineEdit.text()
        config['x_column'] = str(self._ui.colXSpinBox.value())
        config['y_column'] = str(self._ui.colYSpinBox.value())
        config['z_column'] = str(self._ui.colZSpinBox.value())
        return config

    def setConfig(self, config):
        '''
        Set the current value of the configuration for the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        '''
        self._previousIdentifier = config['identifier']
        self._previousFileLoc = config['Filename']
        self._ui.idLineEdit.setText(config['identifier'])
        self._ui.fileLocLineEdit.setText(config['Filename'])
        self._ui.colXSpinBox.setValue(int(config['x_column']))
        self._ui.colYSpinBox.setValue(int(config['y_column']))
        self._ui.colZSpinBox.setValue(int(config['z_column']))

    def setWorkflowLocation(self, location):
        self._location = location

    def _fileLocClicked(self):
        location = QtWidgets.QFileDialog.getOpenFileName(self, 'Select File Location', self._previousFileLoc)
        if location[0]:
            self._previousFileLoc = location[0]
            self._ui.fileLocLineEdit.setText(os.path.relpath(location[0], self._location))

    def _fileLocEdited(self):
        self.validate()
