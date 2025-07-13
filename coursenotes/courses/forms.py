from django import forms
from .models import Course
from .models import Note
from ckeditor.widgets import CKEditorWidget
from .models import Tag


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']

# class NoteForm(forms.ModelForm):
#     class Meta:
#         model = Note
#         fields = ['title', 'content']


# class NoteForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorWidget())

#     class Meta:
#         model = Note
#         fields = ['title', 'content']

class NoteForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple  # 或 forms.SelectMultiple
    )

    class Meta:
        model = Note
        fields = ['title', 'content', 'tags']