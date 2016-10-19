from . import code_v1 as code
from .common import *

# import json # included in common
# import time # included in common
# from django.http import HttpResponse # included in common
# from django.core.handlers.wsgi import WSGIRequest # included in common
# from django.core.exceptions import SuspiciousOperation # included in common
# from breeze.utilities import * # included in common
# from breeze.utils import pp
# from django.core.urlresolvers import reverse
# from django.conf import settings
# from django import http
# from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
# from django.template.context import RequestContext
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect


#########
# VIEWS #
#########


# clem 17/10/2016
def hook(_):
	return code.get_response()


# clem 17/10/2016
@csrf_exempt
def reload_sys(request):
	payload, rq = code.get_git_hub_json(request)
	if payload:
		allow_filter = {
			'ref'                 : settings.GIT_AUTO_REF,
			'repository.id'       : "70237993",
			'repository.full_name': 'Fclem/isbio2',
			'pusher.name'         : 'Fclem',
			'sender.id'           : "6617239",
		}
		if match_filter(payload, allow_filter):
			logger.info(
				'Received system reload from GitHub, pulling (django should reload itself if any change occurs) ...')
			result = code.do_self_git_pull()
			return get_response(result, payload)
		else:
			return HttpResponseNotModified('')
		
	# raise default_suspicious(request)
	return HttpResponseBadRequest
	
	
# clem 17/10/2016
@csrf_exempt
def git_hook(request):
	payload, rq = code.get_git_hub_json(request)
	if payload:
		allow_filter = {
			'ref'                 : "refs/heads/master",
			'repository.id'       : "70131764", # "DSRT-v2"
		}
		if match_filter(payload, allow_filter):
			logger.info('Received git push event for R code')
			result = code.do_r_source_git_pull()
			return get_response(data=payload) if result else get_response_opt(http_code=HTTP_NOT_IMPLEMENTED)
		else:
			return HttpResponseNotModified('')
	
	# raise default_suspicious(request)
	return HttpResponseBadRequest
