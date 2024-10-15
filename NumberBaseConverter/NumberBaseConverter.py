"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import numpy as np

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...

#Backend

#Convert base binary to decimal

def convertBinaryDecimal():
    num=101010
    num_arr = list(map(int, str(num)))
    reverse_num = reversed(list(num_arr))
    count=0
    sum_num = 0
    for i in reverse_num:
        n= (2 * count) * i
        sum_num += n
        count+=1
    print(sum_num)

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
