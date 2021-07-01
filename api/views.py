from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(["GET"])
def welcome(request):
    content = {"message": "Minha primeira view em Django!"}
    return JsonResponse(content)


@api_view(["GET"])
def users(request):
    users = [
        {'nameDisciplina': 'Programação Web I','nameAluno': 'Jefferson Henrique', 'nota1': 10, 'nota2': 9, 'media': ( 10 + 9) / 2, 'situacao': 'Aprovado'},
        {'nameDisciplina': 'Teste de Software', 'nameAluno': 'Jefferson Henrique', 'nota1': 3, 'nota2': 6, 'media': ( 3 + 6) / 2, 'situacao': 'Reprovado'},
        {'nameDisciplina': 'Programação Web II', 'nameAluno': 'Jefferson Henrique', 'nota1': 9, 'nota2': 9, 'media': ( 9 + 9) / 2, 'situacao': 'Aprovado'},
        {'nameDisciplina': 'Programação Web III', 'nameAluno': 'Jefferson Henrique', 'nota1': 5, 'nota2': 6, 'media': ( 5 + 6) / 2, 'situacao': 'Reprovado'},
        {'nameDisciplina': 'Lógica de Programação', 'nameAluno': 'Jefferson Henrique', 'nota1': 10, 'nota2': 8, 'media': ( 10 + 8 ) / 2, 'situacao': 'Aprovado'},
        {'nameDisciplina': 'Programação Java', 'nameAluno': 'Jefferson Henrique', 'nota1': 7, 'nota2': 7, 'media': ( 7 + 7 ) / 2, 'situacao': 'Aprovado'}
    ]

    return JsonResponse(users, safe=False)
