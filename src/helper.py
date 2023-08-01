import json
from os.path import join

from config import Config as cfg


class BlogHelper(object):
  def save(self, data):
    with open(join(cfg.BASE_DIR, "posts.json"), "w+") as file:
      print("simpan postingan")
      json.dump(data, file)