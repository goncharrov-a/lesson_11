from data.user_factory import UserFactory

users = [UserFactory.create() for _ in range(3)]
