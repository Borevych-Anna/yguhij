from PIL import Image, ImageDraw


def create_image(name):
    image = Image.new("RGB", (400, 400), "white")
    draw = ImageDraw.Draw(image)

    draw.text((30, 100), f"Hello, {name}!", fill="black")

    image.save("output/profile.png")
    print("Зображення збереженно")