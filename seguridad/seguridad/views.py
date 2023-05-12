from django.contrib import messages
from django.contrib.auth.models import Group,User
from django.contrib import auth
from io import StringIO
import json
from django.shortcuts import redirect, render
import requests
from django.contrib.auth import login, logout, authenticate

def saceConeccion(username, password):
	try:
		apiSace = "https://sace.se.gob.hn/api/api-token-auth/"
		#<print(username, password)
		data = {"username":username, "password": password}
		jsonData1 = requests.post(apiSace, data=data).json()
		#print(jsonData1)
		apiSace2 = "https://sace.se.gob.hn/api/login_sere/"
		headers = {'Authorization': "token " + jsonData1["token"]}
		jsonData2 = requests.get(apiSace2, headers=headers).json()
		cod = StringIO(jsonData2)
		cod2 = json.load(cod)
		#print(cod2)
		return cod2
	except:
			return 

#-------------------------------------------------------------------------#
def signin(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
        
		sace = saceConeccion(username, password)
		user = authenticate(username=username, password=password)
		 
		if user:
			grupo = user.groups.all()
			print(grupo)
			if str(grupo[0]) == "DOCENTE":
				login(request, user)
				return redirect('/repositorio-de-recursos/2')  
				
			else: 
				login(request, user) 
				return redirect('/admin/')  

		
			
		elif sace:
			sace = saceConeccion(username, password)
			grupo = sace[0]["usuario_grupo"]
			
			usuario = User.objects.create_user(username=username, 
                                        password=password, 
                                        first_name=sace[0]["usuario_firstname"], 
                                        last_name=sace[0]["usuario_lastname"],
                                        email="asda@gmail.com",
                                        )
			usuario.save()
			usuario.groups.add(Group.objects.get(name=grupo))
			usuario.save()
			login(request, usuario)
			return redirect('/repositorio-de-recursos/2') 
		
		else:
			
			messages.add_message(request, messages.INFO, 'Usuario y/o contraseña Incorrecto')
			return redirect('/')	

	
			
#---------------------------------------------------------------------#   
def signout(request):
    auth.logout(request)
    return redirect('/')