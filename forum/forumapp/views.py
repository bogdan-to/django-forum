from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Topic
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
import itertools

def index(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'index.html', context)

def category(request,slug):

    category = get_object_or_404(Category, category_slug=slug)
    topics = Topic.objects.filter(topic_category = category).order_by('-topic_date')

    paginated_topics = Paginator(topics, 10)
    page = request.GET.get('page', 1)
    topics_on_page = paginated_topics.get_page(page)
    page_range = paginated_topics.get_elided_page_range(number=page, on_each_side=1, on_ends=1)

    context = {
        'category':category,
        'topics_on_page': topics_on_page,
        'page_range': page_range
    }

    return render(request, 'category.html', context)

@login_required(login_url='login')
def new_topic(request, category_id):
    category = Category.objects.get(id=category_id)

    if request.method == 'POST' and request.user.is_authenticated:
        new_topic_title = request.POST['new_topic_title']

        if new_topic_title.strip():

            new_topic_slug = slugify(new_topic_title)
            for i in itertools.count(1):
                if not Topic.objects.filter(topic_slug=new_topic_slug).exists():
                    break
                new_topic_slug = new_topic_slug + '-' + str(i)
                if len(new_topic_slug) > 20:
                    new_topic_slug = new_topic_slug[:20]

            new_topic = Topic(
                topic_category = category,
                topic_title = new_topic_title,
                topic_opened_by = request.user,
                topic_slug = new_topic_slug
            )
            new_topic.save()
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Tema ne sme biti prazna.', extra_tags='alert-warning')
    return redirect(request.META.get('HTTP_REFERER'))



def error_404_view(request, exception):
    return render(request, '404.html')