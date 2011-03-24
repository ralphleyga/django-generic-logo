from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader, RequestContext, Context
from django.contrib.contenttypes.models import ContentType


from models import *
from forms import GlogoForm


@login_required
def select_primary(request, logo_id):
    """
    Select primary photo
    """
    
    glogo = get_object_or_404(Glogo, pk=logo_id)
    try:
        content_type = get_object_or_404(ContentType, model=glogo.content_type.model)
        primary_logo = get_object_or_404(Glogo, is_primary=True, \
                                            content_type=glogo.content_type, \
                                            object_id=glogo.object_id)
        primary_logo.is_primary = False
        primary_logo.save()
    except Exception, ObjectDoesNotExist:
        pass
    glogo.is_primary = True
    glogo.save()
    next = request.GET.get('next', None)
    if next:
        return HttpResponseRedirect(next)
    else:
        return HttpResponse('Success Set to primary')


@login_required
def delete_logo(request, logo_id):
    """
    Select primary photo
    """
    
    glogo = get_object_or_404(Glogo, pk=logo_id)
    glogo.delete()
    next = request.GET.get('next', None)
    if next:
        return HttpResponseRedirect(next)
    else:
        return HttpResponse('Successsfully Delete')
