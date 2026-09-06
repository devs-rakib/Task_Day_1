import json

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


LABELS = [
    "High Risk",
    "Medium Risk",
    "Standard / Low Risk"
]


def calculate_metrics(y_true, y_pred):

    accuracy = accuracy_score(
        y_true,
        y_pred
    )

    precision = precision_score(
        y_true,
        y_pred,
        labels=LABELS,
        average="macro",
        zero_division=0
    )

    recall = recall_score(
        y_true,
        y_pred,
        labels=LABELS,
        average="macro",
        zero_division=0
    )

    macro_f1 = f1_score(
        y_true,
        y_pred,
        labels=LABELS,
        average="macro",
        zero_division=0
    )

    matrix = confusion_matrix(
        y_true,
        y_pred,
        labels=LABELS
    )

    return {
        "accuracy": accuracy,
        "precision_macro": precision,
        "recall_macro": recall,
        "macro_f1": macro_f1,
        "confusion_matrix": matrix.tolist()
    }
