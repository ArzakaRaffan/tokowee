from django.shortcuts import render
def show_main(request):
    context = {
        'itemName': 'Chet Baker Vinyl - Sings Again 1985 (Reissued)',
        'itemPrice' : 'Rp599.000,00',
        'itemDescription' : 'Artist: Chet Baker\n    Album: Sings Again\n    Country: Europe\n    Genre: Jazz\n    Style: Bop, Cool Jazz',
        'itemStock' : 2
        }

    return render(request, "main.html", context)