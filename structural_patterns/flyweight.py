from __future__ import annotations


class ImageType:
    name: str
    link: str

    def __init__(self, name, link):
        self.name = name
        self.link = link

    def add_to_article(self, article_name):
        print(f'Добавить картинку {self.name} в статью {article_name}.')


class ImageFactory:
    image_types: list[ImageType] = []

    def test_method(self):
        pass

    @classmethod
    def get_image_type(cls, name, link):
        image_type = None
        if len(cls.image_types) > 0:
            for im_t in cls.image_types:
                if im_t.name == name and im_t.link == link:
                    image_type = im_t
                elif im_t.name != name and im_t.link != link:
                    image_type = ImageType(name, link)
                    cls.image_types.append(image_type)
        else:
            image_type = ImageType(name, link)
            cls.image_types.append(image_type)
        return image_type


class Image:
    article_name: str
    type: ImageType

    def __init__(self, article_name, type):
        self.article_name = article_name
        self.type = type

    def add_to_article(self):
        self.type.add_to_article(self.article_name)


image_type1 = ImageFactory.get_image_type('image_type1', 'link1')
print(len(ImageFactory.image_types))

image_type1_duplicate = ImageFactory.get_image_type('image_type1', 'link1')
print(len(ImageFactory.image_types))

image_type2 = ImageFactory.get_image_type('image_type2', 'link2')
print(len(ImageFactory.image_types))


article1_image1 = Image('article1', image_type1)
article1_image1.add_to_article()

article1_image2 = Image('article1', image_type2)
article1_image2.add_to_article()
