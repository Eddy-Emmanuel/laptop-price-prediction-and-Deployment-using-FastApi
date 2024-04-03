# Laptop Price Prediction

This project aims to predict the price of laptops based on various features such as company, laptop type, RAM, CPU, GPU, storage, operating system, and more. The prediction model is built using machine learning techniques, particularly the CatBoostRegressor algorithm.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/laptop-price-prediction.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

4. Access the FastAPI documentation and test the prediction endpoint by visiting `http://localhost:8080/docs` in your web browser.

## Usage

Once the FastAPI server is up and running, you can make POST requests to the `/get_prediction/` endpoint with the required parameters to obtain a laptop price prediction.

Example request body:

```json
{
  "company": "acer",
  "typename": "notebook",
  "ram": 8,
  "cpu_brand": "intel core i5",
  "touchscreen": "no",
  "ips": "yes",
  "hdd": 1000,
  "ssd": 256,
  "gpu_brand": "nvidia",
  "os": "windows",
  "weight": 2.5,
  "ppi": 150
}
```

Example response:

```json
{
  "Laptop Price": 1200.0
}
```

## Model Training

The machine learning model used for prediction is trained using the `model.py` script and saved as `model.pkl`. For training details and data preprocessing steps, refer to the `Laptop_price_prediction.ipynb` Jupyter Notebook.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to adjust the content as needed to better fit your project's specifics. Let me know if you need further assistance!
