# coding: utf-8

import unicodedata
from datetime import datetime

import requests
import numpy as np
import tensorflow as tf
import cloudinary
import cloudinary.uploader

from io import BytesIO
from PIL import Image


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


def predict(mtx):
    save_model_path = './cifar_10/model/image_classification'
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
