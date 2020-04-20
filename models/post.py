import uuid
import datetime
from database import Database


class Post(object):
    # Default value parameters are only allowed as last argument || following argument has to also have default value
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = uuid.uuid4().hex if id is None else id
        # post = Post(blog_id='123', title="a title", content="some content', author='Jose')

    def save_to_mongo(self):
        Database.insert(
            collection='posts',
            data=self.json()
        )

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @classmethod
    def from_mongo(cls, id):
        # Post.from_mongo('123')
        post_data = Database.find_one(collection='posts', query={'id': id})
        return cls(blog_id=post_data['blog_if'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   date=post_data['created_date'],
                   id=post_date['id'])

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]
