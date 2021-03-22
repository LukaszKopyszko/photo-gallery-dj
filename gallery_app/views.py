from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user, login, logout

from django.contrib.auth.views import LoginView, LogoutView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Photo, Category

class CustomLoginView(LoginView):
    template_name = 'gallery_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True  
    context_object_name = 'login'

    def get_success_url(self):
        return reverse_lazy('gallery')

class RegisterPage(FormView):
    template_name = 'gallery_app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
              return redirect('gallery')
        return super(RegisterPage, self).get(*args, **kwargs) 


@login_required(login_url="/login/")
def GalleryView(request):
    category = request.GET.get('category')
    if category == None:
        photo = Photo.objects.all().filter(user=request.user)
    else:
        photo = Photo.objects.filter(user = request.user).filter(category__name = category)    



    categories = Category.objects.all()
    context = {'categories' : categories, 'photos': photo}
    return render(request, 'gallery_app/gallery.html', context)

@login_required(login_url="/login/")
def PhotoView(request, pk):
    categories = Category.objects.all()
    photo = Photo.objects.get(id=pk)
    context = {'categories' : categories, 'photo':photo}
    return render(request, 'gallery_app/view_photo.html', context)

@login_required(login_url="/login/")
def AddPhoto(request):
    current_user = request.user
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None


        photo = Photo.objects.create(title = data['title'], description = data['description'], category = category, image=image, user = current_user)

        return redirect('gallery')            

    context = {'categories' : categories}
    return render(request, 'gallery_app/add_photo.html', context)    


