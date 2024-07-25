
from django.shortcuts import render

def index(request):
    cards = [
        {
            'title' : 'SEDANS',
            'bg_color' : 'bg_color',
            'para' : 'Choose a sedan for its affordability and excellent fuel economy. Ideal for cruising in the city or on your next road trip.',
            'image' : 'images/icon-sedans.svg',
            'text_color' : 'color:hsl(31, 77%, 52%)',
            'hovertext' : 'learn'
        },
        {
            'title': 'SUVS',
            'bg_color' : 'bg_color1',
            'para' : 'Take an SUV for its spacious interior, power, and versatility. Perfect for your next family vacation and off-road adventures.',
            'image' : 'images/icon-suvs.svg',
            'text_color' : 'color:hsl(184, 100%, 22%)',
            'hovertext' : 'learn1'
        },
        {
            'title': 'LUXURY',
            'bg_color' : 'bg_color2',
            'para' : 'Cruise in the best car brands without the bloated prices. Enjoy the enhanced comfort of a luxury rental and arrive in style.',
            'image' : 'images/icon-luxury.svg',
            'text_color' : 'color:hsl(179, 100%, 13%)',
            'hovertext' : 'learn2'
        }
    ]
    return render(request, 'index.html', {'cards':cards})
