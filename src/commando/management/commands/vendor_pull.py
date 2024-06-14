import helpers

from typing import Any
from django.core.management.base import BaseCommand
from django.conf import settings

VENDOR_STATICFILES = {
    'flowbite.min.css':'https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css',
    'flowbite.min.js':'https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js',
    'flowbite.min.js.map':'https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js.map',    
}

STATICFILES_VENDOR_DIR = getattr(settings, 'STATICFILES_VENDOR_DIR')


class Command(BaseCommand):
    def handle(self, *args:Any, **options:Any) -> str | None:
        self.stdout.write('Downloading vendor static files')
        completed_urls = []

        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            dl_success = helpers.download_to_local(url, out_path)

            if dl_success:
                completed_urls.append(url)
            else:
                self.stdout.write(self.style.ERROR(f'failed to download {url}'))

        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(self.style.SUCCESS('successfully updated all vendor files.'))
        else:
            self.stdout.write(self.style.WARNING('some files were not updated.'))