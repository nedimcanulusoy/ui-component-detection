# UI Component Detection

This is an open-source prototype for detecting UI components, developed for the startup company in Sweden I contributed to. You can use this API to predict UI components in your own images.

--- 

## About

YoloV5 via Ultralytics is used for the model architecture. 
The model is trained on the [RICO dataset](https://interactionmining.org/rico).
It is connected to a [Flask app](predict_api.py) that can be used to make predictions on images through a simple REST API.
Detailed information about the model can be found in the [notebook](notebooks/ready-to-run-rico-ui-detection.ipynb).

_**Note: The model is NOT tuned for the best performance. It is just a prototype.**_

---

## Requirements

- Python 3.x
- Flask
- Pillow
- Ultralytics

---

## Installation

1. Clone the repository

```
git clone https://github.com/nedimcanulusoy/ui-component-detection.git
```

2. Create a virtual environment and activate it

```
python3 -m venv venv
```

``` 
source venv/bin/activate
```

3. Install the requirements

```
pip install -r requirements.txt
```

---

## Usage

1. Start the Flask app: python predict_api.py
``` 
python3 predict_api.py
```
2. Make a POST request to the /api/predict endpoint with an image file in the image parameter.
3. The API will return a JSON response with the detected objects in the image.

---

## Example

```
curl -X POST -F image=@/path/to/your/image http://localhost:xxxx/api/predict
```

---

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## Disclaimer

This project is not affiliated with the main project of the company whose projects I have contributed to. It is a prototype that I have developed as an additional tool alongside the given task.

---