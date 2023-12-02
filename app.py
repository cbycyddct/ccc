from flask import Flask,request, url_for, redirect, render_template, jsonify
from dopamine.datasets.figure8 import Figure8Dataset, load_figure8_dataset
from dopamine.datasets.lorenz import LorenzAttractorDataset, load_lorenz_attractor_dataset
from dopamine.datasets.rossler import RosslerAttractorDataset, load_rossler_attractor_dataset
from dopamine.optimizer import Dopamine
from dopamine.models.rnn import RNNModel


import numpy as np

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template("index.html")

@app.route("/optimize", methods=["POST"])
def optimize():
    # Instantiate the Dopamine class and perform optimization
    dopamine_optimizer = Dopamine()
    # Perform optimization steps here using the Dopamine instance

    # Dummy response, you can return any information you want
    return jsonify({"message": "Optimization with Dopamine completed."})

@app.route("/rnn_model", methods=["POST"])
def rnn_model():
    try:
        model_type = request.form.get("model_type")

        if model_type == "rnn_model":
            # Dummy values for input_size, output_size, and hidden_dim
            input_size, output_size, hidden_dim = 10, 5, 20
            
            # Instantiate the RNNModel class
            rnn_model = RNNModel(input_size, output_size, hidden_dim)
            # Perform any additional model loading steps if needed

            # Dummy response, you can return any information you want
            return jsonify({"message": "RNN Model loaded successfully."})
        else:
            return jsonify({"error": "Invalid model type."})
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route("/load_dataset", methods=["POST"])
def load_dataset():
    try:
        dataset_type = request.form.get("dataset_type")

        if dataset_type == "figure8":
            # Dummy values for Figure8Dataset instantiation
            sequence_length = 50
            target_length = 1

            # Load the Figure8Dataset
            data = load_figure8_dataset()
            figure8_dataset = Figure8Dataset(data, sequence_length, target_length)

            # Dummy response, you can return any information you want
            return jsonify({"message": "Figure 8 Dataset loaded successfully."})

        elif dataset_type == "lorenz":
            # Dummy values for LorenzAttractorDataset instantiation
            sequence_length = 499
            target_length = 1

            # Load the LorenzAttractorDataset
            data = load_lorenz_attractor_dataset(data_length=500)
            lorenz_dataset = LorenzAttractorDataset(data, sequence_length, target_length)

            # Dummy response, you can return any information you want
            return jsonify({"message": "Lorenz Dataset loaded successfully."})
        
        elif dataset_type == "rossler":
            # Load the RosslerAttractorDataset
            sequence_length = 499
            target_length = 1
            data = load_rossler_attractor_dataset(data_length=500)
            rossler_dataset = RosslerAttractorDataset(data, sequence_length, target_length)

            # Dummy response, you can return any information you want
            return jsonify({"message": "Rossler Dataset loaded successfully."})

        else:
            return jsonify({"error": "Invalid dataset type."})
    except Exception as e:
        return jsonify({"error": str(e)})



app.run(debug=True)
