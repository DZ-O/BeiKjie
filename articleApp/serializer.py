from django.contrib.auth.hashers import check_password
from django.core.validators import RegexValidator
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers, validators

from login import models


# 文章信息序列化器
class ArticleSerializer(ModelSerializer):
    article_tag = serializers.PrimaryKeyRelatedField(many=True, queryset=models.ArticleTag.objects.all())

    class Meta:
        model = models.Article
        fields = '__all__'

class CommentsSer(ModelSerializer):

    class Meta:
        model = models.Comments
        fields = '__all__'