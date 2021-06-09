import pytest
from django.contrib.auth.models import User
from about.models import Post

from django.urls import reverse

@pytest.mark.django_db
def test_user_create():
  User.objects.create_user('john', 'john@doe.com', 'johnpassword')
  assert User.objects.count() == 1

@pytest.mark.django_db
def test_post_create():
  User.objects.create_user('john', 'john@doe.com', 'johnpassword')
  user = User.objects.all()[:1].get()
  post = Post(author=user, title='Hello Word', text='dldkjbafas lkfsd falhdds adf a')
  post.save()
  assert Post.objects.count() == 1

@pytest.mark.django_db 
def test_view(client):
   url = reverse('post_content')
   response = client.get(url+'/1')
   assert response.status_code == 404

# @pytest.mark.django_db
# def test_unauthorized(client):
#    url = reverse('adm-main')
#    response = client.get(url)
#    assert response.status_code == 401

# @pytest.mark.django_db
# def test_superuser_view(admin_client):
#    url = reverse('superuser-url')
#    response = admin_client.get(url)
#    assert response.status_code == 200

# @pytest.mark.django_db
# def test_user_detail(client, django_user_model):
#    user = django_user_model.objects.create(
#        username='someone', password='password'
#    )
#    url = reverse('user-detail-view', kwargs={'pk': user.pk})
#    response = client.get(url)
#    assert response.status_code == 200
#    assert 'someone' in response.content

# @pytest.mark.django_db
# @pytest.mark.parametrize([
#    ('gr', 'Yasou'),
#    ('de', 'Guten tag'),
#    ('fr', 'Bonjour')
# ])
# def test_languages(language_code, text, client):
#    url = reverse('say-hello-url')
#    response = client.get(
#        url, data={'language_code': language_code}
#    )
#    assert response.status_code == 200
#    assert text == response.content