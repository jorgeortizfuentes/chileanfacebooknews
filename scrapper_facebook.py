from facebook_scraper import get_posts
import datetime
import random
import time
import os
import csv
import pandas as pd


def check_file(filename):
    if os.path.exists(filename):
        return {'a_w': 'a', 'w_h': False}
    else:
        return {'a_w': 'w', 'w_h': True}


def write_file(filename, fields, row):
    check = check_file(filename)
    with open(filename, mode=check['a_w'], newline='', encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        if check['w_h']:
            writer.writeheader()
        writer.writerow(row)
        csv_file.close()


n_scrolls = 1000000000000000  # None
post_per_scroll = None
page = "RadioBioBio"
path = "/Users/jorge/Facebook/"

tot_counter = 0
counter = 0

# Create csv files
# Post
posts_filename = path+"posts-{}.csv".format(page)
posts_fields = ['post_id', 'text', 'post_text', 'shared_text', 'time', 'image', 'image_lowquality', 'images', 'images_description', 'images_lowquality', 'images_lowquality_description', 'video', 'video_duration_seconds', 'video_height', 'video_id', 'video_quality',	'video_size_MB', 'video_thumbnail',	'video_watches', 'video_width',
                'likes', 'comments', 'shares', 'post_url', 'link', 'user_id', 'username', 'user_url', 'is_live', 'factcheck', 'shared_post_id', 'shared_time', 'shared_user_id', 'shared_username', 'shared_post_url', 'available', 'comments_full', 'reactors', 'w3_fb_url', 'reactions', 'reaction_count', 'image_id', 'image_ids', 'fetched_time']

import os

existe = os.path.isfile(posts_filename)
if existe == False:
    df = pd.DataFrame(columns=posts_fields)
    df.to_csv(posts_filename, index=False)

posts = []
for full_post in get_posts(page, youtube_dl=False, pages=n_scrolls, timeout=600, cookies=path+"cookies.json", extra_info=True,
                           options={
                               "comments": False,
                               "reactors": True,
                               "post_per_page": 200,
                           }):

    try:
        tot_counter += 1

        # if (full_post['time'] <= start_date) | (full_post['time'] >= end_date):  # if date is out of range do not extract
        #     raise ValueError('Of of date range.')

        # if full_post['time'] <= start_date:  # if date is out of range do not extract
        #    raise ValueError('Of of date range.')

        counter += 1
        print('total_count: ', end=''), print(tot_counter, end=' | ')
        print('post_count: ', end=''), print(counter, end=' | ')
        print('post_date: ', end=''), print(full_post['time'], end=' | ')
        print('fetch_date: ', end=''), print(datetime.datetime.now())
        
        post = {
            'post_id': full_post['post_id'],
            'post_url': full_post['post_url'],
            'text': full_post['text'],
            'time': full_post['time'],
            'n_reactions': full_post['reaction_count'],
            'n_comments': full_post['comments'],
            'n_shares': full_post['shares']
        }

        post = {
            'post_id': full_post['post_id'],
            'text': full_post['text'],
            'post_text': full_post['post_text'],
            'shared_text': full_post['shared_text'],
            'time': full_post['time'],
            'image': full_post['image'],
            'image_lowquality': full_post['image_lowquality'],
            'images': full_post['images'],
            'images_description': full_post['images_description'],
            'images_lowquality': full_post['images_lowquality'],
            'images_lowquality_description': full_post['images_lowquality_description'],
            'video': full_post['video'],
            'video_duration_seconds': full_post['video_duration_seconds'],
            'video_height': full_post['video_height'],
            'video_id': full_post['video_id'],
            'video_quality': full_post['video_quality'],
            'video_size_MB': full_post['video_size_MB'],
            'video_thumbnail': full_post['video_thumbnail'],
            'video_watches': full_post['video_watches'],
            'video_width': full_post['video_width'],
            'likes': full_post['likes'],
            'comments': full_post['comments'],
            'shares': full_post['shares'],
            'post_url': full_post['post_url'],
            'link': full_post['link'],
            'user_id': full_post['user_id'],
            'username': full_post['username'],
            'user_url': full_post['user_url'],
            'is_live': full_post['is_live'],
            'factcheck': full_post['factcheck'],
            'shared_post_id': full_post['shared_post_id'],
            'shared_time': full_post['shared_time'],
            'shared_user_id': full_post['shared_user_id'],
            'shared_username': full_post['shared_username'],
            'shared_post_url': full_post['shared_post_url'],
            'available': full_post['available'],
            # 'comments_full': full_post['comments_full'],
            'reactors': full_post['reactors'],
            'w3_fb_url': full_post['w3_fb_url'],
            'reactions': full_post['reactions'],
            'reaction_count': full_post['reaction_count'],
            'image_id': full_post['image_id'],
            'image_ids': full_post['image_ids'],
            'fetched_time': datetime.datetime.now(),
        }
        posts.append(post)
        if (counter % 100) == 0:
            df2 = pd.DataFrame(posts)
            df2.to_csv(posts_filename, index=False, header=False, mode='a')
            posts = []
            sleep_time = random.randint(1, 12)
    
    #write_file(posts_filename, posts_fields, post)
    # guardar
    
    except Exception as e:
        print(e)
        sleep_time = random.randint(30, 120)
        print("sleeping {}sec.".format(sleep_time))
        time.sleep(sleep_time)
