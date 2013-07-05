from django import forms

from rpg_game.models import Character, Character_class, Item

# class CategoryForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         queryset = None
#         if kwargs.has_key('user'):
#             queryset = Category.objects.filter(owner=kwargs.pop('user'))
#         elif kwargs.has_key('instance'):
#             category = kwargs['instance']
#             queryset = Category.objects.filter(owner=category.owner).exclude(name=category.name)
#         super(CategoryForm, self).__init__(*args, **kwargs)
#         if queryset is not None:
#             self.fields['category_parent'].queryset = queryset

#     class Meta:
#         model = Category
#         exclude = ('owner')
    
class CreateCharacterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        queryset = None
        if kwargs.has_key('user'):
            queryset = Character.objects.filter(owner=kwargs.pop('user'))
        elif kwargs.has_key('instance'):
            character = kwargs['instance']
            queryset = Category.objects.filter(owner_id=character.owner_id).exclude(name=character.name)
        super(CreateCharacterForm, self).__init__(*args, **kwargs)
        if queryset is not None:
            self.fields['Character'].queryset = queryset

    class Meta:
        model = Character
        exclude = ('owner_id')
