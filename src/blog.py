import json

from helper import BlogHelper


class Blog(BlogHelper):

  def __init__(self, title, penulis, tanggal, isi):
    self.title = title
    self.penulis = penulis
    self.tanggal = tanggal
    self.isi = isi
    self.data_postingan = {}

    self.posts = []

  # Fitur
  def add_blog(self):
    self.data_postingan["title"] = self.title
    self.data_postingan["penulis"] = self.penulis
    self.data_postingan["tanggal"] = self.tanggal
    self.data_postingan["isi"] = self.isi

    # simpan postingan
    self.posts.append(self.data_postingan)

    # simpan ke json
    self.save(data=self.posts)

  def edit_blog(self):
    pass

  def view_blog(self):
    pass

  def delete_blog(self):
    pass
