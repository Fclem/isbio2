from isbio.settings import MEDIA_ROOT, TEMPLATE_FOLDER, REPORTS_FN, MOULD_FOLDER

# FIXME obsolete
# SHINY_APPS = MEDIA_ROOT + 'shinyApps/'
SHINY_FN_REPORTS = 'shinyReports'
SHINY_FN_TAGS = 'shinyTags'
SHINY_FN_TEMPLATE = 'shiny_templates'
SHINY_TAGS = '%s%s/' % (MEDIA_ROOT, SHINY_FN_TAGS)
SHINY_REPORTS = '%s%s/' % (MEDIA_ROOT, SHINY_FN_REPORTS)
SHINY_REPORT_TEMPLATE_PATH = '%s%s/' % (TEMPLATE_FOLDER, SHINY_FN_TEMPLATE)
SHINY_ORIG_TARGET_URL = '%s/breeze/'
SHINY_ORIG_STANDALONE_URL = '%s/apps/'
SHINY_ORIG_LIBS_TARGET_URL = '%s/libs/'
# local Shiny
SHINY_LOCAL_ENABLE = True
SHINY_LOCAL_IP = '127.0.0.1:3838'
SHINY_LOCAL_TARGET_URL = 'http://' + SHINY_ORIG_TARGET_URL % SHINY_LOCAL_IP
SHINY_LOCAL_LIBS_TARGET_URL = 'http://' + SHINY_ORIG_LIBS_TARGET_URL % SHINY_LOCAL_IP
SHINY_LOCAL_LIBS_BREEZE_URL = '/libs/'
SHINY_LOCAL_STANDALONE_BREEZE_URL = 'http://' + SHINY_ORIG_STANDALONE_URL % SHINY_LOCAL_IP
# remote Shiny
SHINY_REMOTE_ENABLE = True
# SHINY_REMOTE_IP = 'vm0326.kaj.pouta.csc.fi:3838'
SHINY_REMOTE_IP = 'vm0326.kaj.pouta.csc.fi'
SHINY_REMOTE_LOCAL_PATH = '/shiny-csc/'
SHINY_REMOTE_CSC_LOCAL_PATH = '/home/shiny/shiny/'
SHINY_REMOTE_BREEZE_REPORTS_PATH = SHINY_REMOTE_LOCAL_PATH + REPORTS_FN
SHINY_REMOTE_REPORTS = '%s%s/' % (SHINY_REMOTE_LOCAL_PATH, SHINY_FN_REPORTS)
SHINY_REMOTE_REPORTS_INTERNAL = '%s%s/' % (SHINY_REMOTE_CSC_LOCAL_PATH, SHINY_FN_REPORTS)
SHINY_REMOTE_TAGS = '%s%s/' % (SHINY_REMOTE_LOCAL_PATH, SHINY_FN_TAGS)
SHINY_REMOTE_TAGS_INTERNAL = '%s%s/' % (SHINY_REMOTE_CSC_LOCAL_PATH, SHINY_FN_TAGS)
# SHINY_REMOTE_PROTOCOL = 'http'
SHINY_REMOTE_PROTOCOL = 'https'
SHINY_REMOTE_TARGET_URL = '%s://' % SHINY_REMOTE_PROTOCOL + SHINY_ORIG_TARGET_URL % SHINY_REMOTE_IP
SHINY_REMOTE_LIBS_TARGET_URL = '%s://' % SHINY_REMOTE_PROTOCOL + SHINY_ORIG_LIBS_TARGET_URL % SHINY_REMOTE_IP
SHINY_REMOTE_LIBS_BREEZE_URL = '/libs/'

# LEGACY ONLY (single Shiny old system)
SHINY_MODE = 'local'
SHINY_PUB_REDIRECT = 'http://breeze-dev.giu.fi:8080/'

SHINY_HEADER_FILE_NAME = 'header.R'
SHINY_LOADER_FILE_NAME = 'loader.R'
SHINY_GLOBAL_FILE_NAME = 'global.R'
SHINY_UI_FILE_NAME = 'ui.R'
SHINY_SERVER_FILE_NAME = 'server.R'
SHINY_FILE_LIST = 'files.json'
# SHINY_SERVER_FOLDER = 'scripts_server/'
# SHINY_UI_FOLDER = 'scripts_body/'
# SHINY_SERVER_FOLDER = 'scripts_server/'
SHINY_RES_FOLDER = 'www/'
# SHINY_DASH_UI_FILE = 'dash_ui.R'
# HINY_DASH_SERVER_FILE = 'dashboard_serverside.R'
# SHINY_DASH_UI_FN = SHINY_UI_FOLDER + SHINY_DASH_UI_FILE
# SHINY_DASH_SERVER_FN = SHINY_SERVER_FOLDER + SHINY_DASH_SERVER_FILE
SHINY_TAG_CANVAS_FN = 'shinyTagTemplate.zip'
SHINY_TAG_CANVAS_PATH = MOULD_FOLDER + SHINY_TAG_CANVAS_FN
SHINY_MIN_FILE_SIZE = 14 # library(shiny) is 14 byte long
# NOZZLE_TARGET_URL = 'http://' + FULL_HOST_NAME + '/'
# Install shiny library : install.packages('name of the lib', lib='/usr/local/lib/R/site-library', dependencies=TRUE)
SHINY_URL = '/shiny/rep/' # FIXME
