# Phân công nhiệm vụ nhóm

**Đề tài:** Xây dựng hệ thống cho thuê xe máy khu vực trung tâm Đà Nẵng
**Công nghệ:** C# (Windows Forms, .NET 8) - MySQL - mô hình 3 lớp (GUI - BLL - DAL)

## Bảng phân công

| Thành viên | Module phụ trách | Nhánh làm việc | Nội dung chính |
|---|---|---|---|
| Trần Nam Phương (nhóm trưởng) | Core, MainForm, kết nối DB | `feature/core-config` | Khởi tạo solution, lớp kết nối MySQL, form chính (menu), file schema.sql, duyệt Pull Request, triển khai cloud |
| Hồ Ngọc Quỳnh Anh | Accounts, Shops | `feature/accounts-shops` | Đăng ký, đăng nhập, phân quyền, hồ sơ, đăng ký cửa hàng |
| Dương Lê Đức | Vehicles, Reviews | `feature/vehicles-reviews` | Quản lý xe và ảnh xe, tìm xe, đánh giá sau thuê |
| Bùi Ngọc Thịnh | Bookings | `feature/bookings` | Đặt xe, kiểm tra trùng lịch, xác nhận đơn, thanh toán và cọc |
| Nguyễn Thị Bích Thư | Handovers, Rescue | `feature/handovers-rescue` | Biên bản giao/trả xe, yêu cầu cứu hộ |

## Thư mục phụ trách trong solution

| Thành viên | GUI | BLL / DAL / DTO |
|---|---|---|
| Phương | `GUI/Main`, `GUI/Common` | `DAL/DbHelper`, `database/` |
| Quỳnh Anh | `GUI/Accounts`, `GUI/Shops` | `*Account*`, `*Shop*` |
| Đức | `GUI/Vehicles`, `GUI/Reviews` | `*Vehicle*`, `*Review*` |
| Thịnh | `GUI/Bookings` | `*Booking*`, `*Payment*` |
| Bích Thư | `GUI/Handovers`, `GUI/Rescue` | `*Handover*`, `*Rescue*` |

## Quy ước làm việc

1. Mỗi người làm trên nhánh riêng của mình, không commit trực tiếp vào `main`.
2. Commit nhỏ, thường xuyên, message rõ ràng (ví dụ: `Thêm form đăng nhập`).
3. Mỗi người tự push và tự tạo Pull Request, nhóm trưởng duyệt và merge.
4. Chỉ sửa file trong module của mình. Cần sửa file chung thì báo nhóm trưởng.
5. Không đưa mật khẩu, chuỗi kết nối DB lên GitHub (dùng `App.config`, đã ghi trong `.gitignore`).
