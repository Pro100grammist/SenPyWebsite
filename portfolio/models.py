from django.db import models


class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class HardSkill(models.Model):
    title = models.CharField(max_length=100)
    url_name = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.title


class NecessaryUseful(models.Model):
    title = models.CharField(max_length=100)
    url_name = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.title


class IDE(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/dropmenu/ides/')
    url = models.URLField()
    rating = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class WebFrameworks(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/dropmenu/web/')
    url = models.URLField()
    rating = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class Data(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/dropmenu/data/')
    url = models.URLField()
    rating = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class WebServers(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/dropmenu/server/')
    url = models.URLField()
    rating = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class FrontEnd(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/dropmenu/frontend/')
    url = models.URLField()
    rating = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class GitServices(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/dropmenu/git_serv/')
    url = models.URLField()
    rating = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class PaaS(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/dropmenu/paas/')
    url = models.URLField()
    rating = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class LearningPlatform(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/dropmenu/platform/')
    url = models.URLField()
    rating = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/dropmenu/education/')
    url = models.URLField()
    rating = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class CodingSimulator(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/dropmenu/cs/')
    url = models.URLField()
    rating = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class Certificates(models.Model):
    url = models.URLField()
    image = models.ImageField(upload_to='portfolio/about/')
    alt = models.CharField(max_length=100)

    def __str__(self):
        return self.alt
