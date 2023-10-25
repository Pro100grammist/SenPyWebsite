import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_portfolio_website.settings")
django.setup()

from portfolio.models import *
from portfolio.content import content

models_and_data = {
    HardSkill: content['hard_skills'],
    NecessaryUseful: content['necessary_useful'],
    IDE: content['ide'],
    WebFrameworks: content['web_frameworks'],
    Data: content['data'],
    Certificates: content['certificates'],
}


for model, data_list in models_and_data.items():
    for data in data_list:
        model.objects.create(**data)

# for project_data in content['projects']:
#     Projects.objects.create(
#         title=project_data['title'],
#         description=project_data['description'],
#         image=project_data['image'],
#         url=project_data['url']
#     )
#
# for skill_data in content['hard_skills']:
#     HardSkill.objects.create(
#         title=skill_data['title'],
#         url_name=skill_data['url_name'],
#         link=skill_data['link']
#     )
#
# for useful_data in content['necessary_useful']:
#     NecessaryUseful.objects.create(
#         title=useful_data['title'],
#         url_name=useful_data['url_name']
#     )
#
# for ide_data in content['ide']:
#     IDE.objects.create(
#         name=ide_data['name'],
#         image=ide_data['image'],
#         url=ide_data['url'],
#         rating=ide_data['rating'],
#         description=ide_data['description']
#     )
#
# for framework_data in content['web_frameworks']:
#     WebFrameworks.objects.create(
#         name=framework_data['name'],
#         image=framework_data['image'],
#         url=framework_data['url'],
#         rating=framework_data['rating'],
#         description=framework_data['description']
#     )
#
# for data_data in content['data']:
#     Data.objects.create(
#         name=data_data['name'],
#         image=data_data['image'],
#         url=data_data['url'],
#         rating=data_data['rating'],
#         description=data_data['description']
#     )
#
# for certificate_data in content['certificates']:
#     Certificates.objects.create(
#         url=certificate_data['url'],
#         image=certificate_data['image'],
#         alt=certificate_data['alt']
#     )
