import flet as ft
from hurry.filesize import size
from flet_core.file_picker import FilePickerFile


class UploadView(ft.Column):
    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.page = page
        # file picker
        self.file_picker = ft.FilePicker(on_result=self.__pick_files_result)
        page.overlay.append(self.file_picker)
        page.update()
        # refs
        self.total_files_ref = ft.Ref[ft.Text]()
        self.total_size_ref = ft.Ref[ft.Text]()
        self.data_table_ref = ft.Ref[ft.DataTable]()
        self.progress_bar_ref = ft.Ref[ft.ProgressBar]()
        self.search_bar_ref = ft.Ref[ft.TextField]()

        # files
        self.uploaded_files: list[FilePickerFile] = []

        self.__create_view__()

    def __pick_files_result(self, e: ft.FilePickerResultEvent):
        # Handle enpty files
        if e.files is None:
            return

        self.search_bar_ref.current.disabled = False
        self.progress_bar_ref.current.value = None

        files = len(e.files)
        total_size = sum(file.size for file in e.files)

        self.total_files_ref.current.value = f"{files} files"
        self.total_size_ref.current.value = size(total_size)

        self.uploaded_files.extend(e.files)
        self.construct_data_table(e.files)

    def construct_data_table(self, files: list[FilePickerFile]):
        self.data_table_ref.current.rows.clear()

        if not len(files) == 0:
            for file in files:
                self.data_table_ref.current.rows.append(
                    ft.DataRow(
                        [
                            ft.DataCell(ft.Text(value=file.name)),
                            ft.DataCell(ft.Text(size(file.size))),
                        ],
                        data=file.name,
                    )
                )
        self.page.update()

    def __create_upload_status__(self):
        return ft.Column(
            controls=[
                ft.ProgressBar(
                    ref=self.progress_bar_ref,
                    height=10,
                    color=ft.colors.BLUE_ACCENT,
                    bgcolor=ft.colors.TERTIARY_CONTAINER,
                    value=0,
                ),
                ft.Column(
                    controls=[
                        ft.Text(
                            ref=self.total_size_ref,
                            value="0 B",
                            font_family="Kokoro-Bold",
                        ),
                        ft.Text(ref=self.total_files_ref, value="0 files"),
                    ],
                    spacing=0,
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
                            ft.Text(
                                value="Browse files",
                                size=17,
                                font_family="Kokoro-Medium",
                            ),
                            ft.Divider(
                                color=ft.colors.with_opacity(0.25, "white"), height=10
                            ),
                            ft.Text(value="Upload", size=13, opacity=0.75),
                        ],
                        spacing=0,
                        alignment=ft.MainAxisAlignment.CENTER,
                        width=100,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            on_click=lambda _: self.file_picker.pick_files(
                allow_multiple=True,
                allowed_extensions=[
                    "mp4",
                    "mkv",
                ],
            ),
        )

    def _handle_serach_event_(self, event: ft.ControlEvent):
        if event.data == "":
            searched_list = self.uploaded_files
        else:
            searched_list: list[FilePickerFile] = []

            for item in self.uploaded_files:
                if event.data.lower() in item.name.lower():
                    searched_list.append(item)

        self.construct_data_table(searched_list)

    def __create_data_table__(self):
        return ft.Container(
            content=ft.DataTable(
                ref=self.data_table_ref,
                sort_column_index=0,
                sort_ascending=True,
                heading_row_color=ft.colors.SECONDARY,
                show_checkbox_column=True,
                columns=[
                    ft.DataColumn(ft.Text("File Name")),
                    ft.DataColumn(
                        ft.Text("File Size"),
                        numeric=True,
                    ),
                ],
            ),
        )

    def __create_view__(self):
        self.expand = 1
        self.scroll = ft.ScrollMode.ALWAYS
        self.controls = [
            ft.Container(
                content=ft.Row(
                    controls=[
                        self.__create_upload_status__(),
                        self.__create_upload_area__(),
                    ],
                    spacing=100,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                padding=ft.padding.symmetric(horizontal=100, vertical=25),
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Divider(),
                        ft.Row(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.TextField(
                                            label="Search",
                                            ref=self.search_bar_ref,
                                            disabled=True,
                                            filled=True,
                                            bgcolor=ft.colors.TERTIARY_CONTAINER,
                                            label_style=ft.TextStyle(
                                                size=12,
                                            ),
                                            height=40,
                                            content_padding=ft.padding.symmetric(
                                                horizontal=20, vertical=5
                                            ),
                                            text_size=13,
                                            prefix_icon=ft.icons.SEARCH,
                                            border_radius=10,
                                            on_change=self._handle_serach_event_,
                                        ),
                                        ft.ElevatedButton(
                                            text="New folder",
                                            bgcolor=ft.colors.TRANSPARENT,
                                            style=ft.ButtonStyle(
                                                shape={
                                                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(
                                                        radius=10
                                                    )
                                                },
                                            ),
                                            height=40,
                                            icon=ft.icons.ADD,
                                            icon_color=ft.colors.BLUE_200,
                                        ),
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.ElevatedButton(
                                            text="Rename",
                                            bgcolor=ft.colors.TRANSPARENT,
                                            style=ft.ButtonStyle(
                                                shape={
                                                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(
                                                        radius=10
                                                    )
                                                },
                                            ),
                                            height=40,
                                            icon=ft.icons.EDIT,
                                            icon_color=ft.colors.BLUE_200,
                                        ),
                                        ft.ElevatedButton(
                                            text="Edit Details",
                                            bgcolor=ft.colors.TRANSPARENT,
                                            style=ft.ButtonStyle(
                                                shape={
                                                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(
                                                        radius=10
                                                    )
                                                },
                                            ),
                                            height=40,
                                            icon=ft.icons.EDIT,
                                            icon_color=ft.colors.BLUE_200,
                                        ),
                                        ft.ElevatedButton(
                                            text="Delete",
                                            bgcolor=ft.colors.TRANSPARENT,
                                            style=ft.ButtonStyle(
                                                shape={
                                                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(
                                                        radius=10
                                                    )
                                                },
                                            ),
                                            height=40,
                                            icon=ft.icons.DELETE,
                                            icon_color=ft.colors.BLUE_200,
                                        ),
                                    ]
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                    ]
                ),
                padding=ft.padding.symmetric(horizontal=50),
            ),
            ft.Container(
                content=self.__create_data_table__(),
                padding=ft.padding.symmetric(horizontal=50, vertical=10),
            ),
        ]
