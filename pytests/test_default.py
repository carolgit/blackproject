import pytest
from django.contrib.auth.models import User
from about.models import Post

from django.urls import reverse
######################
# DEFAULTS
######################
def create_user():
  User.objects.create_user('john', 'john@doe.com', 'johnpassword')
  return User.objects.all()[:1].get()

def create_post(user):
  post = Post(author=user, title='Hello Word', text='dldkjbafas lkfsd falhdds adf a')
  post.save()
  return post 
######################
# END DEFAULTS
######################

# TESTANDO CRIAR USUARIO
@pytest.mark.django_db
def test_user_create():
  create_user()
  assert User.objects.count() == 1

# TESTANDO CRIAR POST
@pytest.mark.django_db
def test_post_create():
  user = create_user()
  create_post(user)
  assert Post.objects.count() == 1

# AO TENTAR ACESSAR SEM INFORMAR PARAMETRO OBRIGATORIO DA URL OU QUANDO O GET TEM RETORNO 404
@pytest.mark.django_db 
def test_post_404(client):
   url = reverse('post_content')
   response = client.get(url)
   assert response.status_code == 404

# AO TENTAR ACESSAR PAGINA PRIVADA SEM AUTENTICAR DEVE SER REDIRECIONADO 302 PARA TELA DE LOGIN
@pytest.mark.django_db 
def test_post_unauthorized(client):
   url = reverse('post_private')
   response = client.get(url)
   assert response.status_code == 302