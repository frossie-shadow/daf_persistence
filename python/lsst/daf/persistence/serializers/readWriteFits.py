#!/usr/bin/env python

#
# LSST Data Management System
# Copyright 2016 LSST Corporation.
#
# This product includes software developed by the
# LSST Project (http://www.lsst.org/).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the LSST License Statement and
# the GNU General Public License along with this program.  If not,
# see <http://www.lsstcorp.org/LegalNotices/>.
#

# -*- python -*-


from .. import serializerRegistry


class PosixReadWriteFits(object):
    """Contains serializer and deserialzer functions that can be registered for any object that has the
    methods writeFits(location, flags) and readFits(location, hdu, flags)"""
    @staticmethod
    def write(object, butlerLocation):
        import pdb; pdb.set_trace()
        locations = butlerLocation.getLocations()
        if len(locations) < 1:
            raise RuntimeError("no location passed in butlerLocation")
        with SafeFilename(locations[0]) as locationString:
            logLoc = LogicalLocation(locationString, additionalData)
            flags = additionalData.getInt("flags", 0)
            obj.writeFits(logLoc.locString(), flags=flags)

    def read(object, butlerLocation):
        import pdb; pdb.set_trace()
        results = []
        for locationString in locations:
            logLoc = LogicalLocation(locationString, additionalData)
            if not os.path.exists(logLoc.locString()):
                raise RuntimeError, "No such FITS catalog file: " + logLoc.locString()
            hdu = additionalData.getInt("hdu", 0)
            flags = additionalData.getInt("flags", 0)
            finalItem = pythonType.readFits(logLoc.locString(), hdu, flags)
        results.append(finalItem)

