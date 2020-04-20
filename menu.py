from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        # Ask user for author name
        self.user = input("Enter your author name: ")
        self.user_blog = None
        # Check if they've already got an account
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        # If not, prompt them to create one
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
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(author = self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        # Ask User if they want to read or write blogs?
        read_or_write = input("Do you want to read (R) or write (W) blogs? ")
        if read_or_write == 'R':
            # list blogs from database
            self._list_blogs()
            self._view_blog()
            # allow user to pick one
            # display posts
            pass
        elif read_or_write == 'W':
            # Prompt to write a post
            self.user_blog.new_post()
        else:
            print("Thank you for blogging!")

    def _list_blogs(self):
        blogs = Database.find(collection='blogs',
                              query={})
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blog(self):
        blog_to_see = input("Enter the ID of the blog you'd like to read: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {}, title: {}\n\n{}".format(post['created_date'], post['title'], post['content']))
