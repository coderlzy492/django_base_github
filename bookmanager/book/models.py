from django.db import models

# Create your models here.

"""
对象关系映射(英语：Object Relational Mapping，简称ORM，或O/RM，或O/R) 
mapping是一种程序设计技术,用于实现面向对象编程语言里不同类型系统的数据之间的转换
从效果上说,它其实是创建了一个可在编程语言里使用的“虚拟对象数据库”

1.模型类都继承自models.Model
2.系统会自动为我们添加一个id主键
3.定义类属性 ==> 对应表字段名

    3.1字段名 = model.类型(选项)
    3.2字段名不要使用连续的下划线(__)
    3.3字段类型 ==> MySQL中的类型
    3.4字段选项(非必填)
        verbose_name: 主要用于admin站点
        
4.改变表名称
    默认表名称:子应用名+类名(全部小写)
    
    修改表名称:
"""


class BookInfo(models.Model):
    """
    book_name:      书本名(设置不重复)
    pub_date:       出版日期(允许为空)
    read_count:     阅读量(默认值为0)
    comment_count:  评论量(默认值为0)
    book_is_delete:      是否删除(默认值为否)

    Notes:
        一对多的关系模型中,系统会为我们自动添加一个关系模型类名小写_set
    """
    book_name = models.CharField(max_length=10, unique=False)
    pub_date = models.DateField(null=True)
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    book_is_delete = models.BooleanField(default=False)

    class Meta:
        """
        修改表名称
        """
        db_table = 'bookinfo'

    def __str__(self):
        return self.book_name


class CharacterInfo(models.Model):
    """
    character_name:         人物名(设置不重复)
    character_gender:       人物性别(定义一个有序字典)
    character_description:  人物描述(允许为空)
    character_is_delete:    是否删除(默认值为否)
    book:   设置外键
    """
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )
    character_name = models.CharField(max_length=10, unique=True)
    character_gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    character_description = models.CharField(max_length=100, null=True)
    character_is_delete = models.BooleanField(default=False)

    # 外键约束: 人物属于某一本书,系统会自动为外键添加下划线id
    # 外键的级联操作:
    # 主表 & 从表
    # 主表删除一条数据,从表中有关联的数据有哪些操作??
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        """
        修改表名称
        """
        db_table = 'characterinfo'

    def __str__(self):
        return self.character_name