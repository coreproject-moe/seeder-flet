import flet as ft

class UploadView(ft.Column):
    def __init__(self, page: ft.Page, *args, **kwargs):
        super(UploadView,  self).__init__(*args, **kwargs)

        self.page = page
        # file picker
        self.file_picker = ft.FilePicker(on_result=self.__pick_files_result)
        page.overlay.append(self.file_picker)
        page.update()
        # refs
        self.total_files_ref = ft.Ref[ft.Text]()
        self.total_size_ref = ft.Ref[ft.Text]()

        self.__create_view__()

    def __pick_files_result(self, e: ft.FilePickerResultEvent):
        total_files = len(e.files)
        total_size = sum(file.size for file in e.files)

        self.total_files_ref.current.value = f"{total_files} files"
        self.total_size_ref.current.value = f"{total_size} B"
        self.page.update()

    def __create_upload_status__(self):
        return ft.Column(
            controls=[
                ft.ProgressBar(
                    height=10,
                    color=ft.colors.BLUE_ACCENT,
                    bgcolor=ft.colors.TERTIARY_CONTAINER,
                    value=0.5,
                ),
                ft.Column(
                    controls=[
                        ft.Text(ref=self.total_size_ref, value="0 B", font_family="Kokoro-Bold"),
                        ft.Text(ref=self.total_files_ref, value="0 files")
                    ],
                    spacing=0
                ),
            ],
            expand=1,
            spacing=30,
        )

    def __create_upload_area__(self):
        return ft.Container(
            bgcolor=ft.colors.TERTIARY_CONTAINER,
            height=100,
            border_radius=10,
            width=max,
            padding=ft.padding.symmetric(horizontal=50),
            content=ft.Row(
                controls=[
                    ft.Image(
                        src="icons/upload.png",
                        opacity=0.5,
                        width=100,
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(value="Browse files", size=17, font_family="Kokoro-Medium"),
                            ft.Divider(color=ft.colors.with_opacity(0.25, "white"), height=10),
                            ft.Text(value="Upload", size=13, opacity=0.75),
                        ],
                        spacing=0,
                        alignment=ft.MainAxisAlignment.CENTER,
                        width=100
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            on_click=lambda _: self.file_picker.pick_files(allow_multiple=True),
        )

    def __create_view__(self):
        self.controls = [
            ft.Container(
                content=ft.Row(
                    controls=[
                        self.__create_upload_status__(),
                        self.__create_upload_area__()
                    ],
                    spacing=100,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                padding=ft.padding.symmetric(horizontal=100, vertical=25),
            )
        ]