from django import forms

from to_do_list.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            "deadline": forms.DateTimeInput(attrs={
                "type": "datetime-local",
                "class": "form-control"
            },
            format='%Y-%m-%dT%H:%M'
            ),
            "content": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
            "tags": forms.CheckboxSelectMultiple(),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Наприклад: Навчання, Дім, Робота"
            }),
        }

