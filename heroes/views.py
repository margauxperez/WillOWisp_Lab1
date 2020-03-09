# heroes/views.py

from django.shortcuts import render
from django.views.generic import TemplateView

class HomepageView(TemplateView):
	template_name = "homepage.html"

class CloudView(TemplateView):
	template_name = "detail_cloud.html"

class SunfloweyView(TemplateView):
	template_name = "detail_sunflowey.html"

class JesterView(TemplateView):
	template_name = "detail_jester.html"
