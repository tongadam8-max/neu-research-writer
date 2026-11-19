# BỘ LỌC KIỂM ĐỊNH CHẤT LƯỢNG TRƯỚC KHI XUẤT BẢN THẢO (10-POINT QA GATE)

AI tự động chạy toàn bộ 10 bước kiểm tra dưới đây trước khi trả bản thảo cho thành viên. Nhóm trưởng và thành viên tổng biên tập dùng chính danh sách này để duyệt bài trước khi ghép file Word nộp Khoa.

---

## 1. Kiểm định Tính nhất quán & Đồng bộ nhóm
- [ ] **Khóa biến số & ký hiệu:** Toàn bộ tên biến, mã biến quan sát, tên viết tắt và mã giả thuyết (`H1`, `H2`, `H3`...) khớp 100% với `templates/project-context.md`.
- [ ] **Khớp Outline báo cáo & Ma trận nhất quán:** Tên chương, cấp tiểu mục khớp 100% với Outline mới tại Mục 3 của `templates/project-context.md` và phục vụ đúng mục tiêu, câu hỏi nghiên cứu.
- [ ] **Khớp mạch liên chương:** Nếu viết từ Chương 2 trở đi, đã kiểm tra khớp số liệu/phát hiện với `templates/chapter-handoff.md` (không mâu thuẫn giữa các thành viên).

## 2. Kiểm định Chống bịa nguồn & Số liệu (Zero-Hallucination)
- [ ] **Zero Number Drift:** Mọi con số (cỡ mẫu $N$, tần số, tỷ lệ %, hệ số $\beta$, $t$, $p$, VIF, $R^2$, $f^2$, Alpha, CR, AVE, HTMT) trong đoạn văn khớp 100% với bảng số liệu ngay cạnh. Tổng các tỷ lệ thành phần bằng đúng $100\%$.
- [ ] **Chống bịa tài liệu:** 100% trích dẫn trong bài thuộc Kho tài liệu xác thực hoặc do thành viên cung cấp. Mọi chỗ thiếu nguồn đều được đánh dấu rõ bằng thẻ `[CẦN BỔ SUNG TRÍCH DẪN: ...]`.
- [ ] **Đúng quy tắc Biến kiểm soát đơn mục:** Không đưa biến kiểm soát đơn mục vào kiểm định thang đo phản ánh (Outer Loadings, Alpha, CR, AVE, HTMT), nhưng đã báo cáo đầy đủ VIF và tác động trong Inner Model.

## 3. Kiểm định Cấu trúc học thuật & Văn phong NEU
- [ ] **Chống viết tóm tắt kiểu đề cương:** Không dùng gạch đầu dòng tràn lan cho các đoạn phân tích; mỗi luận điểm được triển khai thành đoạn văn hoàn chỉnh có câu chủ đề, cơ chế lập luận, dẫn chứng và chuyển ý.
- [ ] **Thống nhất ngôi xưng & thuật ngữ:** Dùng nhất quán ngôi thứ ba (*nhóm tác giả / nhóm nghiên cứu / nghiên cứu này*); không nhầm lẫn giải nghĩa thuật ngữ tiếng Anh/tiếng Việt (ví dụ: không nhầm EFA là khẳng định hay TPB là Theory of Planned Action).
- [ ] **Chuẩn định dạng Bảng, Hình & Số thập phân:**
  - Bảng đánh số `Bảng [Số chương].[Số thứ tự]` (tiêu đề nằm **trên** bảng, nguồn nằm **dưới** bảng).
  - Hình đánh số `Hình [Số chương].[Số thứ tự]` (tiêu đề và nguồn nằm **dưới** hình).
  - Dẫn chiếu đúng số bảng/hình trong thân bài (không lệch thứ tự).
  - Thống nhất quy tắc dấu thập phân xuyên suốt cả chương.
- [ ] **Chuẩn trích dẫn APA 7th trong văn bản:**
  - 1 tác giả: `(Thaler, 1999)` hoặc `Thaler (1999)`
  - 2 tác giả: `(Lusardi & Mitchell, 2014)` hoặc `Lusardi và Mitchell (2014)`
  - 3 tác giả trở lên: `(Ashby et al., 2025)` hoặc `Ashby và cộng sự (2025)` (thống nhất dùng `et al.` hoặc `và cộng sự` xuyên suốt cả bài theo quy ước của nhóm).
