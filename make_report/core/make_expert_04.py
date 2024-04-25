
from flask import json
import requests
import pdfkit
import matplotlib.pyplot as plt # type: ignore
import mpld3 # type: ignore
import numpy as np # type: ignore
from util.exception_handler import exception_handler
from datetime import date


@exception_handler
def make_expert_04(base_url, options, path):
    data = {
        "header": "expert_04",
        "footer_left": date.today().strftime("%Y.%m.%d")
    }
    
    # Generate some sample data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Plot the data
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph Title')

    # Read the data from expert_04.json
    with open('expert_04.json', 'r') as file:
        data = json.load(file)

    # Extract x and y values from the data
    x = data['x-axis']
    y = data['y-axis']
    z = data['z-axis']

    # Vẽ 3 đồ thị 2D, mỗi đồ thị chỉ chứa 1 trục
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))

    # Đồ thị 2D - Chỉ chứa trục x
    ax1.plot(x)
    ax1.set_title('Đồ thị 2D - Chỉ chứa trục x')
    ax1.set_xlabel('x-axis')
    ax1.grid(True)

    # Đồ thị 2D - Chỉ chứa trục y
    ax2.plot(y)
    ax2.set_title('Đồ thị 2D - Chỉ chứa trục y')
    ax2.set_xlabel('y-axis')
    ax2.grid(True)

    # Đồ thị 2D - Chỉ chứa trục z
    ax3.plot(z)
    ax3.set_title('Đồ thị 2D - Chỉ chứa trục z')
    ax3.set_xlabel('z-axis')
    ax3.grid(True)

    # Điều chỉnh khoảng cách giữa các đồ thị
    plt.subplots_adjust(hspace=0.5)

    plt.show()
    
    html_fig = mpld3.fig_to_html(fig)

# Lưu HTML vào một file
    with open('graph.html', 'w') as f:
        f.write(html_fig)

    _ = requests.post(f"{base_url}submit_data", json=data)

    base_name = "expert_04"
    pdfkit.from_url(f"{base_url}{base_name}", f"{path}{base_name}.pdf",
                    options=options)


if __name__ == "__main__":
    print("This module is not intended to be run directly.")
