from rest_framework import serializers
from apps.settings.models import Setting


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'

    def to_representation(self, instance):
        return {
            "user": {
                "data": {
                    'displayName': instance.owner.username,
                    'email': instance.owner.email,
                    "photoURL": "assets/images/avatars/johndoe.png",
                    'settings': {
                        "layout": {
                            "style": instance.layout_style,
                            "config": {
                                "scroll": instance.layout_config_scroll,
                                "navbar": {
                                    "display":
                                    instance.layout_config_navbar_display,
                                    "folded":
                                    instance.layout_config_navbar_folded,
                                    "position":
                                    instance.layout_config_navbar_position,
                                },
                                "toolbar": {
                                    "display":
                                    instance.layout_config_toolbar_display,
                                    "style":
                                    instance.layout_config_toolbar_style,
                                    "position":
                                    instance.layout_config_toolbar_position,
                                },
                                "footer": {
                                    "display":
                                    instance.layout_config_footer_display,
                                    "style":
                                    instance.layout_config_footer_style,
                                    "position":
                                    instance.layout_config_footer_position,
                                }
                            }
                        },
                        "customScrollbars": instance.custom_scrollbars,
                        "theme": {
                            "main": instance.theme_main,
                            "navbar": instance.theme_navbar,
                            "toolbar": instance.theme_toolbar,
                            "footer": instance.theme_footer,
                        },
                        "shortcuts": []
                    },
                    "error": "",
                    "role": "admin",
                    "uuid": instance.owner.id,
                    "roles": ["admin"],
                    "partner_id": 1,
                }
            }
        }


class SettingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'

    # def to_representation(self, instance):
    #     return {
    #         'id': instance['id'],
    #         'username': instance['owner'],
    #         'email': instance['theme_footer'],
    #         'password': instance['theme_navbar']
    #     }
