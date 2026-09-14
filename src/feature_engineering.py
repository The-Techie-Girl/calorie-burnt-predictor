import pandas as pd


def bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal"

    elif bmi < 30:
        return "Overweight"

    return "Obese"


def age_group(age):

    if age < 25:
        return "Young"

    elif age < 40:
        return "Adult"

    return "Senior"


def workout_intensity(hr):

    if hr < 100:
        return "Low"

    elif hr < 130:
        return "Moderate"

    return "High"


def create_features(df):

    df = df.copy()

    df["Height_m"] = df["Height"] / 100

    df["BMI"] = (
        df["Weight"]
        /
        (df["Height_m"] ** 2)
    )

    df["BMI_Category"] = (
        df["BMI"]
        .apply(bmi_category)
    )

    df["Age_Group"] = (
        df["Age"]
        .apply(age_group)
    )

    df["Workout_Intensity"] = (
        df["Heart_Rate"]
        .apply(workout_intensity)
    )

    return df