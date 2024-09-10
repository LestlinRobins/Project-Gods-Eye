from instagramy import InstagramUser
 
def getProfileDetails(name):
# Connecting the profile
    session_id = "7522562178%3AefSRQHpet7c5uS%3A14%3AAYdfPUsSTvvtQtRnbkS1wNcCPiPVAD9YSKP-8Lodxg"
    user = InstagramUser(name, sessionid=session_id)
    
    # printing the basic details like
    # followers, following, bio
    print(user.is_verified())
    print(user.popularity())
    bio = user.get_biography()
    
    # return list of dicts
    posts = user.get_posts_details()
    
    print('\n\nLikes', 'Comments')
    return [posts, bio]

getProfileDetails('lestlin_robins')