from django.shortcuts import render

def home_view(request):
    # Datos simulados definidos en el backend
    datos_simulados = [
        {"fecha": "2023-10-25", "cliente": "Coca-Cola", "metrica": "Ventas Totales", "valor": 5000},
        {"fecha": "2023-10-26", "cliente": "Pepsi", "metrica": "Retención", "valor": 0.85},
        {"fecha": "2023-10-27", "cliente": "Bimbo", "metrica": "Nuevos Usuarios", "valor": 120},
        {"fecha": "2023-10-28", "cliente": "Netflix", "metrica": "Churn Rate", "valor": 0.05},
    ]
    
    context = {
        'titulo': "Portal Analítico",
        'registros': datos_simulados
    }
    
    return render(request, 'dashboard/index.html', context)