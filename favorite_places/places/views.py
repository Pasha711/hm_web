from django.shortcuts import render

# Create your views here.
# places/views.py

import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import PlaceForm

def get_session_key(request):
    """Отримує або створює ключ сесії."""
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def home(request):
    """Головна сторінка з кнопкою для обрання випадкового місця."""
    random_place = None
    if request.method == 'POST':
        session_key = get_session_key(request)
        user_places = Place.objects.filter(session_key=session_key)

        if user_places.exists():
            # Створюємо зважений список, де кожне місце повторюється 'rating' разів
            weighted_list = []
            for place in user_places:
                weighted_list.extend([place] * place.rating)

            if weighted_list:
                random_place = random.choice(weighted_list)

    return render(request, 'places/home.html', {'random_place': random_place})

def place_list(request):
    """Сторінка зі списком усіх місць поточного користувача."""
    session_key = get_session_key(request)
    places = Place.objects.filter(session_key=session_key)
    return render(request, 'places/place_list.html', {'places': places})

def place_detail(request, pk):
    """Сторінка з деталізованою информацією про конкретне місце."""
    session_key = get_session_key(request)
    # get_object_or_404 гарантує, що користувач бачить лише свої місця
    place = get_object_or_404(Place, pk=pk, session_key=session_key)
    return render(request, 'places/place_detail.html', {'place': place})

def add_place(request):
    """Сторінка з формою для додавання нового месця."""
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            # Не зберігаємо у базу одразу, щоб додати ключ сесії
            new_place = form.save(commit=False)
            new_place.session_key = get_session_key(request)
            new_place.save()
            return redirect('place_list') # Редирект на список місць
    else:
        form = PlaceForm()

    return render(request, 'places/add_place.html', {'form': form})
