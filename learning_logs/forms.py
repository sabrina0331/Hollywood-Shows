from django import forms 
from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic 
        # 建立一个只包含text字段的表单
        fields = ['text']
        # 让django不要为字段text生成标签
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'colors':80})}