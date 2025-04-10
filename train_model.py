import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import pickle

# Đọc dữ liệu
df = pd.read_csv("comment_data.csv")

# Chia dữ liệu thành tập huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(
    df["content"], df["label"], test_size=0.2, random_state=42
)

# Tạo pipeline: TfidfVectorizer + LogisticRegression
model = make_pipeline(
    TfidfVectorizer(),
    LogisticRegression()
)

# Huấn luyện mô hình
model.fit(X_train, y_train)

# Đánh giá mô hình
accuracy = model.score(X_test, y_test)
print(f"Độ chính xác trên tập kiểm tra: {accuracy * 100:.2f}%")

# Lưu mô hình
with open("sentiment_model.pkl", "wb") as f:
    pickle.dump(model, f)
print("Mô hình đã được lưu vào sentiment_model.pkl")