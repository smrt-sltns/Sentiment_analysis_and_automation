from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from facebook.models import AccountsAd



# users can add up to three emails 
# class EmailModel(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     email = models.EmailField(null=False, blank=False, unique=True)
#     email_count = models.IntegerField(default=1)
#     is_email_confirmed = models.BooleanField(default=False)
#     def __str__(self):
#         return f"{self.email}, {self.user.username}"
    

#logic building 
#each negative comments needs to be saved even if an ad has multiple of them 
class LogNegativeComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    adaccount = models.ForeignKey(AccountsAd, on_delete=models.CASCADE)

    comment = models.CharField(max_length=100, null=True, blank=True) # comments can also be just emojis 
    comment_id = models.CharField(max_length=100, null=False, blank=False)

    ad_name = models.CharField(max_length=100, null=True, blank=True)
    ad_id = models.CharField(max_length=100, null=True, blank=True)

    adset_name = models.CharField(max_length=100, null=True, blank=True)
    adset_id = models.CharField(max_length=100, null=True, blank=True)
    
    campaign_name = models.CharField(max_length=100, null=True, blank=True)
    campaign_id = models.CharField(max_length=100, null=True, blank=True)

    created_time = models.CharField(max_length=100, null=True, blank=True) # comment created date 
    is_mail_sent = models.BooleanField(default=False) # was mail sent for the comment?
    automation_runtime = models.DateTimeField(auto_now_add=True,null=True, blank=True) 

    class Meta:
        verbose_name_plural = "Log Negative Comments"

    def __str__(self):
        title = f" {self.comment} | {self.ad_name} | {self.campaign_name} ( {self.user.username})"
        return title 
    
    # def save(self, *args, **kwargs):
    #     if not self.automation_runtime:
    #         self.automation_runtime = timezone.now()
    #     super(LogNegativeComments, self).save(*args, **kwargs)


"""
flow of positive comment log 

"""
class LogPositiveComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    adaccount = models.ForeignKey(AccountsAd, on_delete=models.CASCADE)

    comment_count = models.IntegerField(default=0)

    campaign_id = models.CharField(max_length=100, null=True, blank=True)
    campaign_name = models.CharField(max_length=100, null=True, blank=True)

    adset_id = models.CharField(max_length=100, null=True, blank=True)
    adset_name = models.CharField(max_length=100, null=True, blank=True)

    ad_id = models.CharField(max_length=100, null=True, blank=True) 
    ad_name = models.CharField(max_length=100, null=True, blank=True)

    created_time = models.CharField(max_length=100, null=True, blank=True)
    is_mail_sent = models.BooleanField(default=False)
    automation_runtime = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta: 
        verbose_name_plural = "Log Positive Comments"
    def __str__(self):
        title = f"{self.user.username}, {self.comment_count} | {self.created_time}"
        return title 

    # def save(self, *args, **kwargs):
    #     if not self.automation_runtime:
    #         self.automation_runtime = timezone.now()
    #     super(LogPositiveComments, self).save(*args, **kwargs)