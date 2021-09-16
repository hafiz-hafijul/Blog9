from django.core.checks import messages
from django.db.models.query import Q
from django.shortcuts import get_object_or_404, render
from .models import About, Post, Category, ContactModel, CommentModel,ContactDetail
from .forms import CategoryForm, ContactForm,CommentForm
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.core.checks import messages


def categories(request):
    return {
        'categories': Category.objects.all(),
        'category': Category.objects.all()[:4],
    }


class PostListView(ListView):
    paginate_by = 10
    model = Post
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view"] = self.request.user
        context['first'] = Post.objects.all()[:1]
        context['second'] = Post.objects.all()[1:4]
        return context


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    post = Post.objects.filter(category=category)
    paginator = Paginator(post, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/category.html', {'post': page_obj})

@login_required
def categoryview(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            Keyword = form.cleaned_data['keyword']
            title = form.cleaned_data['title']
            data = Category(keyword=Keyword, title=title)
            data.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = CategoryForm()

    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)



def likepost(request, id):
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
    return HttpResponseRedirect(reverse('likes'))


def about(request):
    about = About.objects.all().last()
    context = {
        'about':about,
    }
    return render(request, 'about.html', context)

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactModel()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.save()
            return HttpResponseRedirect(reverse('contact'))
    else:
        form = ContactForm()
    
    con = ContactDetail.objects.get(id=1)

    context = {
        'form': form,
        'con':con,
    }
    return render(request, 'contact.html', context)


def post_details(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            phone = form.cleaned_data['phone']
            text = form.cleaned_data['text']
            sub=CommentModel(name=name, email=email, subject=subject, phone=phone,text=text)
            obj = sub
            obj.user = request.user
            obj.post = post
            obj.save()
            return HttpResponseRedirect(reverse('single',kwargs={'slug':slug}))
    else:
        form = CommentForm()
    comment = CommentModel.objects.filter(post=post.id, parent=None)
    replies = CommentModel.objects.filter(post=post.id).exclude(parent=None)
    relate=Post.objects.filter(category=post.category)[:4]


    context = {
        'post': post,
        'form': form,
        'comment':comment,
        'replies':replies,
        'relate':relate
    }
    return render(request, "main/blog-single.html", context)



def search(request):
    query = request.GET['search']

    if len(query) > 70:
        allpost = Post.objects.none()
    else:
        allpost = Post.objects.filter(
    Q(title__icontains=query) | Q(content__icontains=query)
)

    return render(request, "main/search.html",{'post':allpost,'query':query})
