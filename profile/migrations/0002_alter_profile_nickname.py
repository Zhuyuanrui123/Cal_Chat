# Generated by Django 4.0.4 on 2022-04-28 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(choices=[('Poet', 'Poet'), ('Scale', 'Scale'), ('Gear', 'Gear'), ('Calc', 'Calc'), ('Beaker', 'Beaker'), ('Helix', 'Helix'), ('Mouse', 'Mouse'), ('Atom', 'Atom'), ('Alice', 'Alice'), ('Bob', 'Bob'), ('Jones', 'Jones'), ('Evans', 'Evans'), ('White', 'White'), ('Black', 'Black'), ('Jackson', 'Jackson'), ('Hill', 'Hill'), ('Clark', 'Clark'), ('Lee', 'Lee'), ('Mills', 'Mills'), ('Jerry', 'Jerry'), ('Tom', 'Tom'), ('Sam', 'Sam'), ('Amy', 'Amy'), ('Allen', 'Allen'), ('Anna', 'Anna'), ('Young', 'Young'), ('Ken', 'Ken'), ('Sara', 'Sara'), ('Shirley', 'Shirley')], max_length=12),
        ),
    ]
