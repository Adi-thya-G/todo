from account.models import Todo_table
from celery import shared_task
from django.core.mail import send_mail
from django.utils.timezone import now
from datetime import timedelta
from todo.settings import EMAIL_HOST_USER
import logging

# Set up logging
logger = logging.getLogger(__name__)

@shared_task(bind=True)
def send_mail_func(self):
    # Get the current time
    current_time = now()

    # Calculate one hour ahead
    one_hour_ahead = current_time + timedelta(hours=1)

    # Get tasks whose deadlines are between now and one hour ahead
    tasks = Todo_table.objects.filter(
        deadline__lte=one_hour_ahead,  # Tasks with a deadline before or equal to one hour from now
        deadline__gt=current_time,    # Tasks with a deadline after the current time
        is_completed=False            # Only tasks that are not completed
    )

    # Check if any tasks are found
    # Log the number of tasks found
    logger.info(f"Found {len(tasks)} tasks due in the next hour.")
    
    # Send email for each task
    for task in tasks:
        user_email = task.user_id # Assuming the email is stored in the 'username' field
        if user_email:  # Ensure there is an email before sending
            print(f"Sending email to: {user_email}")  # Print the email to check its value
            
            subject = f"Reminder: Your Deadline for '{task.title}' is Approaching in 1 Hour!"
            message = f"""
            Dear {task.user_id.username},

            This is a friendly reminder that the deadline for your task "{task.title}" is in 1 hour, set for {task.deadline}.
            
            Please make sure to review your progress and complete any remaining steps before the deadline.

            Best regards,
            Your Todo Application Team
            """

            # Send the email
            send_mail(subject, message, EMAIL_HOST_USER, [user_email], fail_silently=False)
           
    
    return f"Sent email reminders for {len(tasks)} tasks."
