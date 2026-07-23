import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn

if __name__ == "__main__":

    mlflow.set_experiment("Latihan Credit Scoring")
    
    with mlflow.start_run():
        df = pd.read_csv("namadataset_preprocessing/credit_scoring_clean.csv")
        X = df.drop("target", axis=1)
        y = df["target"]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = RandomForestClassifier(n_estimators=10, random_state=42)
        model.fit(X_train, y_train)
        
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, "model")
        print("Model trained and logged to MLflow")
