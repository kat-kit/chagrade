from rest_framework import permissions


class ChagradeAuthCheckMixin(object):

    def extra_permission_check(self, request):
        return True

    def has_permission(self, request, view):
        """Must be an authenticated user, and pass extra_permission_check (True by default)"""
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        else:
            return request.user.is_authenticated and self.extra_permission_check(request)


class UserPermissionCheck(ChagradeAuthCheckMixin, permissions.BasePermission):
    """Only allow authenticated users to make get requests"""
    message = 'You must be logged in to access Users.'

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS


class StudentPermissionCheck(ChagradeAuthCheckMixin, permissions.BasePermission):
    """Only allow authenticated users to make get requests, and
     allow users who match the student and teacher to make changes."""
    message = 'You must be logged in to access Students, or an instructor to make modifications to Students'

    def extra_permission_check(self, request):
        return request.user.instructor

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user == obj.user or request.user == obj.klass.instructor.user


class KlassPermissionCheck(ChagradeAuthCheckMixin, permissions.BasePermission):
    """Only allow authenticated users to make get requests, only
     allow instructors, and only allow klass instructors (creators) to modify"""
    message = 'You must be logged in to access Classes, or an instructor to make modifications to Classes'

    def extra_permission_check(self, request):
        return request.user.instructor

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if not request.user.instructor:
                return False
            else:
                return request.user.instructor == obj.instructor


class DefinitionPermissionCheck(ChagradeAuthCheckMixin, permissions.BasePermission):
    """Only allow authenticated users to make get requests, only
     allow instructors, and only allow klass instructors (creators) to modify"""
    message = 'You must be logged in to access Definitions, or an instructor to make modifications to Definitions'

    def extra_permission_check(self, request):
        return request.user.instructor

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if not request.user.instructor:
                return False
            else:
                return request.user.instructor == obj.klass.instructor


class CriteriaPermissionCheck(ChagradeAuthCheckMixin, permissions.BasePermission):
    """Only allow authenticated users to make get requests, only
     allow instructors, and only allow klass instructors (creators) to modify"""
    message = 'You must be logged in to access Criterias, or an instructor to make modifications to Criterias'

    def extra_permission_check(self, request):
        return request.user.instructor

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if not request.user.instructor:
                return False
            else:
                return request.user.instructor == obj.definition.klass.instructor


class QuestionPermissionCheck(ChagradeAuthCheckMixin, permissions.BasePermission):
    """Only allow authenticated users to make get requests, only
     allow instructors, and only allow klass instructors (creators) to modify"""
    message = 'You must be logged in to access Questions, or an instructor to make modifications to Questions'

    def extra_permission_check(self, request):
        return request.user.instructor

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if not request.user.instructor:
                return False
            else:
                return request.user.instructor == obj.definition.klass.instructor


class SubmissionPermissionCheck(ChagradeAuthCheckMixin, permissions.BasePermission):
    """Only allow authenticated users to make get requests, only
     allow the submission creator to modify. Anyone that's authenticated in a class can make a submission?"""
    message = 'You must be logged in to access Submissions'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user == obj.creator.user


class GradePermissionCheck(ChagradeAuthCheckMixin, permissions.BasePermission):
    """Only allow authenticated users to make get requests, only
     allow the submission creator to modify. Anyone that's authenticated in a class can make a submission?"""
    message = 'You must be logged in to access Grades, or an instructor to make modifications to Grades'

    def extra_permission_check(self, request):
        return request.user.instructor

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user == obj.evaluator.user


class TeamPermissionCheck(ChagradeAuthCheckMixin, permissions.BasePermission):
    """Only allow authenticated users to make get requests, only
     allow the submission creator to modify. Anyone that's authenticated in a class can make a submission?"""
    message = 'You must be logged in to access Teams, or an instructor to make modifications to Teams'

    def extra_permission_check(self, request):
        return request.user.instructor

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.instructor:
            return request.user.instructor == obj.klass.instructor
        else:
            return False
