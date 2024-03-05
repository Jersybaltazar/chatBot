from django.shortcuts import render
from django.http import JsonResponse
#from chatbot import predict_class, get_response 
def index(request):
    return render(request,'index.html')

#def chatbot_response(request):
#    # Lógica para manejar las solicitudes del chatbot y devolver una respuesta JSON
#    if request.method == 'POST':
#        message = request.POST.get('message', '')  # Obtener el mensaje del usuario desde la solicitud
#        intent = predict_class(message)  # Utiliza tu función predict_class para obtener la intención del usuario
#        response = get_response(intent)  # Utiliza tu función get_response para obtener la respuesta del chatbot
#        return JsonResponse({'response': response})
#    else:
#        return JsonResponse({'response': 'Error: Método de solicitud no permitido'})