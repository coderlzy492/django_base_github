from django.db import models

# Create your models here.

"""
对象关系映射(英语：Object Relational Mapping，简称ORM，或O/RM，或O/R) 
mapping是一种程序设计技术,用于实现面向对象编程语言里不同类型系统的数据之间的转换
从效果上说,它其实是创建了一个可在编程语言里使用的“虚拟对象数据库”
1.模型类都继承自models.Model
2.系统会自动为我们添加一个id主键
3.字段
    字段名=model.类型(选项)
"""


class BookInfo(models.Model):
    """
    book_name:  书本名
    """
    book_name = models.CharField(max_length=10)


class CharacterInfo(models.Model):
    """
    character_name:   人物名
    character_gender:   人物性别
    book:   设置外键
    """
    character_name = models.CharField(max_length=10)
    character_gender = models.BooleanField()
    # 外键约束: 人物属于某一本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)