# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2014, Numenta, Inc.  Unless you have purchased from
# Numenta, Inc. a separate commercial license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------
import json

from cerebro2.paths import Paths



class Fetch:


  def __init__(self, dataDir):
    self.paths = Paths(dataDir)


  def getDimensions(self, layer):
    return readJSON(self.paths.dimensions(layer))


  def getActiveCells(self, layer, iteration):
    return readJSON(self.paths.activeCells(layer, iteration))


  def getActiveColumns(self, layer, iteration):
    return readJSON(self.paths.activeColumns(layer, iteration))



def readJSON(filepath):
  with open(filepath, 'r') as infile:
    return json.load(infile)
