from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Post


# Define a view to list blog posts
class PostList(generic.ListView):
    model = Post  # Specify the model to be used for the list view
    queryset = Post.objects.filter(status=1).order_by("-created_on")  # Retrieve published posts
    template_name = "index.html"  # Set the HTML template for the list view
    paginate_by = 6  # Limit the number of posts per page for pagination


# Define a view to display a single blog post along with its comments
class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        # Retrieve all published posts
        queryset = Post.objects.filter(status=1)

        # Get the specific post based on the provided slug; return 404 if not found or not published.
        post = get_object_or_404(queryset, slug=slug)

        # Retrieve all approved comments for the post, sorted from newest to oldest.
        comments = post.comments.filter(approved=True).order_by("-created_on")

        # Check if the current logged-in user has liked this post.
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Render the post detail template, passing the post, its comments, and a new comment form.
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
        
    