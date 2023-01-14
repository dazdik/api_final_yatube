from django.contrib.auth import get_user_model
from django.db import models

CUT_TEXT = 15

User = get_user_model()


class Group(models.Model):
    """Класс Group — модель для группировки постов."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    """Kласс Post — модель для постов."""

    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        blank=True, null=True
    )

    class Meta:
        ordering = ('pub_date', )
        default_related_name = 'posts'

    def __str__(self):
        return self.text[:CUT_TEXT]


class Comment(models.Model):
    """Класс Comment — модель комментирования записей."""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        default_related_name = 'comments'

    def __str__(self):
        return self.text[:CUT_TEXT]


class Follow(models.Model):
    """Класс Follow — модель комментирования записей."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        null=True,
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        null=True,
        verbose_name='Автор'
    )

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_follower'
            )
        ]

    def __str__(self):
        return self.following.username
