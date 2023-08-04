

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

    @staticmethod
    def blog_image(instance, filename):
        return f"Blog_Image/{instance.title}/{filename}"

    @staticmethod
    def services_photo(instance, filename):
        return f"Services_Image/{instance.title}/Photo/{filename}"

    @staticmethod
    def services_logo(instance, filename):
        return f"Services_Image/{instance.title}/Logo/{filename}"

    @staticmethod
    def services_property_photo(instance, filename):
        return f"Services_Image/{instance.services.title}/Service_Property/{filename}"

    @staticmethod
    def services_category_icon(instance, filename):
        return f"Services_Image/{instance.services.title}/Service_Category/{instance.name}/Icon/{filename}"

    @staticmethod
    def services_category_last_works(instance, filename):
        return f"Services_Image/{instance.services_category.services.title}/Service_Category/{instance.services_category.name}/Last_works/{instance.company_name}/{filename}"

    @staticmethod
    def services_package_icon(instance, filename):
        return f"Services_Image/{instance.package.services_category.services.title}/Service_Category/{instance.package.services_category.name}/{instance.package.package_name}/Package_Icon/{instance.property_name}/{filename}"
