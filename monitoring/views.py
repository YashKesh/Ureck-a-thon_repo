from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
import docker
def homepage(request):
    return render(request,"firstboard.html")

from datetime import datetime
from django.utils import timezone
from dateutil import parser

def list_docker_images(request):
    client = docker.from_env()
    try:
        # Get a list of all Docker images
        images = client.images.list()
        # Get the total number of Docker images
        total_images = len(images)

        # Get a list of all Docker containers
        containers = client.containers.list(all=True)
        # Get the total number of Docker containers
        total_containers = len(containers)
        # Get the total number of running containers
        running_containers = sum(1 for container in containers if container.status == 'running')
        stopped_containers = sum(1 for container in containers if container.status == 'exited')
        # Extract image details
        image_details = []
        current_time = timezone.now()
        for image in images:
            image_id = image.short_id.split(':')[1][:10]

            # Convert image size to MB
            image_size = round(image.attrs['Size'] / (1024 * 1024), 2)
            created_time = parser.parse(image.attrs['Created']).replace(tzinfo=None)  # Remove timezone information
            created_time = timezone.make_aware(created_time)  # Make the datetime object timezone-aware
            time_difference = current_time - created_time
            days_ago = time_difference.days
            image_info = {
                'repository': image.tags[0] if image.tags else '',
                'id': image_id,
                'size': f"{image_size} MB",
                'created': f"{days_ago} days ago"
            }
            image_details.append(image_info)
        return render(request, 'firstboard.html', {'images': image_details, 'total_images': total_images, 'total_containers': total_containers,'running_containers':running_containers,'stopped_containers':stopped_containers})
    except docker.errors.APIError as e:
        return render(request, 'firstboard.html', {'error': str(e)})
    except Exception as e:
        return render(request, 'firstboard.html', {'error': str(e)})