from django.db import models


class Client(models.Model):

    Name_cl = models.CharField(max_length=50, verbose_name="Ім'я:")
    Surname_cl = models.CharField(max_length=50, verbose_name="Прізвище:")
    Po_batk_cl = models.CharField(max_length=50, verbose_name="По-батькові:")
    Seria_passport = models.CharField(max_length=50, verbose_name="Серія паспорту:")
    Nomer_passport = models.CharField(max_length=50, verbose_name="Номер паспорту:")

    def __str__(self):
        return f'{self.Surname_cl} {self.Name_cl} {self.Po_batk_cl}'


    class Meta:
        verbose_name = 'Клієнт'
        verbose_name_plural = 'Клієнти'


class Osvita(models.Model):

    Bal_osviti = models.FloatField()
    Name_osviti = models.CharField(max_length=50)

    def __str__(self):
        return self.Name_osviti


    class Meta:
        verbose_name = 'Освітній рівень'
        verbose_name_plural = 'Освітні рівні'


class Vik(models.Model):
    
    Bal_viku = models.FloatField()
    Vik = models.IntegerField()

    def __str__(self):
        if self.Vik == 18:
            return f'{self.Vik} - 23'
        elif self.Vik == 23:
            return f'{self.Vik} - 27'
        elif self.Vik == 27:
            return f'27 - 36'
        elif self.Vik == 36:
            return f'36 - 46'
        elif self.Vik == 46:
            return f'46 - 60'
        else:
            return f'60 або старіше'


    class Meta:
        verbose_name = 'Вік'
        verbose_name_plural = 'Вікові категорії'


class Posada (models.Model):

    Bal_posadi = models.FloatField()
    Name_posadi = models.CharField(max_length=50)

    def __str__(self):
        return self.Name_posadi


    class Meta:
        verbose_name = 'Посада'
        verbose_name_plural = 'Посади'


class Dohid(models.Model):

    Bal_dohodu = models.FloatField()
    Range_dohodu = models.IntegerField()


    def __str__(self):
        return f'{self.Range_dohodu}'

    
    class Meta:
        verbose_name = 'Дохід'
        verbose_name_plural = 'Доходи'
    

class Diti(models.Model):

    Bal_ditey = models.FloatField()
    Kilkist_ditey = models.IntegerField()

    def __str__(self):
        return f'{self.Kilkist_ditey}'


    class Meta:
        verbose_name = 'Кількість дітей'
        verbose_name_plural = 'Кількість дітей'


class Sfera_roboti(models.Model):

    Bal_sferi = models.FloatField()
    Name_Sferi = models.CharField(max_length=50)

    def __str__(self):
        return self.Name_Sferi


    class Meta:
        verbose_name = 'Сфера роботи'
        verbose_name_plural = 'Сфери роботи'


class Family_stan(models.Model):

    Bal_stanu = models.FloatField()
    Name_stanu = models.CharField(max_length=50)

    def __str__(self):
        return self.Name_stanu


    class Meta:
        verbose_name = 'Сімейне положення'
        verbose_name_plural = 'Сімейне положення'


class Stat(models.Model):

    Bal_stati = models.FloatField()
    Name_stati = models.CharField(max_length=50)

    def __str__(self):
        return self.Name_stati


    class Meta:
        verbose_name = 'Стать'
        verbose_name_plural = 'Стать'


class Bajana_suma_creditu(models.Model):

    Bal_sumi = models.FloatField()
    Znachennya_creditu = models.CharField(max_length=50)

    def __str__(self):
        return self.Znachennya_creditu


    class Meta:
        verbose_name = 'Можлива сума кредиту'
        verbose_name_plural = 'Можлива сума кредиту'


class Anketa(models.Model):

    Code_Stati = models.ForeignKey(
        Stat,
        on_delete=models.CASCADE,
        related_name='ankets'
    )
    Code_Stanu = models.ForeignKey(
        Family_stan,
        on_delete=models.CASCADE,
        related_name='ankets'
    )
    Code_Sferi = models.ForeignKey(
        Sfera_roboti,
        on_delete=models.CASCADE,
        related_name='ankets'
    )
    Code_Viku = models.ForeignKey(
        Vik,
        on_delete=models.CASCADE,
        related_name='ankets'
    )
    Code_ditey = models.ForeignKey(
        Diti,
        on_delete=models.CASCADE,
        related_name='ankets'
    )
    Code_osvity = models.ForeignKey(
        Osvita,
        on_delete=models.CASCADE,
        related_name='ankets'
    )
    Code_Posadi = models.ForeignKey(
        Posada,
        on_delete=models.CASCADE,
        related_name='ankets'
    )
    Code_Dohodu = models.ForeignKey(
        Dohid,
        on_delete=models.CASCADE,
        related_name='ankets'
    )
    Code_bajanoi_sumi = models.ForeignKey(
        Bajana_suma_creditu,
        on_delete=models.CASCADE,
        related_name='ankets'
    )
    Kod_clienta = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='ankets'
    )

    
    class Meta:
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкети'