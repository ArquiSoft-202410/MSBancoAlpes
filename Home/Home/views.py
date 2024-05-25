from django.shortcuts import redirect, render

def home(request):
    return render(request, 'home.html')

def userForm(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            # Redirect to API Gateway
            return redirect('home')
    return render(request, 'userForm.html')