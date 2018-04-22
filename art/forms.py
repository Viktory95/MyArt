from django.forms import ModelForm
from art.models import Comments_art, ArtFolder, Arts

class CommentForm(ModelForm):
    class Meta:
        model = Comments_art
        fields = ['comments_text']

class FolderForm(ModelForm):
    class Meta:
        model = ArtFolder
        fields = ['artfolder_name']

class ArtForm(ModelForm):
    class Meta:
        model = Arts
        fields = ['art_title', 'art_text', 'art_link', 'art_folder']