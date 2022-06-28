from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # faqatgina ko'rish uchun ruxsat beriladi
        if request.method in permissions.SAFE_METHODS:
            return True
        # o'zgartirish ya'ni yozish uchun ruxsatnoma faqat post muallifiga ruxsat beriladi
        return obj.author == request.user
