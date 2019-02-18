from django import forms
from django.core.files.images import get_image_dimensions
from .models import Psychologue


class PsychologueForm(forms.ModelForm):
    """ 
    https://stackoverflow.com/questions/6396442/add-image-avatar-field-to-users-in-django
    https://coderwall.com/p/bz0sng/simple-django-image-upload-to-model-imagefield
    
    """
    class Meta:
        model = Psychologue
        fields = ()
    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        
        try:
            # Validate dimentions
            w, h = get_image_dimensions(avatar)
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                    '%s x %s pixels or smaller' % (max_width, max_height)
                    )
            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar