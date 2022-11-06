from django.shortcuts import render, redirect
from django.urls import reverse_lazy
import requests

from health_app.forms import PostForm, UserForm
from health_app.models import Post

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin

# LogMeal API Data
logmeal_app_user_token = "8943b1b2dc5111cbe4da658779365d77e42a5251"
logmeal_headers = {'Authorization': 'Bearer ' + logmeal_app_user_token}
logmeal_endpoint = 'https://api.logmeal.es/v2/recognition/dish'

nutritionix_app_id = "72c83243"
nutritionix_app_key = "053ddd9f760f7e462383e58cd86f17a4"
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"
nutritionix_headers = {
    "x-app-id": nutritionix_app_id,
    "x-app-key": nutritionix_app_key,
}

# Create your views here.
def index(request):
    return render(request, "splash_page.html")

def register_request(request):
    form = UserForm(request.POST)
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("post_list")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    return render(request, template_name="user_form.html", context={"register_form":form})

def login_request(request):
    form = AuthenticationForm(request, data=request.POST)
    if request.method == "POST":
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print(f"You are now logged in as {username}.")
                return redirect("post_list")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
        form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

class CreatePostView(SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('post_list')
    success_message = "Post Successfully Created!"
    def form_valid(self, form):
        form.instance.author = self.request.user
        img = form.instance.post_pic
        response_logmeal = requests.post(logmeal_endpoint, files={'image': img},
                                headers=logmeal_headers)
        query = response_logmeal.json()
        food_name = query['recognition_results'][0]['name'].title()
        nutritionix_params = {"query": food_name}
        response_nutritionix = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=nutritionix_headers)
        response_nutritionix_data = response_nutritionix.json()['foods'][0]
        calorie_count = response_nutritionix_data['nf_calories']
        form.instance.calorie_count = calorie_count
        form.instance.food_name = food_name
        return super().form_valid(form)

def post_list_view(request):
       posts = Post.objects.all()

       context = {
              'posts': posts,
       }
       return render(request, 'post_list.html', context)

@login_required # Adding a decorator that makes login required for logging out. Has to be immediately above the view.
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("index")
