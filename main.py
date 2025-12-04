import flet as ft

EARTH_GRAVITY = 9.8

GRAVITY = {
    "Sun": 274.0,
    "Mercury": 3.70,
    "Venus": 8.87,
    "Earth": 9.80,
    "Moon": 1.62,
    "Mars": 3.71,
    "Jupiter": 24.79,
    "Saturn": 10.44,
    "Uranus": 8.87,
    "Neptune": 11.15,
}


def main(page: ft.Page):
    page.title = "Solar System Weight Calculator"
    page.window.width= 1920
    page.window.height = 1080
    #page.window_full_screen = True
    page.window.center()
    page.window.maximized = True
    #page.window.frameless = True
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0

    weight_field = ft.TextField(
        value="0.00",
        text_align=ft.TextAlign.CENTER,
        width=250,
        height=60,
        bgcolor="#00000099",
        color="white",
        border_radius=10,
        border_color="white",
        border_width=2,
        on_change=lambda e: calculate_weight(),
    )

    # Create planet labels
    label_controls = {}
    for p in GRAVITY.keys():
        label_controls[p] = ft.Text(
            "0.00",
            size=32,
            color="yellow",
            weight=ft.FontWeight.BOLD,
        )

    # Absolute positioned planets (same as your NetBeans absolute layout)
    planets_positioned = ft.Stack(
        controls=[
            # Sun
            ft.Container(
                content=label_controls["Sun"],
                left=120, top=450, width=200, height=70
            ),
            ft.Container(content=label_controls["Mercury"],
                left=550, top=760, width=200, height=70
            ),
            ft.Container(content=label_controls["Moon"],
                left=930, top=350, width=200, height=70
            ),
            ft.Container(content=label_controls["Earth"],
                left=860, top=690, width=200, height=70
            ),
            ft.Container(content=label_controls["Mars"],
                left=980, top=800, width=200, height=70
            ),
            ft.Container(content=label_controls["Jupiter"],
                left=1185, top=600, width=200, height=70
            ),
            ft.Container(content=label_controls["Uranus"],
                left=1560, top=750, width=200, height=70
            ),
            ft.Container(content=label_controls["Saturn"],
                left=1350, top=270, width=200, height=70
            ),
            ft.Container(content=label_controls["Neptune"],
                left=1650, top=300, width=200, height=70
            ),
            ft.Container(content=label_controls["Venus"],
                left=700, top=210, width=200, height=70
            ),
        ],
        expand=True
    )

    # Background Image
    bg = ft.Image(
        src="solar_bg.jpg",
        fit=ft.ImageFit.FILL,
        width=float("inf"),
        height=float("inf")
    )

    # Stack background + labels
    full_layout = ft.Stack(
        controls=[bg, planets_positioned],
        expand=True,
    )

    # Bottom weight input
    bottom_panel = ft.Row(
        [
            ft.Text("Enter your weight (kg):", size=24, color="white"),
            weight_field,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
        height=60,
        #bgcolor="#00000088",
    )

    # Page Layout
    page.add(
        ft.Column(
            controls=[
                full_layout,
                bottom_panel,
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.END
        )
    )

    # Weight calculation function
    def calculate_weight():
        try:
            value = float(weight_field.value)
        except:
            value = 0

        for planet, gravity in GRAVITY.items():
            if planet == "Earth":
                result = value
            else:
                result = (value * gravity) / EARTH_GRAVITY

            label_controls[planet].value = f"{result:.2f}"

        page.update()


ft.app(target=main)
