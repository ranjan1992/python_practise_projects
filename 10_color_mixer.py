print("☄️ COLOR MIXER ☄️")

color_mixes = {
    ("red", "blue"): "purple",
    ("red", "yellow"): "orange",
    ("blue", "yellow"): "green",
    ("blue", "green"): "teal",
    ("white", "red"): "pink",
    ("red", "green"): "brown"
}

while True:
    color1 = input("\nEnter first color: ").lower()
    color2 = input("Enter second color: ").lower()

    mix = None

    if (color1, color2) in color_mixes:
        mix = color_mixes[(color1, color2)]
    if (color2, color1) in color_mixes:
        mix = color_mixes[(color2, color1)]

      # todo: add 1 optimization

    if mix:
        print(f"When you mix {color1} and {color2}, you get {mix}")
    else:
        print("I don't know what those colors make when mixed.")

    if not input("\nMix more colors? (y/n)").lower().startswith("y"):
        print("Goodbye ! 👋")
        break
