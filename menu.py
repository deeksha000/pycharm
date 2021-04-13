from database import Database
from model.blog import Blog




class Menu(object):
    def __init__(self):
        # ask author name
        self.user = input("Enter your author name : ")
        self.user_blog = None
        # check if they have an account
        if self._user_has_account():
            print("welcome back {}".format(self.user))
        # if not prompt them to create one
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("enter blog author")
        description = input("enter blog description")
        blog = Blog(author=self.user, title=title, description=description)
        blog.save_to_mongo()

    def run_menu(self):
        # user read or write blogs:
        answer = input("do you want to read(R) or write(W)")
        # if read: list blogs in database and allow to pick one
        # display posts
        if answer == 'R':
            self._list_blogs()
            self._view_blog()

        elif answer == 'W':
            self.user_blog.new_post()
        else:
            print("exit")

    def _list_blogs(self):
        blogs = Database.find(collection='blogs', query={})
        for blog in blogs:
            print("ID : {} , Title: {},Author : {}".format(blog['id'], blog['title'], blog['author']))


    def _view_blog(self):
        blog_to_see=input("enter the id of the blog to read")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {},title {}\n\n{}".format(post['date'], post['title'], post['content']))