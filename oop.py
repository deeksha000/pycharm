from model.post import Post
from database import Database

Database.initialize()
post_3 = Post('223', 'great_cost', 'sample_content', 'piku')
post_3.save_to_mongo()
post_1 = Post.from_mongo("1dbc9584ea0a45f584cf7abb6b20969d")
print(post_1)
post_2 =Post.from_blog('223')
i=0
for po in post_2:
    i+=1
    print(po)
print(i)
