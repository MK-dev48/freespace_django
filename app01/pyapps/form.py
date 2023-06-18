from django import forms

class InputForm(forms.Form):

    text = forms.CharField(label="もじ")
    number = forms.IntegerField(label="かず")
    check = forms.BooleanField(label="チェック")

    #    return text
    def hogehoge():
        hoge = text
        return text