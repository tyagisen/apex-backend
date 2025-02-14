from rest_framework import serializers

from enrollments.api.utils import is_enrolled, is_enrolled_active


class EnrolledSerializerMixin(serializers.ModelSerializer):
    is_enrolled = serializers.SerializerMethodField()
    is_enrolled_active = serializers.SerializerMethodField()

    # (
    #     "is_enrolled",
    #     "is_enrolled_active",
    # )

    def get_is_enrolled(self, obj):
        return is_enrolled(obj, self.context["request"].user)

    def get_is_enrolled_active(self, obj):
        """Return True if the user is enrolled and active.

        Args:
            obj (db object): Objects which can be enrolled into.

        Returns
            bool: True if the user is enrolled and active.

        """
        return is_enrolled_active(obj, self.context["request"].user)
