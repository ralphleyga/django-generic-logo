from django.template import Library, Node, TemplateSyntaxError
from django.db.models import get_model
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.utils.datastructures import SortedDict


register = Library()

class GetObjectLogoNode(Node):
    def __init__(self, content_type, object_id, varname):
        self.content_type = content_type
        self.object_id = object_id
        self.varname = varname
    
    def render(self, context):
        glogo = None
        content_type = ContentType.objects.get(model=context[self.content_type])
        Glogo = get_model('glogo', 'glogo')
        try:
            glogo = Glogo.objects.get(content_type=content_type, \
                                        object_id=context[self.object_id], \
                                        is_primary=True)
        except Exception, ObjectDoesNotExist:
            glogo = None
        
        context[self.varname] = glogo
        return ''


def get_object_logo(parser, token):
    """
    get_object_logo content_type object_id as varname
    """
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError, "get_object_logo there must be 2 arguments"
    if bits[3] != 'as':
        raise TemplateSyntaxError, "get_object_logo must have 'as'"
    return GetObjectLogoNode(bits[1], bits[2], bits[4])
get_object_logo = register.tag(get_object_logo)



class GetObjectLogosNode(Node):
    def __init__(self, content_type, object_id, varname):
        self.content_type = content_type
        self.object_id = object_id
        self.varname = varname
    
    def render(self, context):
        glogo = None
        content_type = ContentType.objects.get(model=context[self.content_type])
        Glogo = get_model('generic_logo', 'glogo')
        glogo = Glogo.objects.filter(content_type=content_type, \
                                        object_id=context[self.object_id])
        context[self.varname] = glogo
        return ''


def get_object_logos(parser, token):
    """
    get_object_logos content_type object_id as varname
    """
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError, "get_object_logos there must be 2 arguments"
    if bits[3] != 'as':
        raise TemplateSyntaxError, "get_object_logos must have 'as'"
    return GetObjectLogosNode(bits[1], bits[2], bits[4])
get_object_logos = register.tag(get_object_logos)
