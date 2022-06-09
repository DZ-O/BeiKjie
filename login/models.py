from django.db import models

# Create your models here.
from django.contrib.auth.models import User, AbstractUser


# import articleApp
class UserDetail(AbstractUser):
    username = models.CharField(blank=True,null=True,unique=True, verbose_name='用户名', help_text="用户名",max_length=10)
    password = models.CharField(max_length=255,default='',help_text='密码',verbose_name='密码')
    email = models.EmailField(blank=True,null=True,help_text='邮箱',verbose_name='邮箱')
    phone = models.CharField(verbose_name='手机号码', help_text="手机号码",max_length=30)
    signature = models.CharField(default='神秘客？懒人？', max_length=100, verbose_name="个性签名", help_text="个性签名")
    identity = models.CharField(max_length=10, null=True, verbose_name='身份', help_text="官方身份")
    subscribe_count = models.IntegerField(default=0, verbose_name='关注人数', help_text='关注人数')
    collect_count = models.IntegerField(default=0, verbose_name='收藏人数', help_text='收藏人数')
    fans_count = models.IntegerField(default=0, verbose_name='粉丝人数', help_text='粉丝人数')
    praise_count = models.IntegerField(default=0, verbose_name='获赞总数', help_text='获赞总数')
    been_read_count = models.IntegerField(default=0, verbose_name='被阅读总数', help_text='被阅读总数')
    SignIn = models.IntegerField(default=0, verbose_name='签到天数', help_text='签到天数')
    icon = models.ImageField(default='icon/default.png',upload_to='icon')
    subscribe_to = models.ManyToManyField(to='self',
                                          through='SubscriptionRelactionship',
                                          through_fields=('user', 'subscribed'))
    collect_to = models.ManyToManyField(to='Article',
                                        through='CollectRelactionship',
                                        through_fields=('user', 'article')
                                        )


class SubscriptionRelactionship(models.Model):
    user = models.ForeignKey(to=UserDetail, on_delete=models.CASCADE, verbose_name='用户id', help_text='用户id')
    subscribed = models.ForeignKey(to=UserDetail, on_delete=models.CASCADE, verbose_name='关注的用户id',
                                   help_text='关注的用户id', related_name='UserDetail1')


class ArticleType(models.Model):
    type = models.CharField(max_length=10, verbose_name='文章分类', help_text='文章分类')


class ArticleTag(models.Model):
    tag = models.CharField(max_length=10, verbose_name='文章标签', help_text='文章标签')


# Create your models here.
class Article(models.Model):
    auth = models.ForeignKey(to=UserDetail, on_delete=models.CASCADE, help_text='作者id', verbose_name='作者id')
    title = models.CharField(max_length=20, verbose_name='文章标题', help_text='文章标题')
    introduction = models.CharField(max_length=100, default='', verbose_name='文章简介', help_text='文章简介')
    article_content = models.TextField(verbose_name='文章内容', help_text='文章内容')
    like_count = models.IntegerField(default=0, verbose_name='点赞数', help_text='点赞数')
    dislike_count = models.IntegerField(default=0, verbose_name='点踩数', help_text='点踩数')
    read_count = models.IntegerField(default=0, verbose_name='被观看次数', help_text='被观看次数')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, help_text='创建时间')
    revise_time = models.DateTimeField(verbose_name='修改时间', auto_now=True, help_text='修改时间')
    article_type = models.ForeignKey(to=ArticleType, on_delete=models.CASCADE)
    article_tag = models.ManyToManyField(to=ArticleTag,
                                         through='Article2ArticleTag',
                                         through_fields=('article', 'article_tag')
                                         )


class CollectRelactionship(models.Model):
    user = models.ForeignKey(to=UserDetail, on_delete=models.CASCADE, verbose_name='收藏者id', help_text='收藏者id')
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, verbose_name='收藏文章id', help_text='收藏文章id')


class Article2ArticleTag(models.Model):
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, verbose_name='文章id', help_text='文章id')
    article_tag = models.ForeignKey(to=ArticleTag, on_delete=models.CASCADE, verbose_name='文章标签id',
                                    help_text='文章标签id')


class Comments(models.Model):
    comment_content = models.TextField(verbose_name='评论内容', help_text='评论内容')
    comment_article = models.ForeignKey(to=Article, on_delete=models.CASCADE, verbose_name='评论的文章id',
                                        help_text='评论的文章id')
    father_comment = models.ForeignKey(to='self', on_delete=models.CASCADE, verbose_name='父评论的id',
                                       help_text='父评论id')
    comment_user = models.ForeignKey(to=UserDetail, on_delete=models.CASCADE, verbose_name='评论者id',
                                     help_text='评论者id')
    comment_like_count = models.IntegerField(default=0, verbose_name='评论点赞数', help_text='评论点赞数 ')
    comment_dislike_count = models.IntegerField(default=0, verbose_name='评论点踩数', help_text='评论点踩数 ')
