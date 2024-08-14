from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ImageUploadForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Image uploaded successfully')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})


@csrf_exempt
def save_image(request):
    if request.method == 'POST':
        image_data = request.POST.get('image')
        # Process and save image_data
        return HttpResponse('Image saved successfully')
    return HttpResponse('Invalid request')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('upload_image')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def newupload(request):
    return render(request,'newupload.html')