#
# LSST Data Management System
# Copyright 2008, 2009, 2010 LSST Corporation.
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


import unittest
import os

import lsst.utils.tests
from lsst.daf.persistence import DbAuth
from lsst.pex.policy import Policy

# Define the root of the tests relative to this file
ROOT = os.path.abspath(os.path.dirname(__file__))


class DbAuthTestCase(unittest.TestCase):
    """A test case for DbAuth."""

    def setUp(self):
        pol = Policy(os.path.join(ROOT, "testDbAuth.paf"))
        DbAuth.setPolicy(pol)

    def tearDown(self):
        DbAuth.resetPolicy()

    def testSetPolicy(self):
        self.assertTrue(DbAuth.available("lsst-db.ncsa.illinois.edu", "3306"))
        self.assertEqual(DbAuth.authString("lsst-db.ncsa.illinois.edu", "3306"),
                         "test:globular.test")
        self.assertEqual(DbAuth.username("lsst-db.ncsa.illinois.edu", "3306"),
                         "test")
        self.assertEqual(DbAuth.password("lsst-db.ncsa.illinois.edu", "3306"),
                         "globular.test")
        self.assertTrue(DbAuth.available("lsst-db.ncsa.illinois.edu", "3307"))
        self.assertEqual(DbAuth.authString("lsst-db.ncsa.illinois.edu", "3307"),
                         "boris:natasha")
        self.assertEqual(DbAuth.username("lsst-db.ncsa.illinois.edu", "3307"),
                         "boris")
        self.assertEqual(DbAuth.password("lsst-db.ncsa.illinois.edu", "3307"),
                         "natasha")
        self.assertTrue(DbAuth.available("lsst9.ncsa.illinois.edu", "3306"))
        self.assertEqual(DbAuth.authString("lsst9.ncsa.illinois.edu", "3306"),
                         "rocky:squirrel")
        self.assertEqual(DbAuth.username("lsst9.ncsa.illinois.edu", "3306"),
                         "rocky")
        self.assertEqual(DbAuth.password("lsst9.ncsa.illinois.edu", "3306"),
                         "squirrel")


class TestMemory(lsst.utils.tests.MemoryTestCase):
    pass


def setup_module(module):
    lsst.utils.tests.init()

if __name__ == "__main__":
    lsst.utils.tests.init()
    unittest.main()
