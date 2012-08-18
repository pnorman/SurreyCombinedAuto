#!/usr/bin/env python

import zipfile
import sys
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO as StringIO
import urllib2

urlbase = "http://media.surrey.ca/files/"

outputdir = "./SurreyData"

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'OSMSurreyGenerate (contact: penorman@mac.com)')]
urllib2.install_opener(opener)

'''
Skip SurreyDrainage

add:

trnRoadCentrelinesSHP.shp
cadSurveyMonumentsSHP.shp
'''

files = {
            'SurreyEnvironment':      [ 'drnOpenChannelsSHP', 'drnWaterBodiesSHP', 'prkNaturalAreasSHP'],
            'SurreyPlanning':         [ 'lndZoningBoundaries', 'lndOfficialCommunityPlan', 'facSchools', 
                                        'facFacilities', 'facBuildings'],
            'SurreyProperty':         [ 'cadSurveyMonumentsSHP', 'cadLotsSHP',
                                        'cadAddressesSHP'],
            'SurreyTransportation':   [ 'trnRoadCentrelinesSHP', 'trnTrafficSignalsSHP', 'trnSidewalksSHP',
                                        'trnPolesSHP', 'trnNonMotorizedRoutesSHP', 'trnMedians', 'trnBarriers'],
            'SurreyWater':            [ 'wtrHydrantsSHP' ]
}
for file, layers in files.items():
    print 'Fetching ' + file
    zipobj = zipfile.ZipFile(StringIO.StringIO(urllib2.urlopen(urlbase + file + '.zip').read()), 'r')
    for layer in layers:
        zipobj.extract(layer + '.dbf', outputdir)
        zipobj.extract(layer + '.prj', outputdir)
        zipobj.extract(layer + '.shp', outputdir)
        zipobj.extract(layer + '.shx', outputdir)
