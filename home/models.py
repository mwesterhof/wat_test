from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page


class HomePage(Page):
    content = StreamField([
        ('text', blocks.TextBlock()),
        ('page', blocks.PageChooserBlock()),
    ], blank=True, null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('content')
    ]
