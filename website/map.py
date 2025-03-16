from flask import Blueprint, render_template , jsonify
import os

map = Blueprint("map",__name__)

def get_images_for_building(building_id):
    image_folder = f"static/images/{building_id}"
    if not os.path.exists(image_folder):
        return []
    
    images = [f"/{image_folder}/{img}" for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg', '.jpeg'))]
    return images

@map.route('/get_images/<building_id>')
def get_images(building_id):
    images = get_images_for_building(building_id)
    return jsonify(images)