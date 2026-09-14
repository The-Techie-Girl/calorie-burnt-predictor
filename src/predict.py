import pandas as pd

from src.feature_engineering import create_features


def prepare_input(
    user_input,
    feature_list
):

    df = pd.DataFrame(
        [user_input]
    )

    df = create_features(df)

    df = pd.get_dummies(
        df,
        drop_first=True
    )

    for col in feature_list:

        if col not in df.columns:
            df[col] = 0

    df = df[feature_list]

    return df