# Phân công nhiệm vụ nhóm

**Đề tài:** Xây dựng hệ thống cho thuê xe máy khu vực trung tâm Đà Nẵng
**Công nghệ:** Python (Django) – MySQL – mô hình MVC (MVT của Django)

## Bảng phân công

| Thành viên | App phụ trách | Nhánh làm việc | Nội dung chính |
|---|---|---|---|
| Trần Nam Phương (nhóm trưởng) | `config`, `core` | `feature/core-config` | Cấu hình chung, giao diện chung, duyệt Pull Request, deploy cloud |
| Hồ Ngọc Quỳnh Anh | `accounts`, `shops` | `feature/accounts-shops` | Đăng ký, đăng nhập, phân quyền, hồ sơ, đăng ký cửa hàng |
| Dương Lê Đức | `vehicles`, `reviews` | `feature/vehicles-reviews` | Quản lý xe và ảnh xe, tìm xe, đánh giá sau thuê |
| Bùi Ngọc Thịnh | `bookings` | `feature/bookings` | Đặt xe, kiểm tra trùng lịch, xác nhận đơn, thanh toán và cọc |
| Nguyễn Thị Bích Thư | `handovers`, `rescue` | `feature/handovers-rescue` | Biên bản giao/trả xe, yêu cầu cứu hộ |

## Quy ước làm việc

- Mỗi thành viên làm trên nhánh riêng, chỉ sửa trong thư mục app của mình.
- Hoàn thành thì push nhánh và tạo Pull Request vào `main`; nhóm trưởng duyệt và merge.
- Tên commit viết theo dạng `ten-app: viec da lam`.