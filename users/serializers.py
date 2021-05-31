from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer
from .models import Profile, User


class UserDetailSerializer(UserDetailsSerializer):
    profile = Profile()

    class Meta(UserDetailsSerializer.Meta):
        model = User
        fields = UserDetailsSerializer.Meta.fields + ('profile',)
        read_only_fields = ('',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    # state = serializers.CharField(source="profile.state")
    # present_class = serializers.CharField(source="profile.present_class")
    # local_government = serializers.CharField(source="profile.local_government")
    # profile_picture = serializers.CharField(source="profile.profile_picture")
    user = UserSerializer()

    class Meta(UserDetailSerializer.Meta):
        model = Profile
        fields = ('dob', 'gender', 'school',
                  'state', 'present_class', 'local_government', 'profile_picture', 'user',)
        read_only_fields = ('email',)

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        state = profile_data.get('state')
        present_class = profile_data.get('present_class')
        local_government = profile_data.get('local_government')
        profile_picture = profile_data.get('profile_picture')
        dob = profile_data.get('dob')
        gender = profile_data.get('gender')
        school = profile_data.get('school')

        instance = super(UserSerializer).update(instance, validated_data)

        # get and update user profile
        profile = instance.profile
        if profile_data:
            profile.state = state
            profile.present_class = present_class
            profile.local_government = local_government
            profile.profile_picture = profile_picture
            profile.dob = dob
            profile.gender = gender
            profile.school = school
            profile.save()
        return instance
