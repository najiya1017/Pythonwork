users=["rahul","rohit","kohli","rishab","sanju","pandya","siraj"]

rahul_followers=["rohit","kohli","rishab","rahul"]

sanju_followers=["sanju","rohit","kohli"]

# users_set=set(users)

# rahul_follower_set=set(rahul_followers)

rahul_suggestion=set(users).difference(set(rahul_followers))

mutual_friends=set(rahul_followers).intersection(set(sanju_followers))

print(mutual_friends)