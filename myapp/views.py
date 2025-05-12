from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from .forms import PostForm, TagForm

# Post yaratish
def post_list(request):
    posts = Post.objects.all()  # Barcha postlarni olish
    return render(request, 'post_list.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Listga qaytish
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

# Postni ko'rsatish
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    tags = post.tag_set.all()  # Postga tegishli barcha taglarni olish
    return render(request, 'post_detail.html', {'post': post, 'tags': tags})
