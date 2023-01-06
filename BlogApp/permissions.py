from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    # custom 된 permission >> 해당 게시글 작성자만 수정할 수 있게끔 

    def has_object_permission(self, request, view, obj):
        # R >> 모든 요청 가능 >> GET, HEAD, OPTIONS request에 대해 허용
        if request.method in permissions.SAFE_METHODS:
            # SAFE_METHODS >> DB에 영향이 없을 HTTP 요청 GET, OPTIONS, HEAD를 의미
            return True

        # U와 D는(그 이외 http 요청) Post의 owner만 가능하게끔
        return obj.owner == request.user