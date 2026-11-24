import pandas as pd

def 정제(df):
    print("시작", len(df))
    df = df.dropna(subset=["점수"]).copy()
    print("빈 칸 제거", len(df))
    df = df.drop_duplicates()
    print("중복 제거", len(df))
    df["반"] = df["반"].str.strip()
    df["과목"] = df["과목"].str.strip()
    df = df[(df["점수"] >= 0) & (df["점수"] <= 100)]
    print("범위 밖 제거", len(df))
    return df

def 반별평균(df):
    return df.groupby("반")["점수"].mean()
