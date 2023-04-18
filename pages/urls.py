from django.urls import path
from .views import IndexView, ProjectsView, ProjectView, PortfoliosView, PortfolioView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("projects", ProjectsView.as_view(), name="projects"),
    path("projects/<int:pk>", ProjectView.as_view(), name="project"),
    path("portfolios", PortfoliosView.as_view(), name="portfolios"),
    path("portfolios/<int:pk>", PortfolioView.as_view(), name="portfolio"),
]