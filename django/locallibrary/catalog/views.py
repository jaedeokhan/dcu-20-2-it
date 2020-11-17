from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# def index와 같이 함수형이면 => @login_required로 로그인해야 접근이 가능하게 설정해준다.
def index(request):
    "View function for home page of site"

    # Generate counts of some of main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Genre count
    num_genre = Genre.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()

    # The 'all' is implied by default
    num_authors = Author.objects.count()

    # Number of visits to this view, as counted in the session variables.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_genre' : num_genre,
        'num_instances_available' : num_instances_available,
        'num_authors' : num_authors,
        'num_visits' : num_visits,
    }

    # Render the HTML template indeox.html with the data in the context variable
    return render(request, 'index.html' , context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
        
class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class AuthorDetailView(generic.DetailView):
    model = Author

# On loan View => 자신이 빌린 책 보게, 자기 자신만
class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 2
    
    # 쿼리셋을 설정해주지 않으면 모두가 출력된다. => 
    # 필터링 처리해서 현재 대여중이고, 만기일을 Ordey by 출력
    def get_queryset(self):
        return BookInstance.objects.filter(
            borrower=self.request.user).filter(status__exact='o').order_by('due_back')
