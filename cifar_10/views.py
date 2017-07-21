# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# coding: utf-8

from pyramid.view import view_config

import helper


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    ori_img_url = request.POST.get('url')
    if ori_img_url:
        img = helper.load_image(ori_img_url)
        mtx = helper.to_matrix(img)
        mtx = helper.normalize(mtx)
        prediction = helper.predict(mtx)
        if 'cloudinary_api_key' in request.registry.settings:
            helper.save_image(img, prediction)
    else:
        prediction = ''
        ori_img_url = None
    return {
        'prediction': prediction,
        'ori_img_url': ori_img_url,
    }
