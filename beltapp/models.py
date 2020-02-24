from django.db import models
import re
import bcrypt


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        print(postData)

        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"

        if len(postData['password']) < 8:
            errors['password'] = "Password too short."
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters."
        if postData['confirm'] != postData['password']:
            errors['confirm'] = "Password must match."
        return errors

    def login_validator(self, postData):
        errors = {}
        if len(User.objects.filter(email=postData['email'])) < 1:
            errors['email'] = "User not found."
        else:
            user = User.objects.get(email=postData['email'])
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['password'] = "Email and Password do not match."
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()



class JobManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 3:
            errors["name"] = "Title should be more than 3 characters"
        if len(postData['desc']) < 3:
            errors["desc"] = "Descrition should be more than 3 characters"
        if len(postData['location']) < 3:
            errors['location'] = 'Location should be more than 3 characters'
        return errors

class Job(models.Model):
    title = models.CharField(max_length=45)
    desc = models.TextField()
    location = models.CharField(max_length=255)
    add = models.BooleanField()
    user = models.ForeignKey(User, related_name="Job", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = JobManager()
