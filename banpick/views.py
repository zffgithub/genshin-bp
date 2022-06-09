from django.shortcuts import render, redirect
from django.urls import reverse
from draft.forms import DraftCreateForm
import string

def home(request):
    if request.method == 'POST':
        mode = request.POST.get("mode")
        forms = DraftCreateForm(request.POST)
        if mode == '1':
            blue_player = ''.join(['//' for i in range(7)])
            red_player = ''.join(['//' for i in range(7)])
        else:
            blue_player = ''.join(['//' for i in range(3)])
            red_player = ''.join(['//' for i in range(3)])
        if forms.is_valid():
            new_draft = forms.save(commit=False)
            new_draft.red_player_name = red_player
            new_draft.blue_player_name = blue_player
            new_draft.mode = mode
            new_draft.save()
            request.session['master'] = new_draft.id
            return redirect('draft:draft_result')
    else:
        forms = DraftCreateForm()
        return render(request, 'home.html', {
            'forms': forms
        })