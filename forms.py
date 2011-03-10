from django import forms

from dciphrd.sc2remix.mpyq import is_mpq

class UploadReplayForm(forms.Form):
    replay = forms.FileField()

    def clean_replay(self):
        replay = self.cleaned_data['replay']
        if not is_mpq(replay):
            raise forms.ValidationError("Invalid file type.")
        
        return replay
        
