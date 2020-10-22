from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instance

# Create your models here.
# 장르모델
class Genre(models.Model):
    # help_text : form widget 용 - 필드 입력 도움말
    name = models.CharField(max_length=200, help_text="책 유형을 입력해주세요.") 

    # 만약, 이름에 정렬 순위를 주고 싶다면?
    # class Meta:
    #    ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    # Foreign Key used because book can only have one author,
    # but authors can have mulptiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text="책 요약을 입력해주세요.")
    isbn = models.CharField('ISBN', max_length=13, help_text="13 Character <a href='https://www.isbn-international.org/content/what-isbn'>ISBN number</a>")

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above. 
    genre = models.ManyToManyField(Genre, help_text="책의 유형을 선택하세요.")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description = 'Genre'
    
class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="도서관에서 책에 존재하는 기본키")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length = 1,
        choices = LOAN_STATUS,
        blank = True,
        default = 'm',
        help_text = 'Book availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

# FK 로 만들기
class Language(models.Model):
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name