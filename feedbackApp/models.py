from django.db import models

# Create your models here.
from login.models import UserDetail

class Feedback(models.Model):
    feedback_user = models.ForeignKey(to=UserDetail,verbose_name='反馈人id',help_text='反馈人id',on_delete=models.CASCADE)
    feedback_content = models.TextField(verbose_name='反馈内容',help_text='反馈内容')
    choose = models.IntegerField(default=0,verbose_name='解决状态',help_text='解决状态,1:已解决;0:未解决')

class FeedbackReplys(models.Model):
    feedback = models.ForeignKey(to=Feedback,verbose_name='反馈问题id',help_text='反馈问题id',on_delete=models.CASCADE)
    reply = models.TextField(verbose_name='回复问题',help_text='回复问题')
    father_reply = models.ForeignKey(to='self',verbose_name='父回复id',help_text='父回复id',on_delete=models.CASCADE)
    user_id = models.ForeignKey(to=UserDetail,on_delete=models.CASCADE,verbose_name='反馈人id',help_text='反馈人id')
    accept_user = models.ForeignKey(to=UserDetail,on_delete=models.CASCADE,verbose_name='受理人id',help_text='受理人id',related_name='UserDetail2')