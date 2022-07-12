class User:

    def __init__(self, user_id, name, follower=0):
        print("new user being created...")
        self.id = user_id
        self.name = name
        self.followers = follower
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('{:03}'.format(1), "Keeshigan")
user_2 = User('{:03}'.format(2), "Biranugan")

user_1.follow(user_2)

print(f"User 1 Followers: {user_1.followers}")
print(f"User 2 Followers: {user_2.followers}")
print(f"User 1 Following: {user_1.following}")
print(f"User 2 Following: {user_2.following}\n")

user_2.follow(user_1)

print(f"User 1 Followers: {user_1.followers}")
print(f"User 2 Followers: {user_2.followers}")
print(f"User 1 Following: {user_1.following}")
print(f"User 2 Following: {user_2.following}")

