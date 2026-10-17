from flask import Flask, render_template, request, session, redirect
import os
from PIL import Image
import numpy as np
from collections import Counter

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

UPLOAD_FOLDER = 'static/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER,exist_ok=True)

@app.route('/',methods=['GET','POST'])
def home():

    colors = session.get("colors",[])

    if request.method == 'POST':

        colors = []

        image = request.files['image']

        image_path = os.path.join(app.config['UPLOAD_FOLDER'],image.filename)

        image.save(image_path)

        img = Image.open(image_path)
        pixels = np.array(img)
        pixels = pixels.reshape(-1,3)

        color_counts = Counter(map(tuple, pixels))
        top_colors = color_counts.most_common(10)


        for color,count in top_colors:

            r,g,b = color

            r = int(r)
            g = int(g)
            b = int(b)

            hex_color = f"#{r:02x}{g:02x}{b:02x}"

            color_data = {
                "rgb": (r,g,b),
                "hex": hex_color,
                "count": count,
            }
            colors.append(color_data)

        session["colors"] = colors
        return redirect("/")

    return render_template("index.html",colors=colors)

if __name__ == '__main__':
    app.run(debug=True)