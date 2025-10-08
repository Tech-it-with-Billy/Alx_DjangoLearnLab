from rest_framework import viewsets, permissions, filters
from .models import Post, Comment, Like, UnLike
from .serializers import PostSerializer, CommentSerializer, LikeSerializer, UnLikeSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

class UserPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = UserPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author__username']
    search_fields = ['content', 'author__username']
    ordering_fields = ['created_at', 'author__username']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = UserPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['post__id', 'author__username']
    search_fields = ['content', 'author__username']
    ordering_fields = ['created_at', 'author__username']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserFeedsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing user feeds.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = UserPagination

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all().order_by('-created_at')
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = UserPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UnLikeViewSet(viewsets.ModelViewSet):
    queryset = UnLike.objects.all().order_by('-created_at')
    serializer_class = UnLikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = UserPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)