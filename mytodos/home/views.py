from django.shortcuts import redirect, render
from .models import myTodos
from .forms import todoForm

# Create your views here.
def index(request):
    return render(request,'index.html',{'todos':myTodos.objects.all(),'form':todoForm})

def todo(request):
    return render(request,'todos.html',{'todos':myTodos.objects.all()})

def submit(request):
    if request.method == 'POST':
        form = todoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('todo')
        
    else:
        pass

def delete(request,id):
    task = myTodos.objects.get(pk=id)
    task.delete()
    return redirect('index')

def edit(request,id):
   mytodos = myTodos.objects.get(pk=id)
   todoForm(request.POST,instance=mytodos)
   if todoForm.is_valid():
       todoForm.save()