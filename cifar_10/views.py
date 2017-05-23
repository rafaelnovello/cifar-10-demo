# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import unicodedata
from datetime import datetime

from pyramid.view import view_config

import requests
import numpy as np
import tensorflow as tf
import cloudinary
import cloudinary.uploader

from io import BytesIO
from PIL import Image


cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET')
)


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    ori_img_url = request.POST.get('url')
    if ori_img_url:
        img = load_image(ori_img_url)
        mtx = to_matrix(img)
        mtx = normalize(mtx)
        prediction = do_magic(mtx)
        process_img_url = save_image(img, prediction)
    else:
        prediction = ''
        ori_img_url = process_img_url = None
    return {
        'prediction': prediction,
        'ori_img_url': ori_img_url,
        'process_img_url': process_img_url
    }


def load_image(url):
    resp = requests.get(url)
    img = Image.open(BytesIO(resp.content))
    img = img.convert('RGB')
    img = img.resize((32, 32))
    return img


def to_matrix(img):
    mtx = np.asarray(img)
    return mtx


def normalize(x):
    """
    Normalize a list of sample image data in the range of 0 to 1
    : x: List of image data.  The image shape is (32, 32, 3)
    : return: Numpy array of normalize data
    """
    x = x.astype('float32')
    x /= 255
    return x


def _load_label_names():
    """
    Load the label names
    """
    labels = [
        "Avião",
        "Automóvel",
        "Passaro",
        "Gato",
        "Cervo",
        "Cão",
        "Sapo",
        "Cavalo",
        "Barco",
        "Caminhão",
    ]
    return labels


def remove_accents(label):
    nfkd_form = unicodedata.normalize('NFKD', label)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii


def save_image(img, label):
    label = remove_accents(label)
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    name = '%s-%s.png' % (label.lower(), now)
    path = '/tmp/%s' % name
    img.save(path)
    name = 'cifar10/%s' % name
    resp = cloudinary.uploader.upload(path, public_id=name)
    return resp['secure_url']


def do_magic(mtx):
    save_model_path = './image_classification'
    loaded_graph = tf.Graph()

    with tf.Session(graph=loaded_graph) as sess:
        # Load model
        loader = tf.train.import_meta_graph(save_model_path + '.meta')
        loader.restore(sess, save_model_path)

        loaded_x = loaded_graph.get_tensor_by_name('x:0')
        loaded_keep_prob = loaded_graph.get_tensor_by_name('keep_prob:0')
        loaded_logits = loaded_graph.get_tensor_by_name('logits:0')

        prediction = tf.argmax(loaded_logits, 1)

        feed_dict = {loaded_x: [mtx], loaded_keep_prob: 1.0}
        best = sess.run([prediction], feed_dict)
        labels = _load_label_names()
        return labels[best[0][0]]
