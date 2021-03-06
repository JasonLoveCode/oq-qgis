# -*- coding: utf-8 -*-
"""
/***************************************************************************
 EqCatalogueDialog
                                 A QGIS plugin
 earthquake catalogue tool
                             -------------------
        begin                : 2013-02-20
        copyright            : (C) 2013 by GEM Foundation
        email                : devops@openquake.org
 ***************************************************************************/

# Copyright (c) 2010-2013, GEM Foundation.
#
# OpenQuake is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with OpenQuake. If not, see <http://www.gnu.org/licenses/>.
"""

from PyQt4 import QtCore, QtGui
from ui_eqcatalogue import Ui_EqCatalogue
# create the dialog for zoom to point


class EqCatalogueDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_EqCatalogue()
        self.ui.setupUi(self)
