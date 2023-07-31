

class Uploader:

    # Core App
    @staticmethod
    def collaborators_logo(instance, filename):
        return f"Collaborators_LOGO/{instance.name}/{filename}"

    @staticmethod
    def feedback_avatar(instance, filename):
        return f"FeedBack_avatars/{instance.fullname}/{filename}"

    @staticmethod
    def our_team_image(instance, filename):
        return f"Our_Team_Images/{instance.fullname}/{filename}"

    @staticmethod
    def slider_image(instance, filename):
        return f"Slider_Image/{instance.slider_header}/{filename}"




    # @staticmethod
    # def services_image(instance, filename):
    #     return f"Services_Image/{instance.name}/Logo/{filename}"

    # @staticmethod
    # def services_last_work_image(instance, filename):
    #     return f"Services_Image/{instance.service.name}/Works/{filename}"
