#-*- coding: utf-8 -*-

from django.db.models import fields

from bootstrap3_wysihtml5x.conf import settings
from bootstrap3_wysihtml5x.utils import keeptags
from bootstrap3_wysihtml5x.widgets import Wysihtml5xTextareaWidget


class Wysihtml5xTextField(fields.TextField):
    def __init__(self, *args, **kwargs):
        self.keep_tags = kwargs.pop('keep_tags', 
                                    settings.WYSIHTML5_ALLOWED_TAGS)
        super(Wysihtml5xTextField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {"widget": Wysihtml5TextareaWidget}
        defaults.update(kwargs)
        return super(Wysihtml5xTextField, self).formfield(**defaults)

    def pre_save(self, model_instance, add):
        value = super(Wysihtml5xTextField, self).pre_save(model_instance, add)
        return keeptags(value, self.keep_tags)


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^wysihtml5\.fields\.Wysihtml5xTextField"])
except ImportError:
    pass
