from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Draft
import uuid

class DraftCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(DraftCreateForm, self).__init__(*args, **kwargs)
    
    match_name = forms.CharField(
        label="匹配名称",
        widget=forms.TextInput(attrs={
            'class': 'bg_black bold draft_input',
            'autofocus': 'true',
            'onkeyup': 'submitable()',
            "autocomplete": "off"
        })
    )

    blue_team_name = forms.CharField(
        label="蓝队名称",
        help_text="", # "<span class='f_right player_check'><input id='blue_player_check' class='blue' type='checkbox' onchange='playerCheck(event);'><label for='blue_player_check'>进入播放器</label></span>",
        widget=forms.TextInput(attrs={
            'class': 'bg_blue bold draft_input',
            'onkeyup': 'submitable()',
            "autocomplete": "off"
        })
    )

    red_team_name = forms.CharField(
        label="红队名称",
        help_text="", # "<span class='f_right player_check'><input id='red_player_check' class='red' type='checkbox' onchange='playerCheck(event);'><label for='red_player_check'>进入播放器</label></span>",
        widget=forms.TextInput(attrs={
            'class': 'bg_red bold draft_input',
            'onkeyup': 'submitable()',
            "autocomplete": "off"
        })
    )

    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={
            'class': 'bg_black bold draft_input',
            'onkeyup': 'submitable()',
            "autocomplete": "new-password"
        })
    )

    class Meta:
        model = Draft
        fields = ('match_name', 'blue_team_name', 'red_team_name', 'password')

    def save(self, commit=True):
        draft = super().save(commit=False)
        draft.code = str(uuid.uuid4())
        draft.set_password(self.cleaned_data["password"])
        if commit:
            draft.save()
        return draft


class DraftChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label="密码"
    )
    
    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]