

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .models import Tasks
from django.contrib.messages.views import SuccessMessageMixin

def index(request):
    context = {

    }
    return render(request, 'index.html', context)

def sign_up(request):
    if str(request.method) == 'POST':
        if str(request.POST['password']) == str(request.POST['password_confirm']):
            if User.objects.filter(username=request.POST['username']).exists():
                messages.error(request, 'O nome de usuário já existe.')
            elif User.objects.filter(email=request.POST['email']).exists():
                messages.error(request, 'Já há uma conta registrada com esse e-mail.')
            else:
                new_user = User.objects.create_user(
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    username=request.POST['username'],
                    email=request.POST['email'],
                    password=request.POST['password']
                )
                new_user.save()
                messages.success(request, f'Cadastrado com sucesso, obrigado!. Seja bem-vindo, {new_user.get_full_name()}!')
                return redirect('index')
        else:
            messages.error(request, 'Senha inicial e de confirmação, não são idênticas!')

    return render(request, 'sign-up-template.html')

def sign_in(request):
    if str(request.method) == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login efetuado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'O usuário ou a senha não existem!')
    return render(request, 'sign-in-template.html')

# from django.contrib.auth import logout
"https://www.youtube.com/watch?v=tUqUdu0Sjyc"  # 29:33
def sign_out(request):
    messages.success(request, 'Saída efetuada com sucesso')
    logout(request)
    return redirect('index')

class TasksListView(ListView):
    context_object_name = 'queryset'  # .objects.all() [ para loop for ]
    model = Tasks
    ordering = 'created'              # por qual campo começar a mostrar dados
    paginate_by = 5                   # ativar lógica de paginação (se há), a partir do valor
    template_name = 'my-tasks.html'

    def get_context_data(self, **kwargs):
        context = super(TasksListView, self).get_context_data(**kwargs)
        context['database'] = Tasks.objects.all()
        return context

"1. CreateView, UpdateView e DeleteView conectam-se"
"2. Sendo assim, quando for criado o formulário no template do CreateView, a tag não deve ter o atributo [ action ]"
"3. Caso contrário, a rota passada sempre vai obedecer as ações da view vinda dela"
"4. Ou seja, se a rota for da view CreateView, o formulário cria, mas não edita, nem deleta"
"5. Por isso, deixa-se o atributo [ action ] fora da tag [ <form></form> ]"

class NewTaskCreateView(SuccessMessageMixin, CreateView):
    fields = ('task',)
    model = Tasks
    success_message = 'Uma nova tarefa foi adicionada!'
    success_url = reverse_lazy('mytasks')
    template_name = 'create-task.html'

class AlterTaskUpdateView(SuccessMessageMixin, UpdateView):
    fields = ('task',)
    model = Tasks
    success_message = 'Sua tarefa foi editada!'
    success_url = reverse_lazy('mytasks')
    template_name = 'create-task.html'

class EraseTaskDeleteView(SuccessMessageMixin, DeleteView):
    model = Tasks
    success_message = 'Sua tarefa foi editada!'
    success_url = reverse_lazy('mytasks')
    template_name = 'delete-task.html'

def handler404(request, exception):
    return render(request, '404.html')

def handler500(request):
    return render(request, '500.html')
