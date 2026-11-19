# BỘ LỌC KIỂM ĐỊNH CHẤT LƯỢNG TRƯỚC KHI XUẤT BẢN THẢO (10-POINT QA GATE)

AI tự động chạy toàn bộ 10 tiêu chí chuẩn khoa học (Tầng 1) dưới đây trước khi trả bản thảo cho thành viên. **Lưu ý:** Bộ lọc này chỉ kiểm soát tính chuẩn mực khoa học và đồng bộ nhóm; tuyệt đối không dùng để bác bỏ số liệu thực tế mới, nguồn tài liệu mới hoặc cách diễn đạt học thuật sắc bén hơn của tác giả.

---

## 1. Kiểm định Tính nhất quán & Đồng bộ tiến hóa của nhóm
- [ ] **Khớp thuật ngữ & Ký hiệu hiện hành:** Tên biến, mã biến quan sát và ký hiệu viết tắt khớp với `templates/project-context.md` hoặc bản cập nhật mới nhất do thành viên cung cấp trong phiên làm việc.
- [ ] **Đánh dấu đồng bộ (Sync Alert):** Nếu phiên viết có phát sinh nguồn tài liệu mới, biến số điều chỉnh (loại/tách biến) hoặc kiểm định bổ sung so với khung ban đầu, đã ghi chú rõ vào mục *Ghi chú bàn giao & Đồng bộ* cuối bài để nhóm cập nhật chung.
- [ ] **Khớp mạch liên chương:** Nếu viết từ Chương Kết quả/Thảo luận trở đi, đã đối chiếu khớp hoàn toàn với số liệu thực tế tại `templates/chapter-handoff.md` hoặc output phần mềm mới nhất.

## 2. Kiểm định Trung thực khoa học & Chống bịa đặt (Zero-Hallucination)
- [ ] **Zero Number Drift:** Mọi con số (cỡ mẫu $N$, tần số, tỷ lệ %, hệ số $\beta$, $t$, $p$, VIF, $R^2$, $f^2$, Alpha, CR, AVE, HTMT) trong đoạn văn khớp 100% với bảng số liệu thực tế ngay cạnh. Tổng tỷ lệ thành phần bằng đúng $100\%$.
- [ ] **Chống bịa tài liệu:** 100% trích dẫn trong bài đến từ Kho tài liệu xác thực hoặc nguồn mới do chính thành viên cung cấp trong phiên chat. Mọi chỗ thiếu nguồn đều được gắn thẻ `[CẦN BỔ SUNG TRÍCH DẪN: ...]`.
- [ ] **Đúng quy tắc Biến kiểm soát đơn mục & Minh bạch tinh lọc:** Không đưa biến kiểm soát đơn mục vào kiểm định thang đo phản ánh, nhưng đã báo cáo đầy đủ VIF và tác động trong Inner Model; báo cáo trung thực mọi biến bị loại hoặc giả thuyết bị bác bỏ.

## 3. Kiểm định Cấu trúc học thuật & Văn phong NEU
- [ ] **Độ sâu lập luận toàn văn:** Không viết kiểu gạch đầu dòng tóm tắt như đề cương; mỗi luận điểm được triển khai thành đoạn văn học thuật mạch lạc (linh hoạt theo lối viết hay nhất của tác giả miễn đảm bảo logic khoa học).
- [ ] **Thống nhất ngôi xưng & thuật ngữ:** Dùng nhất quán ngôi thứ ba (*nhóm tác giả / nhóm nghiên cứu / nghiên cứu này*), văn phong khách quan, không nhầm lẫn giải nghĩa thuật ngữ tiếng Anh/tiếng Việt.
- [ ] **Chuẩn định dạng Bảng, Hình & Số thập phân:**
  - Bảng đánh số `Bảng [Số chương].[Số thứ tự]` (tiêu đề nằm **trên** bảng, nguồn nằm **dưới** bảng).
  - Hình đánh số `Hình [Số chương].[Số thứ tự]` (tiêu đề và nguồn nằm **dưới** hình).
  - Dẫn chiếu đúng số bảng/hình trong thân bài và thống nhất dấu thập phân xuyên suốt chương.
- [ ] **Chuẩn trích dẫn APA 7th trong văn bản:**
  - 1 tác giả: `(Thaler, 1999)` hoặc `Thaler (1999)`
  - 2 tác giả: `(Lusardi & Mitchell, 2014)` hoặc `Lusardi và Mitchell (2014)`
  - 3 tác giả trở lên: `(Ashby et al., 2025)` hoặc `Ashby và cộng sự (2025)` (thống nhất dùng một dạng xuyên suốt cả bài).
