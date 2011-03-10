from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.utils.encoding import smart_str

# Create a function to handle the uploaded file
# eg. Send the file to the parser and tar the output.
from dciphrd.sc2remix.models import SC2Replay
from dciphrd.sc2remix.forms import UploadReplayForm
from dciphrd.sc2remix.utils import *
from dciphrd.sc2remix.handlers import REPLAY_PATH
from dciphrd.sc2remix.handlers import handle_uploaded_replay

def upload_replay(request):
    if request.method == 'POST':
        form = UploadReplayForm(request.POST, request.FILES)
        if form.is_valid():
            replay = request.FILES['replay']
            id = handle_uploaded_replay(replay)
            r = get_object_or_404(SC2Replay, id=id)
            url = int_to_base62(id)
            return HttpResponseRedirect('/r/%s' % url)
    else:
        form = UploadReplayForm()
    return render_to_response('sc2remix/upload.html', {'form': form})

def parsed(request, r_id):
    if request.method == 'GET':
        get_object_or_404(SC2Replay, id=base62_to_int(r_id))
        return render_to_response('sc2remix/parsed.html', {'url': r_id})
    else:
        raise Http404

def download_replay(request, r_id):
    if request.method == 'GET':
        r = get_object_or_404(SC2Replay,  id=base62_to_int(r_id))
        response = HttpResponse(mimetype='application/force-download')
        response['Content-Type'] = 'application/SC2Replay'
        response['X-Accel-Redirect'] = '/r/d/files/%s/%s' % (smart_str(r_id),smart_str(r.filename))
        response['Content-Disposition'] = 'attachment;filename=%s' % smart_str(r.filename)
    else:
        raise Http404
    return response

def download_archive(request, r_id):
   if request.method == 'GET':
       r = get_object_or_404(SC2Replay, id=base62_to_int(r_id))
       response = HttpResponse(mimetype='application/force-download')
       response['Content-Type'] = 'application/zip'
       response['X-Accel-Redirect'] = '/r/a/d/files/%s/%s' % (smart_str(r_id),smart_str(r.filename+'.zip'))
       response['Content-Disposition'] = 'attachment;filename=%s' % smart_str(r.filename+'.zip')
   else:
       raise Http404
   return response
