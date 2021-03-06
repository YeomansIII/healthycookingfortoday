from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages
# from django.contrib.comments import Comment
from django.utils.translation import ugettext_lazy as _
from taggit.models import Tag
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import permissions
from blogger.models import Post, Author, Ingredient, RecipeStep, Recipe, Header
import datetime
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, AuthorSerializer


# builds the dictionary for secondary navigation
# by post title
def get_sidebar_data():
    promoted_posts = Post.objects.filter(
        published=True, promoted=True).order_by('-created_at')
    popular_posts = Post.popular_posts.filter(
        published=True).order_by('-publish_at')[:5]
    recent_posts = Post.objects.filter(
        published=True).order_by('-publish_at')[:5]
    archive = Post.objects.filter(
        published=True).datetimes('publish_at', 'month', order='DESC')
    tags = Tag.objects.all()
    authors = Author.objects.all()
    data = {
        'promoted_posts': promoted_posts,
        'popular_posts': popular_posts,
        'recent_posts': recent_posts,
        'archive': archive,
        'tags': tags,
        'authors': authors,
    }
    return data


def get_recipe_sidebar_data():
    recipes = Recipe.objects.filter(promoted=True).order_by('-created_at')
    ingredients = []
    steps = []
    for recipe in recipes:
        ing_mods = Ingredient.objects.order_by('id').filter(recipe=recipe)
        step_mods = RecipeStep.objects.order_by('id').filter(recipe=recipe)
        ingredients.append(ing_mods)
        steps.append(step_mods)
    recipe_zip = zip(recipes, ingredients, steps)
    promoted_recipes = recipe_zip
    # popular_recipes = Recipe.popular_posts.all().order_by('-created_at')[:5]
    recent_recipes = Recipe.objects.all().order_by('-created_at')[:5]
    archive = Recipe.objects.all().datetimes('created_at', 'month', order='DESC')
    tags = Tag.objects.all()
    authors = Author.objects.all()
    data = {
        'promoted_recipes': promoted_recipes,
        # 'popular_recipes': popular_recipes,
        'recent_recipes': recent_recipes,
        'archive': archive,
        'tags': tags,
        'authors': authors,
    }
    return data


# renders data onto list.html for the current theme
def render_on_list(request, data):

    return render_to_response('list.html', data,
                              context_instance=RequestContext(request)
                              )


def render_on_list_recipes(request, data):

    return render_to_response('list_recipes.html', data,
                              context_instance=RequestContext(request)
                              )


# redirects to the item a comment was made on
# when a user posts a comment.
# def comment_posted(request):
#
#     c = request.GET['c']
#     messages.add_message(request, messages.SUCCESS,
#                          _('Commented added successfully.'))
#     c = Comment.objects.get(pk=c)
#     return redirect(c.content_object)


# returns a list of posts onto the list template
def list(request, year=None, month=None, tag=None, author=None):

    sidebar_data = get_sidebar_data()

    data = {
        'posts': None,
        'section_title': _('Posts')
    }

    data.update(sidebar_data)

    # TODO: refactor this if if if if block
    # tag archive
    if tag:
        posts = Post.objects.filter(publish_at__lte=datetime.datetime.now(),
                                    published=True,
                                    tags__slug=tag)
        data['posts'] = posts
        data['section_title'] = _("Tag archive")
        return render_on_list(request, data)

    # author archive
    if author:
        fname, lname = author.split('-')
        posts = Post.objects.filter(publish_at__lte=datetime.datetime.now(),
                                    published=True,
                                    author__first_name=fname,
                                    author__last_name=lname
                                    ).order_by('-publish_at')
        data['posts'] = posts
        data['section_title'] = _("Author archive")
        return render_on_list(request, data)
    # all posts
    if not year:
        posts = Post.objects.filter(publish_at__lte=datetime.datetime.now(),
                                    published=True).order_by('-publish_at')
        data['enable_promoted'] = True
        data['posts'] = posts
        data['section_title'] = _("All Posts")
        return render_on_list(request, data)
    # yearly archive
    if not month:
        posts = Post.objects.filter(publish_at__lte=datetime.datetime.now(),
                                    published=True,
                                    created_at__year=year
                                    ).order_by('-publish_at')
        data['posts'] = posts
        data['section_title'] = _("Yearly Archive")
        return render_on_list(request, data)
    # monthly archive
    else:
        posts = Post.objects.filter(publish_at__lte=datetime.datetime.now(),
                                    published=True,
                                    created_at__year=year,
                                    created_at__month=month
                                    ).order_by('-publish_at')

        data['posts'] = posts
        data['section_title'] = _("Monthly Archive")
        return render_on_list(request, data)


# renders a single post
def view_post(request, slug):

    post = Post.objects.get(slug=slug)
    ingredients = []
    steps = []
    recipes = post.recipes.order_by('created_at').all()
    for recipe in recipes:
        ing_mods = Ingredient.objects.order_by('id').filter(recipe=recipe)
        step_mods = RecipeStep.objects.order_by('id').filter(recipe=recipe)
        ingredients.append(ing_mods)
        steps.append(step_mods)
    recipe_zip = zip(recipes, ingredients, steps)
    if not post.published:
        messages.add_message(request, messages.SUCCESS,
                             _('Post does not exist or is not published yet.'))
        redirect(reverse('all_archive'))

    sidebar_data = get_sidebar_data()
    data = {
        'post': post,
        'recipes': recipe_zip,
        'aprint': True,
    }
    data.update(sidebar_data)
    return render_to_response('view_post.html', data,
                              context_instance=RequestContext(request)
                              )


