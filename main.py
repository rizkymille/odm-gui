import sys
sys.path.append('C:\\ODM')

from opendm import config
from opendm import system
from opendm import io
from opendm.progress import progressbc
from opendm.utils import get_processing_results_paths, rm_r

from stages.odm_app import ODMApp

args = config.config()

app = ODMApp(args)
retcode = app.execute()