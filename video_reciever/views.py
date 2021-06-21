from django.shortcuts import render, redirect
from .models import Videos
from django.contrib import messages
import os

def upload_video(request):
     
    if request.method == 'POST' : 
         
        title = request.POST['title']
        video = request.FILES['video']
         

        content = Videos(title=title, video=video)
        content.save()
        file_path = 'media/videos/' + str(video)
        file_size = os.path.getsize(file_path)
        content.size = file_size
        content.save()

        messages.success(request, "Video oploaded successfully!")
        return redirect('videos')
     
    return render(request,'upload.html')

def display(request):
     
    videos = Videos.objects.all()
    context ={
        'videos':videos,
    }
     
    return render(request,'videos.html',context)