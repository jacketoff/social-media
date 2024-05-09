import sqlite3

class Db:

    def load_profile(self):
        with sqlite3.connect('social media.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT Username, Name, Bio FROM User WHERE Username=?", (self.username,))
            user_info = cursor.fetchone()  #tuple
            cursor.execute("SELECT COUNT(Followers) FROM Followers WHERE username=?", (self.username,))
            followers = cursor.fetchall()
            cursor.execute("SELECT COUNT(Following) FROM Following WHERE username=?", (self.username,))
            follows = cursor.fetchall()
            cursor.execute("SELECT PostID, Content, Image, Timestamp FROM Post WHERE Username=? ORDER BY Timestamp ASC", (self.username,))
            posts = cursor.fetchall() #tupil
            post_count = len(posts)

            #removes seconds from timestamp
            for i in range(len(posts)):
                post = list(posts[i])
                del posts[i]
                formated_date = post[3][:9]
                post[3] = formated_date
                posts.insert(i,post)    
        return user_info[:3], followers[0][0], follows[0][0], posts, post_count
    
    def get_followers(self): 
        with sqlite3.connect('social media.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT followers FROM followers WHERE username=?", (self.username,))
            followers = cursor.fetchall()
            return followers
    
    def get_following(self):
        with sqlite3.connect('social media.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT following FROM following WHERE username=?", (self.username,))
            following = cursor.fetchall()
            return following
    
     #test this
    def post_info(self, postId): 
        with sqlite3.connect('social media.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT Content, Username, Timestamp FROM Comment WHERE PostID=?", (postId,))
            comment_info = cursor.fetchall()
            cursor.execute("SELECT COUNT(LikeID) FROM Likes WHERE PostID=?", (postId,))
            likes = cursor.fetchone()
            cursor.execute("SELECT Hashtag FROM Hashtag WHERE PostID=?", (postId,))
            hashtags = cursor.fetchall()

        return comment_info, likes, hashtags


    def user_exists(self, username):
        with sqlite3.connect('social media.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT Username FROM User WHERE Username='{username}'")
            user = cursor.fetchone()  

        if user is None:
            return False
        else:
            self.username = user[0]
            return True
        
    def create_user(self):
        pass
        #ADD AN @ INFORT OF USERNAME
        #create default pfp

# db = Db()
# db.user_exists('@user1')
# followers = db.get_followers()
# print(followers)

#[('@user2',), ('@user3',)]

