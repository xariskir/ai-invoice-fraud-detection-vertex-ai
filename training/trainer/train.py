import argparse
import pandas as pd
import joblib
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report


def main(args):

    train_df = pd.read_csv(args.train_path)
    val_df = pd.read_csv(args.val_path)

    X_train = train_df.drop("fraud", axis=1)
    y_train = train_df["fraud"]

    X_val = val_df.drop("fraud", axis=1)
    y_val = val_df["fraud"]

    model = XGBClassifier(
        n_estimators=300,
        max_depth=6,
        learning_rate=0.05,
        scale_pos_weight=9,
        eval_metric="logloss"
    )

    pipeline = Pipeline([
        ("model", model)
    ])

    pipeline.fit(X_train, y_train)

    preds = pipeline.predict(X_val)

    print(classification_report(y_val, preds))

    joblib.dump(pipeline, f"{args.model_dir}/model.joblib")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--train_path", required=True)
    parser.add_argument("--val_path", required=True)
    parser.add_argument("--model_dir", required=True)

    args = parser.parse_args()

    main(args)
