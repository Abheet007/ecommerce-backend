import os
import drf_yasg

# Get the path to drf-yasg package directory
drf_yasg_path = os.path.dirname(drf_yasg.__file__)

# Construct the paths to static and templates directories
static_path = os.path.join(drf_yasg_path, 'static')
templates_path = os.path.join(drf_yasg_path, 'templates')

print("Path to drf-yasg static files:", static_path)
print("Path to drf-yasg templates:", templates_path)