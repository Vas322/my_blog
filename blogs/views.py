from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import PostForm, EntryForm
from .models import Post, Entry
from django.shortcuts import render


# Create your views here.
def index(request):
    """Домашняя страница приложения Blogs"""
    posts = Post.objects.order_by('date_added')[:2]  # Параметр сортировки.
    # В данном случае по дате сортирует
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)


@login_required
def posts(request):
    """Выводит список тем."""
    posts = Post.objects.filter(owner=request.user).order_by('date_added')  # Параметр сортировки.
    # В данном случае по дате сортирует
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)


@login_required
def post(request, post_id):
    """Выводит один пост и все его записи."""
    post = Post.objects.get(id=post_id)
    # Проверка того, что тема принадлежит текущему пользователю.
    if post.owner != request.user:
        raise Http404
    entries = post.entry_set.order_by('-date_added')
    context = {'post': post, 'entries': entries}
    return render(request, 'blogs/post.html', context)


@login_required
def new_post(request):
    """Определяет новую тему."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = PostForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:posts'))
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required
def new_entry(request, post_id):
    """Добавляет новую запись по конкретной теме."""
    post = Post.objects.get(id=post_id)
    if post.owner != request.user:
        raise Http404("Ты кто такой? Нечего лезть в чужую тему!)")
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = EntryForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.post = post
            new_entry.owner = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('blogs:post', args=[post_id]))
    context = {'post': post, 'form': form}
    return render(request, 'blogs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Редактирует существующую запись."""
    entry = Entry.objects.get(id=entry_id)
    post = entry.post
    if post.owner != request.user:
        raise Http404("Ты кто такой? Нечего лезть в чужую тему!)")
    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущей записи.
        form = EntryForm(instance=entry)
    else:
        # Отправка данных POST; обработать данные.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:post', args=[post.id]))
    context = {'entry': entry, 'post': post, 'form': form}
    return render(request, 'blogs/edit_entry.html', context)

