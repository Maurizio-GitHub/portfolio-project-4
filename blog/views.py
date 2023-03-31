from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


# Class-based view to render the home page
class PostList(generic.ListView):

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 9


# Class-based view to render in-full each specific post
class PostDetail(View):

    # Definition of our get-method
    def get(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("created_on")
        liked = False

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post-detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked
            },
        )
