from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=255, label="Tiêu đề")
    author = forms.CharField(max_length=255, label="Tác giả")
    published_date = forms.DateField(
        label="Ngày xuất bản",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    price = forms.FloatField(label="Giá")
    description = forms.CharField(widget=forms.Textarea, label="Mô tả")
    image_url = forms.URLField(label="URL Ảnh", required=False)  # ✅ Trường nhập URL ảnh
