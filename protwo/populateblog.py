import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","protwo.settings")

import django
django.setup()

from blog.models import BlogPost,Author
from faker import Faker

fakegen = Faker()

def populate(n=10):

     for i in range(n):

         fake_name = fakegen.name()
         fake_content = fakegen.paragraph(nb_sentences=10)
         fake_date = fakegen.date()
         fake_title = " ".join(fake_content.split(" ")[:3])

         author = Author.objects.get_or_create(name=fake_name)[0]
         post = BlogPost.objects.get_or_create(content=fake_content,author=author,date=fake_date,title=fake_title)[0]

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
