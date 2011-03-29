# Welcome to the django-generic-logo wiki!

This apps is currently in alpha version, haven't used in site.  There will be many updates to come.  Please help us to improve this little django apps :)

Steps to Install django-generic-logo

Step 1:
Download the 'django-generic-logo' at https://github.com/ralphleyga/django-generic-logo and 'python setup.py install' in your terminal.

Step 2:
pip install django-imagekit

Step 3:
add **'generic_logo'** and 'imagekit' at you installed apps and python manage.py syncdb in your terminal.
```python
 INSTALLED_APPS = (
     ...
     'generic_logo',
     'imagekit',
 )
```
Step 4:
Add the app to project urls.py
```python
(r'^logo/', include('generic_logo.urls')),
```

How to used django-generic-logo:
1. import this code to you created app.
```python
from generic_logo.forms import GlogoForm
from generic_logo.models import Glogo
from generic_logo.views import upload_logo
```

2. to upload a logo, you can used the function 'upload_logo(request, content_object, image)' found in generic_logo/views.py.

for example you have an app to upload a logo to a group. in your groups/views.py this is the sample code:

```python
def group(request, group_id, form_class=GlogoForm):
    """
    group detail
    """

    group = get_object_or_404(Group, pk=group_id)
    template_name = "group_detail.html"
    if request.method == "POST":
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data
            upload_logo(request, 
                        group, 
                        form.cleaned_data['image'])
    else:
        form = form_class()
        
    return render_to_response(template_name, dict({
                "group": group,
                "form": form,
            }), context_instance=RequestContext(request))
```

Using the templatetags:

1. First, put the {% load generic_logo %} to your template

2. To attach the list of logos just add this code, for sample you have list of groups. You can modify the _generic_logos.html

	<h3>Logos</h3>
    {% with group as content_object %}
        {% include "generic_logo/_generic_logos.html" %}
    {% endwith %

3. To get the primary logo, just add this code:
	{% with 'group' as content_type %}{% with group.id as object_id %}
        {% get_object_logo content_type object_id as group_logo %}
        {% if group_logo %}
            <img src="{{ group_logo.thumbnail_image.url }}"><br/>
            <b>Primary</b>
        {% else %}
            <b>No primary logo</b>
        {% endif %}
    {% endwith %}{% endwith %}

4. To put the upload form, add this code:

	{% include "generic_logo/_upload_logo.html" %}

You can check the generic_logo demo folder

Note:  This an alpha version yet.  Please help me to fix some bugs and suggest some features :)
