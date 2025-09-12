from django.shortcuts import render,redirect  # type: ignore
from.models import Member
from.models import Post
from.forms import MemberForm
from django.contrib import messages # type: ignore

# Create your views here.

def home(request):
  all_post=Post.objects.all
  all_Member=Member.objects.all
  context = {"all1": all_Member ,
                "all2":all_post}
  return render(request,"home.html",context)

def base(request):
  return render(request,'base.html')

def about(request):
  return render(request,'about.html')

def blogpost(request):
  post = Post.objects.filter(slug=slug).first() # type: ignore
  context = {'post':post}
  return render(request,'blogpost.html',context)

def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Form Submitted Successfully")
            return redirect('home')
    else:
        form = MemberForm()   

    return render(request, 'join.html', {'form': form})
