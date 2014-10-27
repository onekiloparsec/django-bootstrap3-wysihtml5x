#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from wysihtml5.widgets import Wysihtml5TextareaWidget


class Wysihtml5BootstrapWidget(Wysihtml5TextareaWidget):

    class Media:
        # read https://docs.djangoproject.com/en/1.5/topics/forms/media/
        extend = False
        css = {'all': ('css/bootstrap.min.css',
                       'css/bootstrap-django-bootstrap3-wysihtml5x.css')}
        js = ('django-bootstrap3-wysihtml5x/js/advanced.js',
              'django-bootstrap3-wysihtml5x/js/django-bootstrap3-wysihtml5x-0.3.0.min.js',
              'js/bootstrap.min.js',
              'js/bootstrap-django-bootstrap3-wysihtml5x.js',)

    def __init__(self, attrs=None, **kwargs):
        if not attrs:
            attrs = {"style": 'width: 600px; margin:0 auto'}
        elif not attrs.get('style', False):
            attrs.update({'style': 'width: 640px; margin:0 auto'})
        super(Wysihtml5BootstrapWidget, self).__init__(attrs=attrs, **kwargs)

    def render_toolbar_widget(self, id):
        return ''

    def render_js_delay_widget(self, id, position):
        return ''

    def render_js_init_widget(self, id):
        options = {"id": id}
        options.update(self.editor_settings)
        if options.get('toolbar', 'null') == 'null':
            options['toolbar'] = '"%s-toolbar"' % id
        widget = '''
<script>
  $("#%(id)s").django-bootstrap3-wysihtml5x({
    "font-styles": true,
    "emphasis": true,
    "lists": true,
    "html": true,
    "link": true,
    "image": true,
    "stylesheets": false
  });
</script>''' % options
        return widget
