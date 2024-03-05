from django.shortcuts import render

def portfolio(request):
    # Lógica para obtener y mostrar los proyectos del portfolio
    return render(request, 'portfolio/portfolio.html', context)