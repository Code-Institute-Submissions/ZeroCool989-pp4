from django.shortcuts import render
from django.views import generic
from .models import Post


# Define a view to list blog posts
class PostList(generic.ListView):
    model = Post  # Specify the model to be used for the list view
    queryset = Post.objects.filter(status=1).order_by("-created_on")  # Retrieve published posts
    template_name = "index.html"  # Set the HTML template for the list view
    paginate_by = 6  # Limit the number of posts per page for pagination