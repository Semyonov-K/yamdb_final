from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    ROLE_LIST = [
        (ADMIN, 'Admin role'),
        (USER, 'User role'),
        (MODERATOR, 'Moderator role')]

    first_name = models.CharField(
        'first name',
        max_length=30,
        blank=True
    )
    last_name = models.CharField(
        'last name',
        max_length=150,
        blank=True
    )
    email = models.EmailField(unique=True)
    bio = models.TextField(
        'О себе',
        blank=True
    )
    role = models.CharField(
        max_length=10,
        choices=ROLE_LIST,
        default='user'
    )
    confirmation_code = models.CharField(
        max_length=30,
        blank=True
    )

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    class Meta:
        ordering = ('pk',)

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=256)
    year = models.IntegerField(validators=[MaxValueValidator(2022)])
    description = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField(
        Genre, related_name='titles'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        related_name="titles"
    )

    def __str__(self):
        return self.name


class ReviewComment(models.Model):
    text = models.CharField('текст', max_length=256)
    pub_date = models.DateTimeField('дата публикации',
                                    auto_now_add=True, db_index=True)

    class Meta:
        abstract = True


class Review(ReviewComment):
    title = models.ForeignKey(Title, on_delete=models.CASCADE,
                              related_name='reviews',
                              verbose_name='произведение')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='reviews',
                               verbose_name='автор')
    score = models.IntegerField(
        'оценка',
        validators=(MinValueValidator(1), MaxValueValidator(10)),
        error_messages={'validators': 'Оценка 1...10!'}
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(fields=('title', 'author'),
                                    name='unique review')]
        ordering = ('pub_date',)

    def __str__(self):
        return self.text


class Comment(ReviewComment):
    review_field = models.ForeignKey(Review, on_delete=models.CASCADE,
                                     related_name='comments',
                                     verbose_name='комментарий')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='автор')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
