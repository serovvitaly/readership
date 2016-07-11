from django.core.management.base import BaseCommand, CommandError
from content import models
import content.providers.nkj as provider

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        def prepare_model(content_object):
            model, is_created = models.Article.objects.get_or_create(
                source_url=content_object.source_url,
                defaults = {
                    'title': content_object.title,
                    'content': content_object.content,
                    'description': content_object.description,
                    'published_at': content_object.published_at,
                    'source_id': 1,
                }
            )
            if len(content_object.images) > 0:
                for image in content_object.images:
                    models.Image.objects.get_or_create(
                        href=image['href'],
                        defaults={
                            'title': image['title'],
                            'width': image['width'],
                            'height': image['height'],
                            'article_id': model.id,
                        }
                    )

        page = 1
        while page <= 1:
            print('Page ' + str(page) + ' ...')
            provider.get_articles_form_page(page, prepare_model)
            page += 1
