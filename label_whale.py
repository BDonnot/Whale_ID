# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 22:18:05 2015

@author: Benjamin
"""

import sys
sys.path.insert(1, "C:/Anaconda/Lib/site-packages/sloth/bin")
argv = sys.argv+["D:/Users/Benjamin/Documents/Data Science/Whale_ID/cascade/id.json"]
from PyQt4.QtGui import QApplication
from sloth.core.labeltool import LabelTool
from sloth import APP_NAME, ORGANIZATION_NAME, ORGANIZATION_DOMAIN

if __name__ == '__main__':
    app = QApplication(argv)
    app.setOrganizationName(ORGANIZATION_NAME)
    app.setOrganizationDomain(ORGANIZATION_DOMAIN)
    app.setApplicationName(APP_NAME)

    labeltool = LabelTool()
    labeltool.execute_from_commandline(argv)

    sys.exit(app.exec_())