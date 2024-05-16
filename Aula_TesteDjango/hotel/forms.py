from django import forms


class FormNome (forms.Form):
    nome = forms.CharField(label="Seu nome", max_length=100)
    email = forms.EmailField(label="Seu email", max_length=100)
    mensagem = forms.CharField(label="Sua mensagem", widget=forms.Textarea)