def list_recipes(request, year=None, month=None, tag=None, author=None):

    sidebar_data = get_recipe_sidebar_data()

    data = {
        'recipes': None,
        'section_title': _('Recipes')
    }

    data.update(sidebar_data)

    # TODO: refactor this if if if if block
    # tag archive
    if tag:
        recipes = Recipe.objects.filter(created_at__lte=datetime.datetime.now(),
                                        tags__slug=tag)
        ingredients = []
        for recipe in recipes:
            ing_mods = Ingredient.objects.order_by('id').filter(recipe=recipe)
            # step_mods = RecipeStep.objects.filter(recipe=recipe)
            ingredients.append(ing_mods)
            # steps.append(step_mods)
        recipe_zip = zip(recipes, ingredients)  # , steps)
        data['recipes'] = recipe_zip
        data['section_title'] = _("Tag archive")
        return render_on_list_recipes(request, data)

    # author archive
    if author:
        fname, lname = author.split('-')
        recipes = Recipe.objects.filter(created_at__lte=datetime.datetime.now(),
                                        author__first_name=fname,
                                        author__last_name=lname
                                        ).order_by('-created_at')
        ingredients = []
        for recipe in recipes:
            ing_mods = Ingredient.objects.filter(recipe=recipe)
            # step_mods = RecipeStep.objects.filter(recipe=recipe)
            ingredients.append(ing_mods)
            # steps.append(step_mods)
        recipe_zip = zip(recipes, ingredients)  # , steps)
        data['recipes'] = recipe_zip
        data['section_title'] = _("Author archive")
        return render_on_list_recipes(request, data)
    # all posts
    if not year:
        recipes = Recipe.objects.filter(
            created_at__lte=datetime.datetime.now()).order_by('-created_at')
        data['enable_promoted'] = True
        ingredients = []
        for recipe in recipes:
            ing_mods = Ingredient.objects.order_by('id').filter(recipe=recipe)
            # step_mods = RecipeStep.objects.filter(recipe=recipe)
            ingredients.append(ing_mods)
            # steps.append(step_mods)
        recipe_zip = zip(recipes, ingredients)  # , steps)
        data['recipes'] = recipe_zip
        data['section_title'] = _("All Recipes")
        return render_on_list_recipes(request, data)
    # yearly archive
    if not month:
        recipes = Recipe.objects.filter(created_at__lte=datetime.datetime.now(),
                                        created_at__year=year
                                        ).order_by('-created_at')
        ingredients = []
        for recipe in recipes:
            ing_mods = Ingredient.objects.order_by('id').filter(recipe=recipe)
            # step_mods = RecipeStep.objects.filter(recipe=recipe)
            ingredients.append(ing_mods)
            # steps.append(step_mods)
        recipe_zip = zip(recipes, ingredients)  # , steps)
        data['recipes'] = recipe_zip
        data['section_title'] = _("Yearly Archive")
        return render_on_list_recipes(request, data)
    # monthly archive
    else:
        recipes = Recipe.objects.filter(created_at__lte=datetime.datetime.now(),
                                        created_at__year=year,
                                        created_at__month=month
                                        ).order_by('-created_at')

        ingredients = []
        for recipe in recipes:
            ing_mods = Ingredient.objects.order_by('id').filter(recipe=recipe)
            # step_mods = RecipeStep.objects.filter(recipe=recipe)
            ingredients.append(ing_mods)
            # steps.append(step_mods)
        recipe_zip = zip(recipes, ingredients)  # , steps)
        data['recipes'] = recipe_zip
        data['section_title'] = _("Monthly Archive")
        return render_on_list_recipes(request, data)


# renders a single post
def view_recipe(request, slug):
    recipe = Recipe.objects.get(slug=slug)
    ingredients = Ingredient.objects.order_by('id').filter(recipe=recipe)
    steps = RecipeStep.objects.order_by('id').filter(recipe=recipe)

    sidebar_data = get_sidebar_data()
    data = {
        'recipe': recipe,
        'ingredients': ingredients,
        'steps': steps,
        'rprint': True,
    }
    data.update(sidebar_data)
    return render_to_response('view_recipe.html', data,
                              context_instance=RequestContext(request)
                              )


def view_latest(request):
    data = {}
    data['header'] = Header.objects.all().first()
    if Post.objects.count() > 0:
        data = {}
        try:
            post = Post.objects.filter(
                publish_at__lte=datetime.datetime.now(), published=True).order_by('-publish_at')[0]
            data['post'] = post
            ingredients = []
            steps = []
            recipes = post.recipes.order_by('created_at').all()
            for recipe in recipes:
                ing_mods = Ingredient.objects.order_by('id').filter(recipe=recipe)
                step_mods = RecipeStep.objects.order_by('id').filter(recipe=recipe)
                ingredients.append(ing_mods)
                steps.append(step_mods)
            recipe_zip = zip(recipes, ingredients, steps)
            data['recipes'] = recipe_zip
        except IndexError:
            pass
        data['aprint'] = True
    return render_to_response('index.html', data,
                              context_instance=RequestContext(request)
                              )

# Begin API Views


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'authors': reverse('authors-list', request=request),
        'posts': reverse('posts-list', request=request),
    })


class AuthorList(generics.ListAPIView):
    """
    API endpoint that represents a list of users.
    """
    model = Author
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveAPIView):
    """
    API endpoint that represents a single user.
    """
    model = Author
    serializer_class = AuthorSerializer


class PostList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of groups.
    """
    model = Post
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def filter_queryset(self, queryset):
        # this would make it so it only returned posts owned
        # by the user requesting them
        # queryset = queryset.filter(author=self.request.user)
        return super(generics.ListCreateAPIView,
                     self).filter_queryset(queryset)

    def pre_save(self, obj):
        obj.author = self.request.user


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single post.
    """
    model = Post
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def pre_save(self, obj):
        obj.author = self.request.user
