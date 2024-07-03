## Giới thiệu

**_Project này sử dụng Retrieval Augmented Generation (RAG) để thực hiện hỏi đáp tài liệu PDF. Mục tiêu của project là tạo ra một hệ thống có thể xử lý các câu hỏi dựa trên nội dung của các tệp PDF được tải lên, sử dụng mô hình ngôn ngữ lớn (LLM) và Vector Database._**

# I.Cài đặt

## 1.Clone repository

Trước tiên, hãy clone repository này về máy tính của bạn:

## 2.Cài đặt các gói thư viện cần thiết

Sử dụng pip để cài đặt các gói thư viện được liệt kê trong tệp **\`requirements.txt\`**:

`pip install -r requirements.txt`

# II.Chạy project

## 1.Chạy với Streamlit

Bạn có thể chạy project bằng Streamlit để có một giao diện web đơn giản cho việc tải lên tệp PDF và đặt câu hỏi.

`streamlit run src/streamlit_app.py`

## 2.Sử dụng Chainlit cho giao diện chat

Nếu muốn sử dụng giao diện chat được xây dựng bằng Chainlit, hãy chạy lệnh sau:

`python src/main.py`

# III.Sử dụng

## 1.Tải file PDF lên

Sau khi chạy Streamlit, truy cập vào địa chỉ hiển thị trên terminal và tải lên một tệp PDF.

## 2.Đặt câu hỏi

Sau khi tệp PDF được xử lý, bạn có thể đặt câu hỏi liên quan đến nội dung của tài liệu và nhận được câu trả lời từ hệ thống.

# IV.Đóng góp

Nếu bạn muốn đóng góp cho project này, vui lòng tạo pull request hoặc mở issue mới để chúng tôi có thể xem xét và hợp tác phát triển.

