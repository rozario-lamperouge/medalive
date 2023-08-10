from django import template

register = template.Library()

@register.filter
def file_extension_is_image(value):
    image_extensions = ['jpg', 'jpeg', 'png', 'gif']
    file_extension = value.split('.')[-1].lower()
    return file_extension in image_extensions

@register.filter
def file_extension_is_video(value):
    video_extensions = ['mp4', 'avi', 'mov', 'mkv']
    file_extension = value.split('.')[-1].lower()
    return file_extension in video_extensions
