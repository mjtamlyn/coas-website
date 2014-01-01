from django.template import Library, Context
from django.template.loader import get_template
import markdown


register = Library()


@register.simple_tag
def mdcontent(filename):
    content_template = get_template(filename)
    content = content_template.render(Context())
    return markdown.markdown(content)
