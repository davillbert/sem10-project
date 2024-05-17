from django import forms


from .models import Task


class TaskForm(forms.ModelForm):

   class Meta:
       model = Task
       fields = ('title', 'quest', 'right', 'v1', 'v2', 'v3', 'v5', 'text', 'author')



class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions', None)
        super(QuizForm, self).__init__(*args, **kwargs)
        if questions:
            for question in questions:
                choices = [(question.v1, question.v1), (question.v2, question.v2), (question.v3, question.v3), (question.v5, question.v5)]
                self.fields[str(question.id)] = forms.ChoiceField(label=question.quest, choices=choices, widget=forms.RadioSelect)
