from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_delete,pre_save,post_init,post_delete,post_save

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print('.....................')
    print('user',User)

 #user_logged_in.connect(login_success,sender=User)

@receiver(user_logged_out,sender=User)
def log_out(sender,request,user,**kwargs):
    print('...........')
    print('user',User)

    user_logged_out.connect(log_out,sender=User)


@receiver(pre_save,sender=User)
def at_beging(sender,instance,**kwargs):
    print('...........')
    print('user',User)

   # pre_save.connect(at_beging,sender=User)


@receiver(post_save,sender=User)
def at_beging(sender,instance,created,**kwargs):
    if created:
      print('...........')
      print('user',User)
    else:
        print('...........')
        print('user',User)

   # pre_save.connect(at_beging,sender=User)




