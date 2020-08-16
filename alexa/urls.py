from .alexa_skills import skill
from django_ask_sdk.skill_adapter import SkillAdapter
from django.urls import path

my_skill_view = SkillAdapter.as_view(
    skill=skill)

urlpatterns = [
    path('', my_skill_view, name='alexa-skill'),
]