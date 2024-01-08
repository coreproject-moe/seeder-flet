import flet as ft

class UploadView(ft.Text):
    def __init__(self, *args, **kwargs):
        super(UploadView,  self).__init__(*args, **kwargs)

        self.__create_view__()

    def __create_view__(self):
        self.value = "Upload Page"