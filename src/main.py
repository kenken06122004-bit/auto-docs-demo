# ================================
# File: src/main.py
# Mã Python mẫu cho phần CI/CD
# ================================

def xin_chao(ten: str) -> str:
    """
    Hàm chào hỏi đơn giản dùng để minh họa.

    Tham số:
        ten (str): Tên người cần chào.

    Trả về:
        str: Chuỗi chào.
    """
    return f"Xin chào {ten}!"

# Demo chạy hàm
if __name__ == "__main__":
    print(xin_chao("Nam"))