from django.dispatch import Signal
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader, RequestContext
from django.template import Context
from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.models import ContentType


from glogo.forms import GlogoForm
from glogo.models import Glogo


def groups(request):
    """
    groups
    """
    groups = Group.objects.all()
    template_name = "groups.html"
    return render_to_response(template_name, dict({
                "groups": groups,
            }), context_instance=RequestContext(request))


def group(request, group_id, form_class=GlogoForm):
    """
    group detail
    """

    group = get_object_or_404(Group, pk=group_id)
    template_name = "group_detail.html"
    if request.method == "POST":
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            content_type = ContentType.objects.get(model='group')
            try:
                glogo = Glogo.objects.get(content_type=content_type, \
                                    object_id=group_id, \
                                    is_primary=True)
                glogo.is_primary = False
                glogo.save()
            except Exception, ObjectDoesNotExist:
                pass
            Glogo.objects.create(user=request.user, \
                                image=request.FILES['image'],
                                content_type=content_type,
                                object_id=group_id,
                                is_primary=True)
    else:
        form = form_class()
        
    return render_to_response(template_name, dict({
                "group": group,
                "form": form,
            }), context_instance=RequestContext(request))
