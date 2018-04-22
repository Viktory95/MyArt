from django.http.response import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from art.models import Arts, Comments_art, ArtFolder
from django.core.exceptions import ObjectDoesNotExist
from art.forms import CommentForm, FolderForm, ArtForm
from django.template.context_processors import csrf
from django.contrib import auth


def userfolders(request):
    user_folders_var = ArtFolder.objects.filter(artfolder_user=auth.get_user(request).id)
    artsinforder = {}
    for user_older in user_folders_var:
        artsinforder[user_older.id] = Arts.objects.filter(art_folder=user_older.id)[:4]
    return render_to_response('userfolders.html',
                              {'folders': ArtFolder.objects.filter(artfolder_user=auth.get_user(request).id),
                               'username': auth.get_user(request).username,
                               'folderarts': artsinforder})

def folderadd(request):
    folder_form = FolderForm
    args = {}
    args.update(csrf(request))
    args['form'] = folder_form
    args['username'] = auth.get_user(request).username
    return render_to_response('folderadd.html', args)


def addartinfolder(request, art_id):
    folder_form = FolderForm
    args = {}
    args.update(csrf(request))
    args['form'] = folder_form
    args['username'] = auth.get_user(request).username
    args['art_id'] = art_id
    args['folders'] = ArtFolder.objects.filter(artfolder_user=auth.get_user(request).id)
    return render_to_response('addartinfolder.html', args)


def addartinoldfolder(request, art_id):
    args = {}
    args.update(csrf(request))
    if request.POST:
        folder = ArtFolder.objects.get(id=request.POST.getlist('folder_id')[0])
        art = Arts.objects.get(id=art_id)
        newArt = Arts.objects.create()
        newArt.art_folder = folder
        newArt.art_title = art.art_title
        newArt.art_text = art.art_text
        newArt.art_likes = 0
        newArt.art_link = art.art_link
        newArt.save()
    return redirect('/arts/all/')


def addfolderpost(request):
    if request.POST:
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.artfolder_user = auth.get_user(request)
            form.save()
    return redirect('/arts/all/')


def addfolderwithart(request, art_id):
    if request.POST:
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.artfolder_user = auth.get_user(request)
            form.save()
            art = Arts.objects.get(id=art_id)
            art1 = Arts.objects.create()
            art1.art_folder = folder
            art1.art_title = art.art_title
            art1.art_text = art.art_text
            art1.art_likes = 0
            art1.art_link = art.art_link
            art1.save()
    return redirect('/arts/all/')

def artsfromfolder(request, folder_id):
    return render_to_response('artsfromfolder.html',
                              {'arts': Arts.objects.filter(art_folder=folder_id), 'username': auth.get_user(request).username})

def addart(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['folders'] = ArtFolder.objects.filter(artfolder_user=auth.get_user(request).id)
    return render_to_response('artadd.html', args)

def arts(request):
    return render_to_response('arts.html',
                              {'arts': Arts.objects.all(), 'username': auth.get_user(request).username})

def art(request, art_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['art'] = Arts.objects.get(id=art_id)
    args['comments'] = Comments_art.objects.filter(comments_arts_id=art_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('art.html', args)


def addlike(request, art_id):
    try:
        art = Arts.objects.get(id=art_id)
        art.art_likes += 1
        art.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/arts/all')

def addcomment(request, art_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_arts = Arts.objects.get(id=art_id)
            comment.comments_user = auth.get_user(request)
            form.save()
    return redirect('/art/%s/' % art_id)

def addartpost(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        new_art = Arts.objects.create()
        new_art.art_title = request.POST.get('art_title', '')
        new_art.art_text = request.POST.get('art_text', '')
        new_art.art_link = request.POST.get('art_link', '')
        new_art.art_folder = ArtFolder.objects.get(id=request.POST.getlist('folder_id')[0])
        new_art.save()
    return redirect('/arts/all/')