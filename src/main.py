from blog import Blog


if __name__ == "__main__":
  title = input("Masukan Judul Postingan: ")
  penulis = input("Author: ")
  isi = input("Masukan Konten: ")
  blog = Blog(title=title, penulis=penulis, isi=isi, tanggal="10")
  blog.add_blog()