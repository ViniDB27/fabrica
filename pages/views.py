from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class ProjectsView(TemplateView):
    template_name = "projects.html"

class ProjectView(TemplateView):
    template_name = "project.html"

class PortfoliosView(TemplateView):
    template_name = "portfolios.html"

class PortfolioView(TemplateView):
    template_name = "portfolio.html"
