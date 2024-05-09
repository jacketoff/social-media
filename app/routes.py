from flask import render_template, redirect, url_for, request
from app import app
from app.videos import Videos
from app.db import Db

video = Videos()
db = Db()

@app.route('/')      
@app.route('/index', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        search = request.form['search']
        if search[0] == '@':
            print('searching for user')
            profiles = db.user_exists(search)
            print(profiles)
            if profiles:                          
                return redirect(url_for('profile')) 
        print('/n searching for video')        
        video.search(search)
        return redirect(url_for('videos'))    
    return render_template('index.html')

@app.route('/profile')
def profile():
    user_info,followers, following, posts, post_count = db.load_profile()
    username, name , bio = user_info[:3]

            #how to display posts 
    
    return render_template('profile.html',username=username,name=name
                           ,bio=bio, followers=followers,following=following,posts=posts,
                           post_count=post_count)

@app.route('/followers')
def followers():
    followers_list = db.get_followers()
    return render_template('followers.html',followers_list=followers_list)

@app.route('/following')
def following():
    following_list = db.get_following()
    return render_template('following.html',following_list=following_list)

@app.route('/video', methods = ['GET', 'POST'])
def videos():

    if request.method == 'POST':           
        if 'next' in request.form:
            link, video_index, page = video.search('next')
            return render_template('videos.html', link=link,video_index=video_index,page=page)
        
        elif 'back' in request.form:
            link, video_index, page = video.search('back')
            return render_template('videos.html', link=link,video_index=video_index,page=page)
        
    else:
        link, video_index, page = video.search('none')
        return render_template('videos.html',link=link,video_index=video_index,page=page)






 
















