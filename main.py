from fastapi import FastAPI
from fastapi.params import Body     #--> To perform activities like extraction from the body
from pydantic import BaseModel
from typing import Optional
#instance of FastAPI - app of Fastapi
app = FastAPI()


#Post class inherited from BaseModel for Schema Validation
class Post(BaseModel):
    title: str
    content: str
    rating: Optional[int] = None   # Optional Validation
    published: bool = True         # Default Validation


#Routing to '/' endpoint
@app.get('/')
async def root():
    return {'message': 'Hello Fast!!'}


@app.post('/posts')
def create_post(post: Post):
    return {
        'post_status': 'Updated successfully',
        'post_validation': 'Schema is validated successfully',
        'post_title': post.title,
        'post_content': post.content,
        'post_rating': post.rating,
        'post_publish_status': post.published

    }

'''
The above and below methods have the same route,
but the first one will be consired
'''
@app.post('/posts')
def create_post(data: dict = Body()):       #---> Extract data from the body and stores it as dictionary
    return {'new_post_statue': 'Post updated Successfully',
            'post_title': data['title'],
            'post_content': data['content']}
