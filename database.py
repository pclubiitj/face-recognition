from peewee import PostgresqlDatabase, Model, CharField, IntegrityError
import psycopg2
db = PostgresqlDatabase('database_name', user='username', password='pass',
                        host='127.0.0.1', port=1234)


class Base(Model):
    class Meta:
        database = db


class Image(Base):
    origin_image = CharField()
    extract_image = CharField(unique=True, primary_key=True)


db.connect()
conn = psycopg2.connect(
    dbname="database_name",
    user="username",
    host='127.0.0.1',
    password="pass",
    port=1234
)
db.create_tables(Image)


def match(origin, extract):
    try:
        with db.atomic():
            img = Image.create(origin_image=origin, extract_image=extract)
            img.save()
    except IntegrityError:
        print("The extract image exists")
    db.close()


# match("abc980000", "abc100001")
# match("abc5", "abc6")
# match("abc7", "abc11")
# img = Image.select().order_by(Image.origin_image)
# print(img)
# for i in img:
#     print("{} {} " .format(i.origin_image, i.extract_image))
