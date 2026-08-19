import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report



df = pd.read_csv("heart_disease.csv")


X = df.drop("Heart Disease Status", axis=1)
y = df["Heart Disease Status"]



categorical_columns = X.select_dtypes(include=["object"]).columns.tolist()
numerical_columns = X.select_dtypes(exclude=["object"]).columns.tolist()



numerical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median"))
])



categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])



preprocessor = ColumnTransformer([
    ("num", numerical_pipeline, numerical_columns),
    ("cat", categorical_pipeline, categorical_columns)
])


model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight={"No": 1, "Yes": 4}
)

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", model)
])



X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)



pipeline.fit(X_train, y_train)


y_pred = pipeline.predict(X_test)



accuracy = accuracy_score(y_test, y_pred)

print("\nModel Training Completed!")
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))



joblib.dump(pipeline, "heart_disease_model.pkl")

print("\nModel saved as: heart_disease_model.pkl")
