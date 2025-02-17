import json
from django.core.management.base import BaseCommand
from quotes.models import Quote

class Command(BaseCommand):
    help = "Import quotes from a JSON file"

    def handle(self, *args, **kwargs):
        file_path = "quotes.json"
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                quotes = json.load(file)
                for quote in quotes:
                    text = quote.get("text", "").strip()
                    author = quote.get("author", "Unknown").strip()
                    
                    if text:
                        obj, created = Quote.objects.get_or_create(text=text, author=author)
                        if created:
                            self.stdout.write(self.style.SUCCESS(f'Added: "{text}" - {author}'))
                        else:
                            self.stdout.write(self.style.WARNING(f'Skipped duplicate: "{text}"'))

            self.stdout.write(self.style.SUCCESS("Successfully imported quotes"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))  