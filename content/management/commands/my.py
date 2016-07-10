from django.core.management.base import BaseCommand, CommandError
from content.models import Article
import content.providers.nkj as provider

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        def prepare_model(content_object):
            model = Article()
            model.title = content_object.title
            model.content = content_object.content
            model.source_url = content_object.source_url
            model.description = content_object.description
            model.published_at = content_object.published_at
            model.save()

        posts = provider.get_articles_form_page(2, prepare_model)